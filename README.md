# Segurança ConectAI | Skill universal para IA

**Repositório portátil** com um protocolo de auditoria, correção controlada, testes e relatórios de segurança, utilizável em **ChatGPT, Claude, Gemini, Codex, Cursor, GitHub Copilot e outros assistentes**.

> **Importante:** "universal" significa que o **conteúdo pode ser utilizado por qualquer IA capaz de ler texto Markdown**. Não significa instalação automática em todas as plataformas. Cada ferramenta tem seus próprios mecanismos de leitura de regras e permissões.

## Início rápido

**Sem instalação, em qualquer chat de IA**

1. Abra [`PROMPT_UNIVERSAL.md`](PROMPT_UNIVERSAL.md), copie o conteúdo integral ou envie esse arquivo à IA.
2. Disponibilize código ou repositório apenas se possuir autorização de acesso; não cole senhas, `.env` ou tokens.
3. Solicite: **"Use Segurança ConectAI e execute apenas o diagnóstico, sem alterações"**.
4. Analise a matriz de riscos e aprove explicitamente escopo e ambiente antes de qualquer correção.

**Com integração no editor / agente**

| Plataforma | Arquivo preparado | Como funciona |
|---|---|---|
| ChatGPT ou outra IA no navegador | `PROMPT_UNIVERSAL.md` | Anexar ou colar manualmente |
| Claude no navegador | `.claude/skills/seguranca-conectai/` | Criar ZIP só dessa pasta e importar como Skill quando disponível |
| Claude Code | `CLAUDE.md` e `.claude/skills/seguranca-conectai/SKILL.md` | Ler instruções do projeto e skill local |
| OpenAI Codex | `AGENTS.md` | Instruções de projeto |
| Gemini CLI | `GEMINI.md` | Contexto do projeto |
| GitHub Copilot | `.github/copilot-instructions.md` e `AGENTS.md` | Instruções de repositório |
| Cursor | `.cursor/rules/seguranca-conectai.mdc` | Regra de projeto |

**Os arquivos de integração apenas direcionam a IA para `SKILL.md` e exigem obediência às regras críticas.** Para utilizá-los dentro do repositório de código do ConectAI, copie esses arquivos juntamente com `SKILL.md` e `referencias/`, avaliando conflitos com instruções preexistentes. Não sobrescreva cegamente configurações que já existam.

## Conteúdo do repositório

```text
Seguranca-ConectAI-Universal/
├── README.md                     # Instruções de uso
├── SKILL.md                      # Fonte principal do protocolo
├── PROMPT_UNIVERSAL.md           # Texto pronto para qualquer chat de IA
├── AGENTS.md                     # Codex e agentes compatíveis
├── CLAUDE.md                     # Claude Code
├── GEMINI.md                     # Gemini CLI
├── .claude/skills/seguranca-conectai/  # Cópia nativa da skill do Claude
├── .github/copilot-instructions.md    # GitHub Copilot
├── .github/workflows/validar-skill.yml
├── .cursor/rules/seguranca-conectai.mdc
├── referencias/                  # Checklist, aceite, relatório e guia
├── prompts/                      # Exemplos de acionamento por fase
├── scripts/                      # Verificação local de consistência
└── docs/                         # Publicação segura no GitHub
```

## Política de segurança da execução

- Diagnóstico é **somente leitura** e não permite alterar o sistema.
- Mudanças no código exigem aprovação de escopo e ambiente; **produção exige aprovação independente**.
- Integração com Protheus continua exclusivamente **SELECT, sem alterações**.
- Testes ativos, scanners, alterações de credenciais, rotações, deploy e mudanças de infraestrutura requerem aprovação separada.
- Evidências são mascaradas; não publicar dados de colaboradores, segredos ou configurações internas.
- **Não há garantia de ausência de vulnerabilidades**. Toda conclusão requer evidências e explicitação das limitações.

## Para publicar futuramente no GitHub

Leia [`docs/PUBLICACAO_GITHUB.md`](docs/PUBLICACAO_GITHUB.md). **Recomenda-se iniciar com repositório privado**, devido a detalhes operacionais e do domínio de RH. O projeto foi preparado para Git, mas **não foi publicado**.

## Referências técnicas

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [Instruções de repositório do GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- [Instruções AGENTS.md do Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [GEMINI.md do Gemini CLI](https://geminicli.com/docs/cli/gemini-md/)
- [Skills do Claude](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Regras do Cursor](https://docs.cursor.com/context/rules-for-ai)

## Licenciamento

Nenhuma licença pública foi concedida neste pacote. Defina uma licença conscientemente, se decidir abrir o código/instruções para terceiros.