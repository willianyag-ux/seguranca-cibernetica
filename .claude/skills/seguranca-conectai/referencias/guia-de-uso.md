# Guia de uso multiplataforma: Segurança ConectAI

## Em qualquer IA, mesmo sem recurso de Skills

1. Anexe ou cole `PROMPT_UNIVERSAL.md` no chat.
2. Disponibilize o repositório/código somente em um ambiente que você controla, com autorização e sem segredos.
3. Solicite **"Execute apenas o diagnóstico de segurança, em modo somente leitura"**.
4. Analise evidências, plano e dependências. Autorize explicitamente alterações em homologação, se desejar.

Sem acesso ao código, a IA fornece apenas uma análise documental e não pode atestar controles reais.

## ChatGPT

Use `PROMPT_UNIVERSAL.md` como instrução/anexo e dê acesso ao projeto através dos mecanismos disponíveis. O conteúdo é portável, mas o ChatGPT não instala automaticamente a skill do Claude.

## Claude (navegador)

Empacote somente o conteúdo da pasta `.claude/skills/seguranca-conectai/` em ZIP, mantendo `SKILL.md` na raiz interna da pasta da skill conforme a interface de importação. Importe pela função de Skills, quando disponível. Você também pode enviar `PROMPT_UNIVERSAL.md` ao chat diretamente.

## Claude Code

Dentro do projeto, mantenha `CLAUDE.md` na raiz e `.claude/skills/seguranca-conectai/SKILL.md` com seus arquivos `referencias`. Peça para usar `/seguranca-conectai` ou mencione o nome da skill.

## Codex

Mantenha `AGENTS.md`, `SKILL.md` e `referencias/` no diretório do projeto. O Codex utiliza `AGENTS.md` para localizar orientações; peça que siga o protocolo ao fazer tarefas de segurança.

## Gemini CLI

Use `GEMINI.md`, `SKILL.md` e `referencias/` na raiz. Peça que a ferramenta abra `SKILL.md` para auditorias.

## Cursor

Copie `.cursor/rules/seguranca-conectai.mdc`, `SKILL.md` e `referencias/` para o projeto. A regra está configurada para uso por relevância, não universalmente ativa.

## GitHub Copilot

Inclua `.github/copilot-instructions.md`, `SKILL.md` e `referencias/` no repositório. Se já houver instruções, mescle as regras sem sobrescrever conteúdo existente.

## Prompt de ativação universal

> Leia e siga as instruções da Segurança ConectAI. Inicie em modo diagnóstico, somente leitura. Examine o que estiver realmente acessível, registre o não verificado, priorize achados por risco e entregue plano de correção. Não modifique arquivos ou produção sem aprovação específica.

## Observação

A skill não concede acesso, não substitui uma avaliação profissional de segurança e não justifica testes invasivos sem autorização específica do proprietário dos sistemas.
