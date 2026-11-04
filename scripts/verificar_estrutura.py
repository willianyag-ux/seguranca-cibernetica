"""Validação estática e sem rede do protocolo Segurança Cibernética."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = (
    "SKILL.md", "PROMPT_UNIVERSAL.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
    ".github/copilot-instructions.md", ".github/workflows/validar-skill.yml",
    ".cursor/rules/seguranca-cibernetica.mdc",
    ".claude/skills/seguranca-cibernetica/SKILL.md",
    "referencias/checklist-auditoria.md", "referencias/criterios-de-aceite.md",
    "referencias/modelo-relatorio.md", "referencias/guia-de-uso.md",
    "referencias/matriz-autorizacoes.md", "referencias/seguranca-agentes-ia.md",
    "tests/test_protocolo.py",
)
PREFIX = (
    "# PROMPT UNIVERSAL | Segurança Cibernética\n\n"
    "**Uso em qualquer IA:** aplique integralmente o protocolo abaixo, "
    "respeitando o acesso e as autorizações efetivamente concedidos. "
    "Quando não houver acesso ao código ou às ferramentas, relate limitações; "
    "jamais simule auditoria ou teste. Comece pelo diagnóstico somente leitura.\n\n"
)

def fail(message):
    raise ValueError(message)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def validate():
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        fail("Arquivos obrigatórios ausentes: " + ", ".join(missing))
    main = read("SKILL.md")
    native = read(".claude/skills/seguranca-cibernetica/SKILL.md")
    if main != native:
        fail("SKILL.md e skill nativa Claude divergentes")
    if not main.startswith("---\nname: seguranca-cibernetica\n"):
        fail("Frontmatter ou nome da skill inválido")
    if len(main) < 2000:
        fail("Protocolo principal incompleto")
    refs = sorted((ROOT / "referencias").glob("*.md"))
    if not refs:
        fail("Diretório de referências vazio")
    for source in refs:
        counterpart = ROOT / ".claude/skills/seguranca-cibernetica/referencias" / source.name
        if not counterpart.is_file() or counterpart.read_bytes() != source.read_bytes():
            fail("Referência Claude ausente ou divergente: " + source.name)
    expected_prompt = PREFIX + re.sub(r"\A---\n.*?\n---\n\n", "", main, count=1, flags=re.DOTALL)
    if read("PROMPT_UNIVERSAL.md") != expected_prompt:
        fail("PROMPT_UNIVERSAL.md divergiu de SKILL.md: regenere-o")
    for path in ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md", ".cursor/rules/seguranca-cibernetica.mdc"):
        content = read(path)
        if "SKILL.md" not in content:
            fail("Adaptador sem referência ao protocolo: " + path)
    if "MIT License" not in read("LICENSE"):
        fail("Licença MIT ausente ou inválida")
    if not all(tag in main for tag in ("matriz-autorizacoes.md", "seguranca-agentes-ia.md")):
        fail("Protocolo não referencia políticas essenciais")
    print("OK: arquivos, compatibilidade, licença, prompt universal, referências e autorizações consistentes.")

if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError) as exc:
        print("FALHA:", exc, file=sys.stderr)
        raise SystemExit(1)
