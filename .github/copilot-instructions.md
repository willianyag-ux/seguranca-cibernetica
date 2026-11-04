# Diretrizes de segurança para GitHub Copilot

Este repositório contém o protocolo **Segurança ConectAI** em `SKILL.md`. Em tarefas de segurança, siga o arquivo principal e os artefatos relevantes em `referencias/`.

- Diagnostique sem alterar arquivos, dependências ou infraestrutura antes de obter aprovação explícita.
- Não faça push, abra issue pública com falha sensível, revogue chaves ou publique em produção sem autorização.
- Preserve integração Protheus **somente leitura (SELECT)** e regras de acesso e sigilo de RH.
- Omitir/mascarar segredos, tokens, `.env`, identificadores pessoais e detalhes internos.
- Priorize patches mínimos, testes de regressão e evidências verificáveis.
- Classifique itens não testados como **não verificados** e nunca prometa segurança absoluta.
- Responda em português do Brasil.
