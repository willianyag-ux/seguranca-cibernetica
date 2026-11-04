# Publicação futura no GitHub

Este pacote está preparado para Git, mas **ainda não foi enviado ao GitHub**.

## Antes de publicar

1. Preferir **repositório privado** inicialmente. Um projeto auditado pode conter detalhes internos de arquitetura e regras de negócio, ainda que esta skill não contenha senhas.
2. Inspecionar `SKILL.md`, `README.md`, `referencias/`, `prompts/` e o histórico local para confirmar ausência de nomes de servidores privados, IPs, credenciais, dados pessoais e informações restritas.
3. Não copiar `.env`, backups, bancos, certificados, capturas de tela com colaboradores ou relatórios reais de vulnerabilidade.
4. Se houver uma falha confirmada, manter provas e dados de reprodução em canal privado, não em issues públicas.
5. Decidir se a publicação será privada ou pública e qual licença (se houver) deseja conceder.

## Criar repositório privado localmente e enviar ao GitHub

Crie no GitHub um repositório **privado** vazio, por exemplo `seguranca-cibernetica`. Na máquina onde extraiu o pacote, execute:

```bash
cd Seguranca-Cibernetica-Universal
git init
git add .
git commit -m "feat: skill universal Segurança Cibernética"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/seguranca-cibernetica.git
git push -u origin main
```

Substitua `SEU_USUARIO` e o nome do repositório. Configure a autenticação do GitHub com um método aprovado pela sua organização. Os comandos **não foram executados** e exigem sua decisão.

## Como usar a skill em outro repositório

Se quiser que um agente de programação use o protocolo automaticamente dentro do **projeto ConectAI**, copie `SKILL.md`, `referencias/` e os arquivos de integração adequados para a raiz do projeto. Faça merge de `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` ou `.github/copilot-instructions.md` caso já existam, em vez de sobrescrever as regras.

Manter a skill em repositório separado é útil para versioná-la sem divulgar o código de produção.

## Versionamento sugerido

- `1.0.x`: revisão de texto/checklist sem mudança de fluxo.
- `1.x.0`: controles, novas integrações ou relatórios.
- `2.0.0`: alteração de regras de aprovação ou fluxo de execução.

## Verificações de integridade

```bash
python scripts/verificar_estrutura.py
```

A automação do GitHub verifica a consistência do pacote, **não avalia a segurança real do ConectAI**.
