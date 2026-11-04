# Política de segurança e divulgação responsável

Obrigado por ajudar a melhorar a **Segurança Cibernética**. Esta skill é material de orientação e **não** um produto que garanta a ausência de vulnerabilidades.

## Como relatar problemas

Se detectar vulnerabilidade na própria skill, no workflow de CI, exemplos que exponham dados ou instruções capazes de provocar ações indevidas, **não abra uma issue pública com detalhes exploráveis, credenciais ou dados pessoais**.

Use a função **Report a vulnerability** / *Private vulnerability reporting* na aba **Security** do GitHub, quando habilitada pelo mantenedor. Caso não esteja disponível, solicite ao mantenedor um canal privado de comunicação sem anexar detalhes sensíveis em público. Não inventamos um e-mail de segurança.

Inclua somente informações estritamente necessárias: arquivo, versão/commit, cenário, impacto, passos não destrutivos para reproduzir e correção sugerida. Substitua dados reais por exemplos sintéticos.

## Escopo

- Arquivos de instruções, documentação, templates, scripts, regras de agentes e workflow do repositório.
- Problemas de autorização de agentes, *prompt injection*, vazamento de dados ou execução indevida orientada por esta skill.

**Fora do escopo:** testes de invasão em terceiros, sistemas de produção ou projetos que usam a skill. A licença MIT não concede autorização para testar sistemas alheios.

## Tratamento

O mantenedor deverá avaliar severidade, reproduzir em ambiente isolado, preparar correção revisável e publicar orientação segura quando possível. Não há SLA garantido; evite divulgação pública prematura.

## Versões suportadas

A versão principal em `main` é a referência corrente. Releases futuras devem registrar versão e alterações em `CHANGELOG.md`.
