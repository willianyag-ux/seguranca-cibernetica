# Comandos de ativação em qualquer IA

Todos os comandos presumem que a IA recebeu `PROMPT_UNIVERSAL.md` ou possui acesso a `SKILL.md` e `referencias/`.

## Diagnóstico completo, sem mudar nada

> Aplique o protocolo Segurança ConectAI. Analise o repositório e execute somente inventário e auditoria sem alterações. Identifique vulnerabilidades com evidência mascarada, severidade e plano de remediação. Não execute mudanças em homologação ou produção. Ao final, apresente a matriz de achados e peça autorização para a etapa seguinte.

## Correção pontual, após aprovação

> Aplique Segurança ConectAI. Autorizo corrigir **somente SEC-001 e SEC-003** na **branch de homologação**. Faça o menor diff possível, valide com testes e informe efeitos colaterais e rollback. Não altere produção, permissões Protheus ou credenciais e não faça deploy.

## Verificação incremental e econômica

> Aplique Segurança ConectAI para analisar apenas os arquivos alterados entre **[commit-base]** e **[commit-atual]** e seus impactos de segurança. Liste riscos novos e testes indicados, sem chamar essa revisão de auditoria completa. Não altere arquivos.

## Validação pré-publicação

> Aplique Segurança ConectAI. Avalie a candidata à publicação em produção, SEM publicar. Verifique autenticação/autorização, segredos, integração Protheus SELECT, dependências, testes, rollback, monitoramento e riscos residuais. Emita parecer de liberação e pendências.

## Encerrar com relatório

> Aplique Segurança ConectAI e elabore o relatório conforme `referencias/modelo-relatorio.md`, diferenciando confirmado, potencial, corrigido e testado, pendente e não verificado. Não invente métricas ou execução de testes.
