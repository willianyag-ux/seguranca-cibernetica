# Checklist técnico de auditoria do ConectAI

Preencher cada controle com: **Conforme / Não conforme / Não aplicável / Não verificado**, evidência mascarada, componente afetado e risco. Priorizar pontos efetivamente expostos. Esta lista não substitui a leitura das referências OWASP originais.

## 1. Inventário, superfícies e trust boundaries
- [ ] Confirmar ambiente (homologação/produção), versão, branch, artefatos, serviços, reverse proxy e tecnologias reais.
- [ ] Mapear rotas HTTP, APIs internas/externas, WebSocket, tarefas agendadas, arquivos estáticos, armazenamento e endpoints administrativos.
- [ ] Identificar origem dos dados de RH/DP/SST e fluxos com Protheus, usuários, bancos próprios e integrações externas.
- [ ] Identificar dados pessoais/sensíveis, fluxo entre papéis, exportações, relatórios, logs, backups e tempo de retenção.
- [ ] Conferir documentação de ameaças e superfícies de ataque de terceiros, sem assumir que redes internas são confiáveis.

## 2. Identidade, senha e sessão
- [ ] Senhas com Argon2id ou bcrypt com configuração defensável; nada reversível ou texto puro.
- [ ] Rate limit adaptado a login, reset, convites e APIs sensíveis; evitar bloqueio permanente/negação de serviço por usuário.
- [ ] Sessões/tokens com entropia, expiração, revogação, rotação quando aplicável e invalidação após alterações sensíveis.
- [ ] Cookies `HttpOnly`, `Secure`, `SameSite` apropriado; domínio/caminho restritos; `trust proxy` coerente.
- [ ] Login, logout, recuperação e troca de senha sem enumeração indevida de usuários.
- [ ] Reset de senha com token aleatório, uso único, expiração, armazenamento seguro e invalidação após consumo.
- [ ] MFA para administradores, se viável e exigido pelo risco.
- [ ] Proteção contra fixation de sessão e uso indevido de refresh tokens.

## 3. Autorização, papéis e isolamento de dados
- [ ] Todas as rotas protegidas por autorização no **servidor**, não por menu oculto no frontend.
- [ ] Política explícita de acesso por papel: administrador, gestor, colaborador e serviços.
- [ ] IDOR/BOLA: usuário não acessa/edita registros de outro alterando ID, matrícula, filial, query ou corpo.
- [ ] Gestores acessam apenas equipes e dados autorizados; endpoints de listas e exportações filtram no backend.
- [ ] Alterações críticas, aprovações e decisões administrativas exigem autorização verificada na operação.
- [ ] Perfis administrativos seguem menor privilégio; contas de serviço não recebem privilégios de usuário humano.
- [ ] Dados sensíveis de SST/atestados/CID têm controle de acesso específico, auditável e justificado.

## 4. Entradas, browser e API
- [ ] Validar no servidor tipo, tamanho, formato, limites, enums e combinações de campos.
- [ ] Usar parâmetros SQL; evitar concatenação insegura inclusive em filtros, ordenação e paginação.
- [ ] Fazer codificação contextual de saída (HTML, atributo, URL, JS); sanitizar HTML se houver rich text.
- [ ] Configurar CSP progressivamente e avaliar `unsafe-inline`/`unsafe-eval`, sem quebrar o app.
- [ ] CSRF: proteger mutações quando autenticadas por cookie; avaliar defesa real para arquitetura usada.
- [ ] CORS com lista exata de origens, métodos e cabeçalhos; `credentials` somente quando necessário.
- [ ] Evitar SSRF em URLs fornecidas por usuários, fetch/proxies e callbacks; validar destinos e rede.
- [ ] Evitar open redirect, path traversal, injeção de comando e exposição de stack traces.
- [ ] Se houver pagamentos, validar valor, beneficiário, operação e idempotência no backend; webhooks autenticados.

## 5. Upload e download
- [ ] Aplicar limite de tamanho, quantidade e tipo real do arquivo; não confiar só em extensão/MIME declarado.
- [ ] Renomear arquivos com identificador seguro e armazenar fora de diretórios executáveis/publicados.
- [ ] Tratar antivírus/varredura conforme risco e mecanismo de armazenamento.
- [ ] Prevenir traversal, acesso cruzado, execução arbitrária e vazamento por links estáticos.
- [ ] Validar permissão para cada download, inclusive documentos médicos, folhas e anexos de colaborador.

## 6. Banco e integração Protheus
- [ ] Confirmar credencial de Protheus com privilégios **somente leitura**, restrita a objetos estritamente necessários.
- [ ] Verificar que handlers não conseguem operar SQL não permitido. Não assumir que filtro lexical `SELECT` por si só garante segurança.
- [ ] Queries parametrizadas em todo dado controlado pelo usuário; whitelist para nomes de coluna/ordenação.
- [ ] Conexão criptografada e gestão segura de segredos quando suportado pelo ambiente.
- [ ] Pools, timeouts, limites de retorno e índices coerentes com desempenho e proteção contra DoS.
- [ ] Banco próprio do ConectAI (se existir) separado do Protheus e com privilégio mínimo.
- [ ] Backups, restauração testada, credenciais, retenção e rastreabilidade sem cópias de dados reais em ambientes inseguros.
- [ ] Proibido qualquer teste que altere dados reais do Protheus, inclusive por stored procedures, triggers indiretos ou consultas com efeito colateral.

## 7. Infraestrutura, configuração e supply chain
- [ ] HTTPS real e redirecionamento apropriado; TLS/certificados; HSTS somente após validação de domínio e HTTPS.
- [ ] `helmet`/headers equivalentes: CSP, nosniff, políticas de referência, frame protections quando aplicáveis.
- [ ] Erros sem debug/stack trace para clientes em produção; logs internos com controle de acesso.
- [ ] `.env` fora de controle de versão; permissões mínimas; variáveis obrigatórias validadas no startup.
- [ ] Segredos no frontend, bundles, mapas de origem, arquivos públicos e histórico do Git verificados sem imprimir valores.
- [ ] Se segredos estiverem comprometidos: plano aprovado de rotação, propagação e invalidação.
- [ ] `npm audit` ou SCA equivalente, versões e lockfile; priorizar vulnerabilidades **alcançáveis**.
- [ ] Revisão de dependências e pacotes não usados; mudança de versão somente com regressão controlada.
- [ ] Serviços, portas e CORS expostos, proxies, firewall, permissões do SO e execução sem superusuário.
- [ ] Git/CI/CD: permissões de deploy, integridade de artefatos, segredos e restrições de branches.

## 8. Observabilidade, privacidade e resposta
- [ ] Logar falhas e sucessos relevantes de autenticação sem guardar senha ou token.
- [ ] Logar alterações administrativas, permissões e acessos a recursos sensíveis sem conteúdo de documentos.
- [ ] Alertas proporcionais a risco; relógios sincronizados, retenção e política de acesso aos logs.
- [ ] Proteção contra log injection, vazamento de payloads e logs excessivos de dados pessoais.
- [ ] Procedimento para incidente: triagem, contenção, preservação de evidências, recuperação e comunicação pertinente.
- [ ] Revisão de direitos de acesso e retenção de dados compatíveis com requisitos legais/contratuais aplicáveis.

## 9. Evidências e classificação

Para cada achado: identifique arquivo/rota/configuração, comportamento observado, pré-condição, impacto, probabilidade, exposição, severidade e um teste de reteste não destrutivo.

- **Crítico**: comprometimento relevante e imediato provável, como acesso administrativo sem autorização ou vazamento massivo confirmado.
- **Alto**: exploração plausível com impacto expressivo sobre dados, contas ou disponibilidade.
- **Médio**: proteção insuficiente ou exploração dependente de outras condições.
- **Baixo**: melhoria de defesa em profundidade ou exposição limitada.

Não infira gravidade apenas pelo nome de uma biblioteca ou alerta; verifique contexto, alcance e mitigadores. Registre explicitamente falso positivo e não verificado.

## Referências atualizáveis
- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OWASP ASVS 5.0.0: https://asvs.owasp.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
