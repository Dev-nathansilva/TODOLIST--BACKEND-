# ToDo List API

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API de gerenciamento de tarefas (Tasks) construída com **FastAPI** e **PostgreSQL** (Neon). Esta API permite criar, ler, atualizar e deletar tarefas, suportando integração com aplicações front-end como React ou Next.js.

A API está hospedada no **Render**.

---

## Tecnologias

- **Back-end:** Python, FastAPI
- **Banco de dados:** PostgreSQL (Neon) - ORM(sqlachemy)
- **Hospedagem:** Render
- **Server runner:** Uvicorn

---

## Como rodar localmente

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>


2. Instale as dependências:

pip install -r requirements.txt


3. Configure variáveis de ambiente (exemplo .env):

DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<database>

4. Rode a aplicação:

uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000.



Endpoints
1. Listar todas as tasks

GET {URL}/tasks


Resposta:

[
    {
        "id": 1,
        "title": "Exemplo de task",
        "description": "Descrição da task",
        "status": "pendente",
        "priority": "alta",
        "due_date": "2025-09-30T18:00:00+00:00"
    }
]



2. Obter uma task pelo ID
GET {URL}/tasks/{id}


Resposta:

{
    "id": 1,
    "title": "Exemplo de task",
    "description": "Descrição da task",
    "status": "pendente",
    "priority": "alta",
    "due_date": "2025-09-30T18:00:00+00:00"
}

3. Criar uma nova task
POST {URL}/tasks/
Content-Type: application/json


Body:

{
    "title": "Nova task",
    "description": "Descrição da nova task",
    "status": "pendente",
    "priority": "alta",
    "due_date": "2025-10-01T12:00:00+00:00"
}


Resposta:

{
    "id": 2,
    "title": "Nova task",
    "description": "Descrição da nova task",
    "status": "pendente",
    "priority": "alta",
    "due_date": "2025-10-01T12:00:00+00:00"
}

4. Atualizar uma task
PUT {URL}/tasks/{id}
Content-Type: application/json


Body:

{
    "title": "Task atualizada",
    "description": "Descrição atualizada",
    "status": "concluída",
    "priority": "média",
    "due_date": "2025-10-02T12:00:00+00:00"
}


Resposta:

{
    "id": 2,
    "title": "Task atualizada",
    "description": "Descrição atualizada",
    "status": "concluída",
    "priority": "média",
    "due_date": "2025-10-02T12:00:00+00:00"
}

5. Deletar uma task
DELETE {URL}/tasks/{id}


Resposta:

{
    "message": "Task deletada com sucesso"
}




Arquitetura da Aplicação
    +----------------+
    |   Frontend /   |
    |   Cliente      |
    | (React/Next)   |
    +-------+--------+
            |
            | HTTP Request (JSON)
            v
    +----------------+
    |     main.py    |
    | (FastAPI App)  |
    +-------+--------+
            |
            | Depends(get_db)
            v
    +----------------+
    |   database.py  |
    | - SessionLocal |
    | - engine       |
    +-------+--------+
            |
            v
    +----------------+
    |     crud.py    |
    | (Funções CRUD) |
    +-------+--------+
            |
            +-------+--------+
                    |
                    v
    +----------------+   +----------------+
    |  models.py     |   |  models.py     |
    |  Task Model    |   |  Category Model|
    +----------------+   +----------------+
            |
            v
    +----------------+
    | PostgreSQL DB  |
    |    (Neon)      |
    +----------------+
```
