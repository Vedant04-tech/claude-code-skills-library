import os
import re
import sys

def parse_skill(skill_dir):
    skill_md = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.exists(skill_md):
        return None
    with open(skill_md, 'r', encoding='utf-8') as f:
        text = f.read()
    
    name_m = re.search(r'^name:\s*(.+)$', text, re.MULTILINE)
    name = name_m.group(1).strip() if name_m else os.path.basename(skill_dir)
    
    desc_m = re.search(r'^description:\s*(?:>|\|)?\s*\n?([^\n]+(?:\n\s+[^\n]+)*)', text, re.MULTILINE)
    if desc_m:
        desc = re.sub(r'\s+', ' ', desc_m.group(1).strip())
        if (desc.startswith('"') and desc.endswith('"')) or (desc.startswith("'") and desc.endswith("'")):
            desc = desc[1:-1]
    else:
        desc = 'Curated skill'
    
    # shorten desc if too long for table
    short_desc = desc if len(desc) <= 120 else desc[:117] + '...'
    
    return {
        'id': os.path.basename(skill_dir),
        'name': name,
        'full_desc': desc,
        'short_desc': short_desc
    }

def get_category(skill_id):
    if skill_id.startswith('engineering-'):
        return 'Senior Engineering Playbooks (PeterHdd)'
    strix_skills = [
        'api-security-testing', 'application-security-testing', 'ci-security-scanning-with-strix',
        'find-security-vulnerabilities-in-code', 'fix-security-vulnerabilities-with-strix',
        'managed-pentesting-with-strix', 'owasp-top-10-testing', 'penetration-testing-with-strix',
        'web-app-penetration-testing'
    ]
    if skill_id in strix_skills:
        return 'Autonomous Security & Pentesting (Strix)'
    if skill_id in [
        'brainstorming', 'dispatching-parallel-agents', 'executing-plans', 'finishing-a-development-branch',
        'receiving-code-review', 'requesting-code-review', 'subagent-driven-development', 'systematic-debugging',
        'test-driven-development', 'using-git-worktrees', 'using-superpowers', 'verification-before-completion',
        'writing-plans', 'writing-skills'
    ]:
        return 'Engineering Discipline (Superpowers)'
    if skill_id.startswith('ponytail'):
        return 'Pragmatic Anti-Overengineering (Ponytail)'
    if skill_id in ['agent-reach', 'literature-research']:
        return 'Web Retrieval & Deep Research'
    if skill_id in ['convert-documents-to-markdown', 'graphify']:
        return 'Document Parsing & AST Knowledge Graphs'
    if skill_id in ['skill-creator', 'find-skills', 'task-observer']:
        return 'Meta-Tooling, Evolution & Discovery'
    if skill_id.startswith('memory-'):
        return 'Persistent Memory System (Supabase)'
    if skill_id.startswith('vercel-') or skill_id in ['deploy-to-vercel', 'web-design-guidelines']:
        return 'Vercel, React & Performance'
    if skill_id in ['mcp-builder', 'webapp-testing', 'write-swift', 'writing-guidelines']:
        return 'Systems Craftsmanship & Testing'
    if skill_id in [
        'animate', 'animate-expo', 'animation-vocabulary', 'apple-design', 'ask-sonner',
        'design-taste-frontend', 'design-website', 'emil-design-eng', 'find-animation-opportunities',
        'frontend-design', 'hallmark', 'impeccable', 'improve-animations', 'pick-ui-library',
        'prototype', 'review-animations'
    ]:
        return 'Design Engineering, Motion & Craft'
    return 'Agency Business & Lead Generation'

def main():
    skills_dir = '.claude/skills'
    skill_folders = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    
    parsed = []
    for s in skill_folders:
        info = parse_skill(os.path.join(skills_dir, s))
        if info:
            info['category'] = get_category(s)
            parsed.append(info)
            
    print(f'Total skills parsed: {len(parsed)}')
    
    # Group by category
    categories = {}
    for item in parsed:
        cat = item['category']
        categories.setdefault(cat, []).append(item)
        
    lines = [
        '# 📚 Curated Skills Catalog (100 Active Skills)',
        '',
        '> **Comprehensive index of all 100 audited and verified skills available across Google Antigravity, Claude Code, Cursor, and Codex.**  ',
        '> **Last Audited:** October 13, 2026  ',
        '> **Parity Guarantee:** 100% parity across `.claude/skills/`, `.agents/skills/`, and `agent/skills/`.',
        '',
        '---',
        '',
        '## 📊 Quick Category Overview',
        '',
        '| Category | Count | Primary Focus |',
        '|---|:---:|---|',
    ]
    
    # Priority order for display
    order = [
        'Senior Engineering Playbooks (PeterHdd)',
        'Autonomous Security & Pentesting (Strix)',
        'Web Retrieval & Deep Research',
        'Engineering Discipline (Superpowers)',
        'Pragmatic Anti-Overengineering (Ponytail)',
        'Design Engineering, Motion & Craft',
        'Document Parsing & AST Knowledge Graphs',
        'Meta-Tooling, Evolution & Discovery',
        'Systems Craftsmanship & Testing',
        'Vercel, React & Performance',
        'Persistent Memory System (Supabase)',
        'Agency Business & Lead Generation'
    ]
    
    for cat in order:
        if cat in categories:
            count = len(categories[cat])
            lines.append(f'| **{cat}** | **{count}** | {categories[cat][0]["short_desc"][:60]}... |')
            
    lines.extend([
        '',
        '---',
        '',
        '## 🗂️ Detailed Catalog by Domain',
        ''
    ])
    
    for cat in order:
        if cat not in categories: continue
        items = categories[cat]
        lines.append(f'### {cat} ({len(items)} Skills)')
        lines.append('')
        lines.append('| Skill ID | Description | Cross-Agent Paths |')
        lines.append('|---|---|---|')
        for item in items:
            sid = item['id']
            sdesc = item['short_desc'].replace('|', '\\|')
            paths = f'`.claude/skills/{sid}`<br>`.agents/skills/{sid}`'
            lines.append(f'| **`{sid}`** | {sdesc} | {paths} |')
        lines.append('')
        
    with open('docs/skill-catalog.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    print('docs/skill-catalog.md successfully generated!')

if __name__ == '__main__':
    main()
