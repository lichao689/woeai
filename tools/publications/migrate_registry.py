#!/usr/bin/env python3
"""One-time conservative migration; refuses to replace an existing registry."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from woeai.publications.registry import REGISTRY_PATH, save_registry


def migrate(root: Path):
    if (root / REGISTRY_PATH).exists():
        raise ValueError('Registry already exists; migration never overwrites workflow state')
    snapshot = json.loads((root / 'docs/data/2026-06-publications-zotero-snapshot.json').read_text())
    mapping = json.loads((root / 'docs/data/publication-research-map.json').read_text())['items']
    # Parse legacy flat rows without importing the new registry-first reader.
    backlog = {}
    for block in re.split(r'^  - publication_ref: ', (root/'wechat/backlog/selected-papers.yml').read_text(),flags=re.M)[1:]:
        lines=block.splitlines(); ref=lines[0].strip(); row={}
        for line in lines[1:]:
            if ':' in line:
                key,value=line.strip().split(':',1)
                row[key]=value.strip().strip('"').strip("'")
        backlog[ref]=row
    records=[]; private={}
    full_papers={'ref-chen2024-JCP','ref-chen2024-POF','ref-chen2022-JWEIA'}
    for order,item in enumerate(snapshot['items']):
        ref=item['anchor']; key=item['zotero_key']; legacy=backlog.get(ref); selected=legacy is not None
        rtd_path=f'docs/source/paper-notes/{ref}.rst'
        article_path=f'wechat/articles/draft-public-safe/{ref}.md'
        review_path=f'wechat/articles/review/{ref}.review.md'
        public_title=item['title']
        if (root/article_path).exists():
            public_title=next((l[2:] for l in (root/article_path).read_text().splitlines() if l.startswith('# ')),public_title)
        row={'id':key,'type':'article-journal','title':item['title'],'container-title':item['publicationTitle'],
             'issued':{'date-parts':[[item['year']]]},'custom':{'publication_ref':ref,'order':order,
             **mapping[key], 'legacy_bibliography':item, 'source':{'status':'unregistered'},
             'rtd':{'status':'awaiting_audit' if selected else 'unregistered',
                    'kind':('full_paper' if ref in full_papers else 'legacy_intro') if selected else 'unregistered',
                    'path':rtd_path,'public_title':public_title,'order':list(backlog).index(ref) if selected else order,
                    'issues':[],'evidence':{}},
             'wechat':{'selected':selected,'status':'draft_created' if selected else 'unregistered',
                       'path':article_path,'review_path':review_path,'issues':[],'evidence':{},
                       'latest_published_url':''}}}
        if item.get('doi'): row['DOI']=item['doi']
        if legacy is not None:
            legacy=legacy.copy(); media=legacy.pop('wechat_draft_media_id','')
            if media: private[ref]={'media_id':media}
            channel=row['custom']['wechat']; channel['selection_order']=list(backlog).index(ref)
            channel['legacy_backlog']=legacy
            channel['draft_created_at']=legacy.get('wechat_draft_created_at','')
            channel['draft_updated_at']=legacy.get('wechat_draft_updated_at','')
            channel['historical_draft_evidence']={'source':'wechat/backlog/selected-papers.yml (pre-migration)',
                'status':legacy.get('wechat_status',''),'content_version':'unknown','preview_confirmed':False}
            review=(root/review_path).read_text()
            match=re.search(r'^wechat_draft_updated_at:\s*(.+)$',review,re.M)
            if match and match[1].strip()!=channel['draft_updated_at']:
                channel['conflicts']=[{'field':'draft_updated_at','backlog_value':channel['draft_updated_at'],
                    'review_value':match[1].strip(),'review_source':review_path,'resolution':'unresolved'}]
        records.append(row)
    # Operational identifiers stay private; they are not bibliography/evidence.
    private_path=root/'wechat/.local/registry-drafts.json'
    private_path.parent.mkdir(parents=True,exist_ok=True)
    if private_path.exists():
        private={**private,**json.loads(private_path.read_text())}
    private_path.write_text(json.dumps(private,indent=2)+'\n'); private_path.chmod(0o600)
    save_registry(root,records)
    return records

if __name__=='__main__':
    migrate(ROOT)
