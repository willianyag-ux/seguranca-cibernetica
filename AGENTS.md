# Instruções para agentes de programação: Segurança Cibernética

Ao receber pedidos de auditoria de segurança, proteção de dados, análise de vulnerabilidades, correção de riscos ou verificação de publicação, **leia e siga `SKILL.md` integralmente** e carregue apenas as referências necessárias em `referencias/`.

## Regras de proteção prioritárias

- Inicie sempre com diagnóstico **somente leitura** e não altere arquivos, pacotes, infra, banco ou produção sem autorização explícita para essa fase.
- Não faça deploy nem push automaticamente. Homologação e produção exigem aprovações separadas.
- Integração TOTVS Protheus é **exclusivamente SELECT**, sem qualquer escrita ou ampliação de privilégios.
- Não imprima, exponha, registre nem publique senhas, tokens, dados pessoais ou conteúdo de `.env`; masque evidências.
- Não execute exploração, scanners ativos, brute force, fuzzing ou testes destrutivos em produção sem autorização específica.
- Preserve funcionalidades, segregação de perfis, relatórios, aprovações e integrações. Prefira mudanças mínimas, reversíveis e testáveis.
- Não diga que algo foi corrigido sem teste e evidência; classifique o não testado como **não verificado**.
- Sempre responda em português do Brasil.

Ao terminar o diagnóstico, gere a matriz de achados usando `referencias/modelo-relatorio.md` e **pare para aprovação** antes de implementar.
