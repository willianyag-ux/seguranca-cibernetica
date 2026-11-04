# Como contribuir

Contribuições são bem-vindas conforme a licença MIT. **Não inclua dados confidenciais, credenciais, código proprietário, URLs privadas ou informações pessoais** em commits, issues e pull requests.

## Fluxo recomendado

1. Antes de contribuir, leia `SKILL.md`, `SECURITY.md`, `referencias/matriz-autorizacoes.md` e `referencias/seguranca-agentes-ia.md`.
2. Para melhorias, crie uma branch e um pull request com escopo limitado e descrição das mudanças.
3. Para vulnerabilidades exploráveis, use canal privado, não uma issue pública.
4. Execute `python3 scripts/verificar_estrutura.py` e `python3 -m unittest discover -s tests -v`.
5. Mantenha `SKILL.md` sincronizado com a cópia da skill Claude; mantenha referências duplicadas idênticas.
6. Ao atualizar o protocolo, regenere `PROMPT_UNIVERSAL.md` para garantir equivalência de conteúdo.
7. Documente riscos, impacto em outras IAs, testes, retrocompatibilidade e atualização de `CHANGELOG.md`.

## Qualidade mínima

- Não realizar chamadas à rede, varreduras, escrita em produção nem coleta de segredos nos testes do repositório.
- Preferir bibliotecas padrão e comandos executáveis sem credenciais.
- Toda instrução específica de um produto ou sistema deve ser **condicional**.
- Não substituir validação técnica por uma pontuação de segurança sem evidências.
- Revisão humana antes de integração na branch principal.
