# 📝 ToDo List API 

![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API de gerenciamento de tarefas (**Tasks**) construída com **FastAPI** e **PostgreSQL (Neon)**. Permite criar, ler, atualizar e deletar tarefas, integrando facilmente com aplicações front-end como **React** ou **Next.js**.

A API está hospedada no **Render**.

---

## 🛠 Tecnologias

* **Back-end:** Python, FastAPI
* **Banco de dados:** PostgreSQL (Neon) com SQLAlchemy (ORM)
* **Hospedagem:** Render
* **Server runner:** Uvicorn

---

## 🚀 Rodando localmente

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente (`.env`):

```
DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<database>
```

4. Rode a aplicação:

```bash
uvicorn main:app --reload
```

A API estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📌 Endpoints

### 1️⃣ Listar todas as tasks

```http
GET /tasks
```

**Resposta:**

```json
[
  {
    "id": UUID,
    "title": "Exemplo de task",
    "description": "Descrição da task",
    "status": "pendente",
    "priority": "alta",
    "due_date": "2025-09-30T18:00:00+00:00"
  }
]
```

---

### 2️⃣ Obter uma task pelo ID

```http
GET /tasks/{id}
```

**Resposta:**

```json
{
  "id": UUID,
  "title": "Exemplo de task",
  "description": "Descrição da task",
  "status": "pendente",
  "priority": "alta",
  "due_date": "2025-09-30T18:00:00+00:00"
}
```

---

### 3️⃣ Criar uma nova task

```http
POST /tasks/
Content-Type: application/json
```

**Body:**

```json
{
  "title": "Nova task",
  "description": "Descrição da nova task",
  "status": "pendente",
  "priority": "alta",
  "due_date": "2025-10-01T12:00:00+00:00"
}
```

**Resposta:**

```json
{
  "id": UUID,
  "title": "Nova task",
  "description": "Descrição da nova task",
  "status": "pendente",
  "priority": "alta",
  "due_date": "2025-10-01T12:00:00+00:00"
}
```

---

### 4️⃣ Atualizar uma task

```http
PUT /tasks/{id}
Content-Type: application/json
```

**Body:**

```json
{
  "title": "Task atualizada",
  "description": "Descrição atualizada",
  "status": "concluída",
  "priority": "média",
  "due_date": "2025-10-02T12:00:00+00:00"
}
```

**Resposta:**

```json
{
  "id": UUID,
  "title": "Task atualizada",
  "description": "Descrição atualizada",
  "status": "concluída",
  "priority": "média",
  "due_date": "2025-10-02T12:00:00+00:00"
}
```

---

### 5️⃣ Deletar uma task

```http
DELETE /tasks/{id}
```

**Resposta:**

```json
{
  "message": "Task deletada com sucesso"
}
```

---

## 🏗 Arquitetura da Aplicação

```
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

## 📄 Licença

MIT License
