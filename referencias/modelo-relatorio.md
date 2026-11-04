# Modelo de relatório: Segurança Cibernética

**Relatório nº:** [IDENTIFICADOR]  
**Data da análise:** [DATA]  
**Responsável técnico:** [NOME/FERRAMENTA]  
**Ambiente:** [HOMOLOGAÇÃO/PRODUÇÃO/REPOSITÓRIO]  
**Repositório/branch/versão:** [VALOR]  
**Escopo autorizado:** [DESCRIÇÃO]  
**Fases executadas:** [DIAGNÓSTICO / CORREÇÃO / TESTES / PÓS-CORREÇÃO]

## 1. Resumo executivo

- **Risco geral observado:** [Crítico / Alto / Médio / Baixo / Indeterminado]
- **Total de achados:** [N] (Críticos [N], Altos [N], Médios [N], Baixos [N])
- **Corrigidos e testados:** [N]
- **Pendentes / não verificáveis:** [N]
- **Decisão recomendada:** [Continuar em homologação / Apto para avaliação de publicação / Não recomendar publicação]
- **Limitação da avaliação:** [Acessos ou evidências indisponíveis; testes não executados]

## 2. Escopo e arquitetura observada

Descrever exclusivamente componentes inspecionados, fontes, fluxos, dados pessoais, autenticação, APIs, bancos, integrações e infraestrutura. Diferenciar fatos comprovados de informações não verificadas.

## 3. Matriz de achados

| ID | Área/componente | Severidade | Situação | Evidência mascarada | Impacto | Correção proposta/realizada | Reteste |
|---|---|---|---|---|---|---|---|
| SEC-001 | [Ex.: rota administrativa] | [Alto] | [Confirmado] | [Arquivo/linha ou teste sem segredo] | [Impacto] | [Correção mínima] | [Não executado] |

**Possíveis estados:** Confirmado; Potencial; Falso positivo; Não verificado; Pendente; Em implementação; Correção não validada; Corrigido e testado.

## 4. Mudanças implementadas (preencher somente se houve autorização)

| Arquivo/componente | Antes | Depois | Justificativa | Impacto | Reversão |
|---|---|---|---|---|---|
| [Caminho] | [Comportamento] | [Comportamento] | [Achado SEC-...] | [Risco] | [Procedimento] |

**Commits/branches:** [IDENTIFICADORES]

## 5. Testes e verificação

| Teste | Ambiente | Resultado | Evidência | Limitação |
|---|---|---|---|---|
| [Nome] | [Homologação] | [Passou/Falhou/Não executado] | [Resumo mascarado] | [Dependência] |

Relatar resultados negativos, falhas de regressão e verificações não realizadas. Nunca declarar testes inexistentes.

## 6. Particularidades condicionais: perfil ConectAI (quando aplicável)

- **Protheus:** conexão permanece exclusivamente SELECT? [Confirmado / Não confirmado] + evidência
- **Perfis e RBAC:** acesso segregado de administrador/gestor/colaborador? [Estado]
- **Dados RH/DP/SST:** controles de confidencialidade de arquivos, documentos e relatórios? [Estado]
- **Homologação e produção:** separação e aprovações verificadas? [Estado]
- **Segredos:** sem chaves em código/frontend/histórico? [Estado, sem imprimir os valores]
- **Regressão:** recursos existentes preservados? [Estado]

## 7. Riscos residuais e plano de ação

| Prioridade | Pendência | Responsável sugerido | Dependência | Critério de conclusão |
|---|---|---|---|---|
| P1 | [Pendência] | [Equipe] | [Acesso/aprovação] | [Teste] |

## 8. Parecer de publicação

**[ ] Recomendada para avaliação de publicação**  
**[ ] Não recomendada**  
**[ ] Indeterminada pela falta de testes/evidências**

**Justificativa objetiva:** [TEXTO]

**Atenção:** parecer técnico não é autorização de deploy; publicação depende de aprovação explícita do responsável.
