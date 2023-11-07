# TaskTodo.Py

## Descrição

TaskTodo.Py é uma API de lista de tarefas (To-Do List) construída com Flask e SQLAlchemy. Esta API permite aos usuários criar, listar, atualizar e deletar tarefas, funcionando como um backend para aplicações de gerenciamento de tarefas.

## Funcionalidades

- **Criar Tarefas**: Adicione novas tarefas à lista.
- **Listar Tarefas**: Veja todas as suas tarefas atuais.
- **Atualizar Tarefas**: Atualize os detalhes de uma tarefa existente.
- **Deletar Tarefas**: Remova tarefas que não são mais necessárias.

## Como Configurar

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

```bash
# Clone o repositório
git clone https://link-para-o-repositorio

# Entre no diretório do projeto
cd TaskTodo.Py

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
.\venv\Scripts\Activate
# Unix ou MacOS
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
python main.py
```

### Endpoints da API
A API fornece os seguintes endpoints:

* - POST /tasks: Cria uma nova tarefa.
* - Parâmetros esperados no corpo da requisição: title, description.

* - GET /tasks: Lista todas as tarefas.

* - GET /tasks/<id>: Recupera os detalhes de uma tarefa específica.

* - PUT /tasks/<id>: Atualiza uma tarefa existente.
* - Parâmetros esperados no corpo da requisição: title, description, is_complete.

* - DELETE /tasks/<id>: Deleta uma tarefa.
