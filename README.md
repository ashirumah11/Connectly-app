# Connectly

Connectly is an original Instagram-inspired social networking web application built with Django REST Framework and React TypeScript.

## Technology

- Backend: Python, Django, Django REST Framework, Simple JWT, drf-spectacular
- Database: PostgreSQL 16
- Frontend: React, TypeScript, Vite, Tailwind CSS, TanStack Query
- Infrastructure: Docker Compose, Redis

## Local setup

### 1. Backend environment

```powershell
cd C:\Users\amond\OneDrive\Desktop\Connectly-app
.\.venv\Scripts\python.exe -m pip install -r backend\requirements.txt
copy .env.example .env
```

Start PostgreSQL and Redis with Docker Desktop:

```powershell
docker compose up -d postgres redis
```

Run migrations and start Django:

```powershell
cd backend
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py runserver
```

API health: `http://localhost:8000/api/v1/health/`  
Swagger: `http://localhost:8000/api/v1/docs/`

### 2. Frontend

```powershell
cd C:\Users\amond\OneDrive\Desktop\Connectly-app\frontend
copy .env.example .env.local
npm.cmd install
npm.cmd run dev
```

Frontend: `http://localhost:5173`

## Milestone status

Phase 1 foundation and custom `User` model are initialized. PostgreSQL database startup is required before migrations can be applied and database-backed tests can run.
