"""Testes locais, determinísticos, sem rede ou segredos reais."""
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verificar_estrutura as v

class TestProtocolo(unittest.TestCase):
    def test_integridade_repositorio(self):
        v.validate()

    def test_politica_tem_niveis_e_vedacoes(self):
        matrix = v.read("referencias/matriz-autorizacoes.md")
        for tag in ("A0", "A1", "A2", "A3", "Vedado", "produção", "autorização"):
            self.assertIn(tag, matrix)

    def test_defesa_contra_injecao_documentada(self):
        text = v.read("referencias/seguranca-agentes-ia.md")
        for tag in ("prompt injection", "não confiáveis", "ferramentas", "segredos"):
            self.assertIn(tag.lower(), text.lower())

    def test_prompts_universais_nao_presumem_conectai(self):
        main = v.read("SKILL.md")
        self.assertIn("Perfil opcional: ConectAI", main)
        self.assertIn("de qualquer sistema", main)
        for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
            self.assertIn("SKILL.md", v.read(name))

    def test_detecta_copia_claude_divergente(self):
        original = v.read
        def patched(path):
            if path == ".claude/skills/seguranca-cibernetica/SKILL.md":
                return "conteúdo divergente"
            return original(path)
        with patch.object(v, "read", side_effect=patched):
            with self.assertRaisesRegex(ValueError, "divergentes"):
                v.validate()

    def test_detecta_prompt_divergente(self):
        original = v.read
        def patched(path):
            if path == "PROMPT_UNIVERSAL.md":
                return "documento desatualizado"
            return original(path)
        with patch.object(v, "read", side_effect=patched):
            with self.assertRaisesRegex(ValueError, "divergiu"):
                v.validate()

if __name__ == "__main__":
    unittest.main()
