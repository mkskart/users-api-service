# User Management API Microservice

A simple RESTful service for managing users, built with Flask, PostgreSQL, Docker, and Alembic migrations.

---

## Prerequisites

- Docker & Docker Compose installed  
- (Optional) Git & a GitHub account  

---

## Project Structure

```
user-api/
├── app/
│   ├── __init__.py       # Flask app factory, DB setup
│   ├── config.py         # Configuration via environment variables
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Marshmallow schemas for validation/serialization
│   └── routes.py         # API endpoints (CRUD)
├── migrations/           # Alembic migration scripts
├── tests/
│   ├── __init__.py
│   └── test_users.py     # Basic pytest tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py                # Entry point for Flask
└── README.md
```

---

## Setup & Run with Docker

From the project root:

1. **Build and start containers**  
   ```bash
   docker-compose up --build -d
   ```

2. **Verify both services are running**  
   ```bash
   docker-compose ps
   ```

---

## Database Migrations

After the containers are up and PostgreSQL is ready, run migrations inside the `web` container:

```bash
docker-compose exec web bash

# (Only the first time)
flask db init

# Generate and apply migrations
flask db migrate -m "Create users table"
flask db upgrade

exit
```

---

## Testing Endpoints

### Using curl in a UNIX shell (bash, WSL, Git Bash)

```bash
# Create
curl -i -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Kartheek","email":"kartheek@example.com"}'

# List all
curl http://localhost:5000/users

# Get one
curl http://localhost:5000/users/1

# Update
curl -i -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Kartheek Mukkavilli","email":"kartheek.mukkavilli@example.com"}'

# Delete
curl -i -X DELETE http://localhost:5000/users/1
```

### Using curl in Windows `cmd.exe`

```cmd
curl -i -X POST http://localhost:5000/users ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"Kartheek\",\"email\":\"kartheek@example.com\"}"

curl http://localhost:5000/users

curl http://localhost:5000/users/1

curl -i -X PUT http://localhost:5000/users/1 ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"Kartheek Mukkavilli\",\"email\":\"kartheek.mukkavilli@example.com\"}"

curl -i -X DELETE http://localhost:5000/users/1

```

> **GET** endpoints can also be tested directly in your browser by navigating to:
> ```
> http://localhost:5000/users
> http://localhost:5000/users/1
> ```

---

## Automated Tests

1. **Run pytest inside the container** (no host `pip` needed):
   ```bash
   docker-compose exec web pytest
   ```
2. You should see tests like:
   - `test_create_user` → passes with HTTP 201 and correct JSON body  
   - `test_get_user_not_found` → returns 404 with `{ "message": "User not found" }`

---

Happy coding!
