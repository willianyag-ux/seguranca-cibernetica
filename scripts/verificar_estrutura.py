from pathlib import Path
import hashlib

root=Path(__file__).resolve().parent.parent
required=[
    'SKILL.md', 'PROMPT_UNIVERSAL.md', 'AGENTS.md','CLAUDE.md','GEMINI.md',
    'README.md', '.github/copilot-instructions.md',
    '.cursor/rules/seguranca-conectai.mdc',
    '.claude/skills/seguranca-conectai/SKILL.md',
    'referencias/checklist-auditoria.md',
    'referencias/criterios-de-aceite.md',
    'referencias/modelo-relatorio.md',
    'referencias/guia-de-uso.md'
]
missing=[p for p in required if not (root/p).is_file()]
if missing:
    raise SystemExit('ERRO: arquivos ausentes: ' + ', '.join(missing))

main=(root/'SKILL.md').read_bytes()
copy=(root/'.claude/skills/seguranca-conectai/SKILL.md').read_bytes()
assert main==copy, 'SKILL.md nativo do Claude divergente do arquivo principal.'
for p in (root/'referencias').glob('*.md'):
    counterpart=root/'.claude/skills/seguranca-conectai/referencias'/p.name
    assert counterpart.exists() and p.read_bytes()==counterpart.read_bytes(), f'Referência divergente: {p.name}'
assert main.startswith(b'---\nname:'), 'Frontmatter da skill inválido.'
assert len(main)>2000, 'SKILL.md parece incompleto.'
assert len((root/'PROMPT_UNIVERSAL.md').read_bytes())>len(main), 'Prompt universal deve ser autossuficiente.'
print('OK: todos os arquivos obrigatórios existem; skill Claude e referências sincronizadas; prompt universal presente.')
