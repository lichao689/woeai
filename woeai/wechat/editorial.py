"""Mechanical checks for the current editorial structure, not semantic approval."""
import re

from woeai.publications.taxonomy import RESEARCH_FAMILY_ORDER

ENGINEERING_HEADING = '## 从论文到工程'
AI_STATEMENT = '本文由 AI 辅助整理与撰写'
READING_REMINDER = re.compile(r'^点击[“\"]?阅读原文', re.M)


def article_title_findings(text: str, research_family: str) -> list[str]:
    """Match the article H1 to this paper's registered primary research family."""
    titles = re.findall(r'^# ([^\r\n]+)', text, re.M)
    prefix = f'{research_family} | '
    if (research_family not in RESEARCH_FAMILY_ORDER or len(titles) != 1 or
            not titles[0].startswith(prefix) or not titles[0][len(prefix):].strip()):
        return [f'H1 must use custom.research_family: {prefix}<中文标题>']
    return []


def article_structure_findings(text: str) -> list[str]:
    """Validate an explicitly selected article against the current ending contract.

    Legacy articles are not automatically migrated. Engineering value, evidence,
    repetition and the editorial value/condition balance require human review.
    """
    findings = []
    headings = list(re.finditer(r'^## 从论文到工程\s*$', text, re.M))
    if len(headings) != 1:
        return ['Expected exactly one 从论文到工程 heading']
    heading = headings[0]
    reminders = list(READING_REMINDER.finditer(text))
    if len(reminders) != 1 or reminders[0].start() < heading.end():
        return ['Place 从论文到工程 before one 阅读原文 reminder']
    ending = text[heading.end():reminders[0].start()].strip()
    paragraphs = re.split(r'\n\s*\n', ending) if ending else []
    if len(paragraphs) != 1 or re.search(r'^(?:#{1,6}\s|[-*+]\s|\d+[.)]\s|!\[|\$\$)', ending, re.M):
        findings.append('从论文到工程 must contain one natural paragraph without extra sections')
    if text.count(AI_STATEMENT) != 1 or not text.rstrip().endswith(AI_STATEMENT):
        findings.append('Keep the exact AI statement once at the end')
    problem = re.search(r'^## 研究问题与解决思路\s*$', text, re.M)
    if not problem or problem.start() > heading.start():
        findings.append('Keep 研究问题与解决思路 before the engineering ending')
    if re.search(r'^## (?!延伸阅读\s*$).+', text[reminders[0].start():], re.M):
        findings.append('Place all scientific sections before 从论文到工程')
    return findings
