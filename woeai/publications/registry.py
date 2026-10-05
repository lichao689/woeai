"""Single public-safe CSL bibliography and independent publication workflows.

Zotero owns bibliographic facts. This file's custom fields own repo workflow
state; compatibility YAML/map/dashboard files are generated, never edited.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

REGISTRY_PATH = Path('docs/data/publications.json')
MAP_PATH = Path('docs/data/publication-research-map.json')
BACKLOG_PATH = Path('wechat/backlog/selected-papers.yml')
DASHBOARD_PATH = Path('project/publication-progress.md')


def load_registry(root: Path) -> list[dict[str, Any]]:
    records = json.loads((root / REGISTRY_PATH).read_text(encoding='utf-8'))
    if not isinstance(records, list):
        raise ValueError('Publication registry must be a CSL-JSON array')
    return records


def save_registry(root: Path, records: list[dict[str, Any]]) -> None:
    problems = validate_registry(records, root, check_evidence=False)
    if problems:
        raise ValueError('; '.join(problems))
    path = root / REGISTRY_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def research_map(records: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    return {r['id']: {k:r['custom'][k] for k in ('research_family','subdirection')} for r in records}


RTD_STATES = {'unregistered','planned','drafting','awaiting_audit','verified','blocked'}
WECHAT_STATES = {'unregistered','planned','drafting','awaiting_review','draft_created','ready_to_publish','published','blocked'}
ISSUE_URL = re.compile(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/[1-9][0-9]*\Z')
SHA256 = re.compile(r'[a-f0-9]{64}\Z')


def _public_path(root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or any(p.startswith('.') for p in path.parts) or any(p in {'private','secrets'} for p in path.parts):
        raise ValueError(f'Not a public repository path: {value}')
    resolved=(root/path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes repository: {value}')
    return resolved



def _referenced_files(root: Path, paths: set[str]) -> set[str]:
    """Resolve local body dependencies; remote images cannot be byte-verified.

    Supports the Markdown images, RST image/figure/include directives and
    review cover fields used by our publishing tools. Includes are recursive.
    """
    from urllib.parse import unquote, urlsplit
    found: set[str] = set()
    pending = list(paths)
    visited: set[str] = set()
    while pending:
        value = pending.pop()
        if value in visited:
            continue
        visited.add(value)
        source = _public_path(root, value)
        if not source.is_file() or source.suffix not in {'.rst', '.md'}:
            continue
        text = source.read_text(encoding='utf-8')
        relative = re.findall(r'^\s*\.\. (?:\|[^|]+\| )?(?:image|figure|include)::\s*(\S+)\s*$', text, re.M)
        relative += re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
        absolute = re.findall(r'^(?:rtd_cover_image|wechat_cover_image|cover_image):\s*["\']?([^\s"\']+)', text, re.M)
        absolute += re.findall(r'封面素材[^`\n]*`([^`]+)`', text)
        for target, base in [(v, source.parent) for v in relative] + [(v, root) for v in absolute]:
            url = urlsplit(target)
            if url.scheme or url.netloc:
                raise ValueError('Remote image dependencies require a locally approved public asset')
            # Markdown titles are not used by the current renderer; angle
            # brackets are permitted by Markdown and stripped before resolving.
            resolved = (base / unquote(url.path.strip('<>'))).resolve()
            if not resolved.is_relative_to(root.resolve()):
                raise ValueError('Referenced asset escapes repository')
            relative_path = resolved.relative_to(root.resolve()).as_posix()
            _public_path(root, relative_path)
            found.add(relative_path)
            if resolved.suffix == '.rst':
                pending.append(relative_path)
    return found


def workflow_fingerprint(record: dict[str, Any], channel: str, root: Path) -> str:
    """Hash input meaning and bytes, excluding workflow assertions and this hash.

    Source hash represents approved original bytes without publishing a path.
    Include all per-paper public assets conservatively, plus the channel guide,
    body and evidence review. A review edit deliberately invalidates approval.
    """
    custom=record['custom']; workflow=custom[channel]; ref=custom['publication_ref']
    paths={workflow['path']}
    if workflow.get('review_path'): paths.add(workflow['review_path'])
    for evidence in workflow.get('evidence',{}).values():
        if isinstance(evidence,dict) and evidence.get('review_path'): paths.add(evidence['review_path'])
    # Guides are specifications, not body documents; their illustrative image
    # directives are hashed as text but are not actual content dependencies.
    paths.update(_referenced_files(root, paths))
    guide='project/guides/paper-deep-dive-rst.md' if channel=='rtd' else 'wechat/STYLE.md'
    paths.add(guide)
    assets=root/'wechat/assets/public-safe'/ref
    if assets.exists():
        paths.update(p.relative_to(root).as_posix() for p in assets.rglob('*') if p.is_file())
    files={}
    for value in sorted(paths):
        path=_public_path(root,value)
        files[value]=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    payload={'bibliography':{k:v for k,v in record.items() if k!='custom'},
             'source':custom.get('source',{}),'files':files,'kind':workflow.get('kind')}
    return hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def workflow_verified(record: dict[str,Any], channel: str, root: Path) -> bool:
    workflow=record['custom'][channel]; source=record['custom'].get('source',{})
    required=('source_identity','full_paper_coverage','public_safety') if channel=='rtd' else ('source_identity','facts','public_safety','formula_preview','figure_preview','cover_preview')
    if channel=='rtd' and (workflow.get('status')!='verified' or workflow.get('kind')!='full_paper'): return False
    if channel=='wechat' and workflow.get('status') not in {'ready_to_publish','published'}: return False
    if source.get('status')!='verified' or not SHA256.fullmatch(source.get('sha256','')): return False
    evidence=workflow.get('evidence',{}).get('verified',{})
    if not evidence.get('recorded_at') or not evidence.get('review_path'): return False
    if not all(evidence.get('checks',{}).get(k) is True for k in required): return False
    try:
        if not _public_path(root,workflow['path']).is_file() or not _public_path(root,evidence['review_path']).is_file(): return False
        dependencies = _referenced_files(root, {workflow['path'], evidence['review_path']})
        if any(not _public_path(root, path).is_file() for path in dependencies): return False
        return evidence.get('fingerprint')==workflow_fingerprint(record,channel,root)
    except (ValueError,OSError):
        return False


def validate_registry(records: list[dict[str, Any]], root: Path, *, check_evidence: bool = True) -> list[str]:
    from woeai.publications import RESEARCH_SUBDIRECTION_ORDER
    problems=[]; ids=set(); refs=set()
    # Deliberately small CSL subset used by our Zotero adapter; custom carries
    # all non-CSL fields. No display-name splitting or rendered-citation parsing.
    allowed={'id','type','title','container-title','issued','DOI','URL','author','volume','issue','page','abstract','language','custom'}
    for row in records:
        key=row.get('id'); custom=row.get('custom',{}); ref=custom.get('publication_ref','')
        prefix=str(key)
        if not isinstance(key,str) or not key or key in ids: problems.append(f'{prefix}: duplicate/missing id')
        ids.add(key)
        if not re.fullmatch(r'ref-[A-Za-z0-9_-]+',ref) or ref in refs: problems.append(f'{prefix}: invalid/duplicate publication_ref')
        refs.add(ref)
        if row.get('type')!='article-journal' or not isinstance(row.get('title'),str) or not row.get('title'): problems.append(f'{prefix}: invalid CSL type/title')
        if set(row)-allowed: problems.append(f'{prefix}: unknown CSL properties')
        family=custom.get('research_family'); sub=custom.get('subdirection')
        if sub not in RESEARCH_SUBDIRECTION_ORDER.get(family,()): problems.append(f'{prefix}: invalid research mapping')
        for channel,states in (('rtd',RTD_STATES),('wechat',WECHAT_STATES)):
            workflow=custom.get(channel,{})
            if channel=='wechat' and not isinstance(workflow.get('selected'),bool): problems.append(f'{prefix}: wechat.selected must be a boolean')
            if workflow.get('status') not in states: problems.append(f'{prefix}: invalid {channel} state')
            issues=workflow.get('issues',[])
            if not isinstance(issues,list) or any(not isinstance(u,str) or not ISSUE_URL.fullmatch(u) for u in issues): problems.append(f'{prefix}: invalid {channel} issue URL')
            try:
                _public_path(root,workflow['path'])
                if workflow.get('review_path'): _public_path(root,workflow['review_path'])
                for e in workflow.get('evidence',{}).values():
                    if e.get('review_path'): _public_path(root,e['review_path'])
            except (ValueError,KeyError,TypeError): problems.append(f'{prefix}: invalid {channel} public path')
            needs_verification=(channel=='rtd' and workflow.get('status')=='verified') or (channel=='wechat' and workflow.get('status') in {'ready_to_publish','published'})
            if check_evidence and needs_verification and not workflow_verified(row,channel,root): problems.append(f'{prefix}: missing/stale {channel} verification')
            if channel=='wechat' and workflow.get('status')=='published':
                from urllib.parse import urlparse
                url=urlparse(workflow.get('latest_published_url',''))
                if url.scheme!='https' or url.netloc!='mp.weixin.qq.com' or not url.path.startswith('/s'): problems.append(f'{prefix}: publication URL required')
        public=json.dumps(custom,ensure_ascii=False)
        if re.search(r'wechat_draft_media_id|"media_id"|/Users/|/home/|/tmp/|access_token|appsecret|source\.pdf',public,re.I): problems.append(f'{prefix}: private operational material in public registry')
    return problems


def merge_zotero_items(records: list[dict[str,Any]], items: list[dict[str,Any]]) -> list[dict[str,Any]]:
    """Refresh trusted structured bibliography without mutating custom state.

    New identities must be registered/classified explicitly first. Absence from
    a refresh never deletes a previously curated publication or its history.
    """
    merged=copy.deepcopy(records); by_key={r['id']:r for r in merged}
    fields={'title':'title','publicationTitle':'container-title','DOI':'DOI','url':'URL','volume':'volume','issue':'issue','pages':'page','abstractNote':'abstract','language':'language'}
    for item in items:
        key=item['key']
        if key not in by_key:
            raise ValueError(f'{key}: register and classify new publication before Zotero refresh')
        row=by_key[key]; data=item['data']
        for source,dest in fields.items():
            if source in data:
                if data[source]: row[dest]=str(data[source])
                else: row.pop(dest,None)
        if 'creators' in data:
            authors=[]
            for creator in data['creators']:
                if creator.get('creatorType')!='author': continue
                if creator.get('name'): authors.append({'literal':creator['name']})
                else:
                    name={k:creator[v] for k,v in (('given','firstName'),('family','lastName')) if creator.get(v)}
                    if name: authors.append(name)
            if authors: row['author']=authors
            else: row.pop('author',None)
        if 'date' in data:
            date=str(data['date']); match=re.fullmatch(r'(\d{4})(?:[-/](\d{1,2}))?(?:[-/](\d{1,2}))?',date)
            if match: row['issued']={'date-parts':[[int(p) for p in match.groups() if p]]}
            elif date: row['issued']={'literal':date}
            else: row.pop('issued',None)
    return merged


def backlog_row(record: dict[str,Any]) -> dict[str,Any]:
    custom=record['custom']; workflow=custom['wechat']; parts=record.get('issued',{}).get('date-parts',[[0]])
    # Keep historic assertions exclusively in custom.legacy_backlog, not in a
    # generated view where a consumer could mistake them for current authority.
    legacy=workflow.get('legacy_backlog',{})
    row={'publication_ref':custom['publication_ref'],'zotero_key':record['id'],'title':record['title'],
         'research_family':custom['research_family'],'subdirection':custom['subdirection'],
         'original_year':parts[0][0] if parts and parts[0] else 0,
         'repost_priority':legacy.get('repost_priority',''), 'wechat_status':workflow['status'],
         'publication_mode':workflow.get('publication_mode',legacy.get('publication_mode','first_publish')),
         'previous_published_url':workflow.get('previous_published_url',''),
         'latest_published_url':workflow.get('latest_published_url',''),
         'revision_note':workflow.get('revision_note','Historical draft evidence; current backend preview and publication unconfirmed.'),
         'publication_history':workflow.get('publication_history',[]),
         'wechat_draft_created_at':workflow.get('draft_created_at',''),
         'wechat_draft_updated_at':workflow.get('draft_updated_at','')}
    return row


def generated_views(root: Path, records: list[dict[str,Any]]) -> dict[Path,str]:
    mapping={'generated_from':REGISTRY_PATH.as_posix(),'items':research_map(records)}
    selected=sorted((r for r in records if r['custom']['wechat']['selected'] is True),key=lambda r:r['custom']['wechat'].get('selection_order',r['custom'].get('order',0)))
    lines=['# GENERATED from docs/data/publications.json; do not edit.','schema_version: 2',
           'description: Generated compatibility view; registry owns workflow state.','items:']
    for row in selected:
        item=backlog_row(row)
        for n,(key,value) in enumerate(item.items()):
            encoded=str(value) if key=='publication_ref' else json.dumps(value,ensure_ascii=False)
            lines.append(('  - ' if n==0 else '    ')+f'{key}: {encoded}')
    dashboard=['# 论文制作进度（自动生成）','','来源：[publications.json](../docs/data/publications.json)。只修改清单，运行生成命令；不要手改本页。',
               '',f'共 {len(records)} 篇；公众号已选 {len(selected)} 篇。未登记表示没有结构化记录，不等于尚未开始。',
               '现有页面可访问不等于全文核验完成；历史草稿记录不等于已预览或已发布。',
               '', '| 论文 | RTD | 公众号 | 问题与证据 |','| --- | --- | --- | --- |']
    labels={'unregistered':'未登记','planned':'已计划','drafting':'制作中','awaiting_audit':'待全文核验','verified':'已核验','blocked':'受阻',
            'awaiting_review':'待审核','draft_created':'有历史/已创建草稿，待预览','ready_to_publish':'已预览待发布','published':'已发布'}
    for row in records:
        c=row['custom']; rtd=c['rtd']; wc=c['wechat']; ref=c['publication_ref']; details=[]
        for channel in ('rtd','wechat'):
            w=c[channel]
            for n,url in enumerate(w.get('issues',[]),1): details.append(f'[{channel} issue {n}]({url})')
            for name,e in w.get('evidence',{}).items():
                if e.get('review_path'): details.append(f'[{channel} {name}](../{e["review_path"]})')
            if w.get('review_path') and (root/w['review_path']).is_file(): details.append(f'[{channel} review](../{w["review_path"]})')
            if w.get('conflicts'): details.append(f'{channel} 时间记录冲突待核对')
        title=row['title'].replace('|','\\|').replace('\n',' ')
        publication=f'[{ref}](https://woeai.readthedocs.io/zh-cn/latest/Publications.html#{ref.lower()})<br>{title}'
        rlabel=labels[rtd['status']]
        if rtd['status']=='verified' and not workflow_verified(row,'rtd',root): rlabel='核验已失效，待重审'
        if (root/rtd['path']).exists(): rlabel=f'[{rlabel}](../{rtd["path"]})'
        if rtd.get('kind')=='legacy_intro': rlabel+='（历史导读）'
        elif rtd.get('kind')=='full_paper': rlabel+='（全文型）'
        wlabel=labels[wc['status']]
        if wc['status'] in {'ready_to_publish','published'} and not workflow_verified(row,'wechat',root): wlabel+='（核验已失效，待重审）'
        if (root/wc['path']).exists(): wlabel=f'[{wlabel}](../{wc["path"]})'
        if wc.get('latest_published_url'): wlabel+=f' [原文]({wc["latest_published_url"]})'
        dashboard.append(f'| {publication} | {rlabel} | {wlabel} | {"；".join(details) or "—"} |')
    return {MAP_PATH:json.dumps(mapping,ensure_ascii=False,indent=2,sort_keys=True)+'\n',
            BACKLOG_PATH:'\n'.join(lines)+'\n',DASHBOARD_PATH:'\n'.join(dashboard)+'\n'}


def write_views(root: Path, records: list[dict[str,Any]]) -> None:
    for path,text in generated_views(root,records).items():
        target=root/path; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(text,encoding='utf-8')


def check_views(root: Path, records: list[dict[str,Any]]) -> list[str]:
    return [f'{path}: generated view out of sync' for path,text in generated_views(root,records).items()
            if not (root/path).exists() or (root/path).read_text(encoding='utf-8')!=text]
