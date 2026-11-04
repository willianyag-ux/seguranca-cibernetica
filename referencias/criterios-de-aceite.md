# Critérios de aceite e testes de segurança

## Condições para marcar um achado como corrigido

Um achado só pode receber status **Corrigido e testado** se:
1. A falha foi identificada com evidência reproduzível ou justificada.
2. O patch foi aplicado no ambiente **especificamente aprovado**.
3. O diff foi revisado e aponta exatamente quais arquivos/comportamentos mudaram.
4. O teste que falhava anteriormente passa depois do ajuste.
5. Um teste de regressão confirma que usuários autorizados continuam operando.
6. Não há nova exposição de dados/segredos; o comportamento observado foi documentado.

Caso falte item, usar **Em implementação**, **Correção não validada**, **Pendente** ou **Não verificado**.

## Matriz de testes recomendada (adaptar ao sistema real)

| Área | Teste positivo | Teste negativo | Evidência |
|---|---|---|---|
| Login | Credencial válida autentica | Credencial inválida não autentica; limitação de tentativas | Suite/local e logs mascarados |
| Sessões | Sessão válida funciona | Logout, expiração ou revogação impedem reutilização | Teste de integração |
| RBAC | Administrador autorizado acessa rota | Colaborador/gestor sem papel recebe 403 | Teste por perfil |
| IDOR/BOLA | Acesso ao próprio recurso é permitido | ID de terceiro não libera outro registro | Casos isolados de homologação |
| SQL | Consulta permitida e parametrizada funciona | Entrada malformada não altera comando SQL | Testes unitários e revisão de query |
| Protheus | `SELECT` autorizado é realizado | Nenhum comando com gravação permitido | Permissões de banco e auditoria do código |
| CORS | Origem aprovada recebe resposta apropriada | Origem desconhecida não recebe liberação | Teste de cabeçalhos |
| CSRF | Requisição legítima funciona | Mutation por cookie sem proteção falha | Teste conforme auth real |
| XSS | Conteúdo válido exibe corretamente | Payload não executa como código no navegador | Teste em homologação |
| Upload | Arquivo permitido e seguro é aceito | Excesso de tamanho/tipo inválido rejeitado | Suite de validação |
| HTTPS | Aplicação opera via HTTPS | Tráfego inseguro não expõe sessão | Verificação no proxy autorizado |
| Logs | Eventos relevantes rastreáveis | Senhas, tokens e documentos não aparecem | Evidência mascarada |

## Travas antes de qualquer produção

- [ ] Aprovação explícita e separada para o deploy.
- [ ] Branch/commit, versão e diff identificados.
- [ ] Plano de rollback testável e responsável definidos.
- [ ] Backup e recuperação adequados quando a mudança afetar armazenamento próprio.
- [ ] Retestes e regressão passam em ambiente autorizado.
- [ ] Variáveis de ambiente e segredos tratados sem vazamento.
- [ ] Conexão com Protheus continua **exclusivamente leitura (SELECT)**.
- [ ] Perfis e funcionalidades de RH, DP, SST, relatórios e aprovações essenciais verificados.
- [ ] Riscos residuais explicitados e aceitos por quem aprova.

## Proibições operacionais

Não testar invasão em terceiros, não executar ataque de negação de serviço, não expor credenciais em relatório, não alterar produção por consequência automática de um teste, não modificar permissões do Protheus, não desativar controles de segurança para fazer testes passarem.
