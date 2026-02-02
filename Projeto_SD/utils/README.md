Service Desk API

API REST desenvolvida em Python com Flask para gerenciamento de chamados técnicos.

Tecnologias Utilizadas

Python

Flask

MySQL

Requests

Estrutura do Projeto

service-desk-api/
├── app.py
├── database.py
├── models/
├── routes/
├── client/
├── requirements.txt
└── utils/

Como Executar o Projeto

1. Criar ambiente virtual

python -m venv venv

2. Ativar ambiente virtual

venv\\Scripts\\activate

3. Instalar dependências

pip install -r requirements.txt

4. Executar aplicação

python app.py

--> Funcionalidades

Usuários
- Criar usuário
- Listar usuários
- Buscar por ID
- Atualizar usuário
- Deletar usuário

Chamados
- Criar chamado
- Listar chamados
- Filtrar por prioridade
- Alterar status (Aberto / Em atendimento / Concluído)
- Deletar chamado

Atendimentos
- Criar atendimento
- Listar atendimentos por chamado

--> Como executar o projeto

Clone o repositório
bash
git clone https://github.com/seu-usuario/service-desk-api.git
cd service-desk-api