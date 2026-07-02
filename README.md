# AURA-OS

> **AI Unified Retrieval & Assistant Operating System**

AURA-OS is a production-oriented Personal AI Memory Operating System that continuously collects a user's digital activities (with explicit permission), converts them into semantic memory using embeddings, and enables intelligent search and conversation through Retrieval-Augmented Generation (RAG).

The goal of this project is to demonstrate end-to-end AI engineering skills across Android development, backend engineering, vector databases, LLM integration, MLOps, containerization, and cloud deployment.

> **Project Status:** 🚧 Under Active Development

---

# Vision

Build a scalable AI-powered memory platform that can securely collect personal digital events from an Android device and transform them into searchable semantic memory.

Users will eventually be able to ask questions such as:

* Show all Kubernetes-related notifications.
* Summarize yesterday's activities.
* When did Rahul message me?
* What meetings did I have last week?
* Show interview-related notes.
* Which reminders are still pending?

---

# Current Progress

## Sprint 1 – Foundation (Completed)

### Infrastructure

- ✅ Git repository initialized
- ✅ Production-ready project structure
- ✅ Docker Compose environment
- ✅ Docker-first development workflow

### Backend

- ✅ FastAPI application
- ✅ Modular backend architecture
- ✅ Configuration management using Pydantic Settings
- ✅ Centralized logging configuration
- ✅ Environment variable management

### Database

- ✅ PostgreSQL container
- ✅ SQLAlchemy 2.0 integration
- ✅ Database session management
- ✅ Declarative Base configuration
- ✅ User ORM model
- ✅ Alembic migration setup
- ✅ Initial database migration

### AI Infrastructure

- ✅ ChromaDB container
- ✅ Redis container
- ✅ MLflow container

### API

- ✅ Health endpoint
- ✅ Root endpoint
- ✅ OpenAPI / Swagger documentation

---

## Sprint 2 – Authentication (Upcoming)

- JWT Authentication
- User Registration
- Login
- Password Hashing
- Refresh Tokens
- Role-Based Access Control
---

# Project Structure

```text
AURA-OS/
│
├── android-app/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── middleware/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── workers/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
├── android-app/
├── embeddings/
├── ml/
├── vector-db/
├── infrastructure/
├── docs/
├── scripts/
├── .github/
│
├── docker-compose.yml
├── .env
├── README.md
└── LICENSE
```

---

# Technology Stack

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL
- Redis
- ChromaDB
- LangChain
- Sentence Transformers
- PyTorch
- MLflow
- Pydantic Settings
- JWT (Upcoming)

## Frontend (Planned)

* React
* TypeScript
* Tailwind CSS
* React Query

## Android (Planned)

* Kotlin
* MVVM
* Room Database
* Retrofit
* WorkManager
* NotificationListenerService

## Infrastructure

* Docker
* Docker Compose
* Kubernetes (Planned)
* GitHub Actions (Planned)
* AWS (Planned)

---

# Current Architecture

```text
                  Android App (Planned)
                           │
                     HTTPS / JWT
                           │
                    FastAPI Backend
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     PostgreSQL         ChromaDB         Redis
          │
       MLflow
```

## Backend Architecture

The backend follows **Clean Architecture** principles to ensure scalability, maintainability, and separation of concerns.

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

### Core Modules

| Module | Responsibility |
|---------|----------------|
| api | API endpoints |
| services | Business logic |
| repositories | Database operations |
| models | SQLAlchemy ORM models |
| schemas | Pydantic request/response models |
| db | Database engine & session |
| core | Configuration, logging, security |
| middleware | Request/response middleware |
| workers | Background processing |

---

# Running the Project

## Prerequisites

* Docker Desktop
* Git

# Database Migrations

AURA-OS uses **Alembic** for database version control.

## Generate a Migration

```bash
alembic revision --autogenerate -m "migration_name"
```

## Apply Migration

```bash
alembic upgrade head
```

## Roll Back

```bash
alembic downgrade -1
```

Database schema changes are tracked through version-controlled migrations to ensure consistent deployments across development, staging, and production environments.

# Current Database Schema

## Users

| Column | Type |
|----------|------|
| id | Integer |
| full_name | String |
| email | String |
| password_hash | String |
| is_active | Boolean |
| created_at | Timestamp |

Additional tables will be introduced in future sprints:

- Notifications
- SMS
- Calendar Events
- Notes
- Contacts
- Chat History
- AI Summaries


# Development Workflow

The project follows a Docker-first development workflow.

```text
VS Code
    │
    ▼
Docker Compose
    │
    ├── FastAPI
    ├── PostgreSQL
    ├── Redis
    ├── ChromaDB
    └── MLflow
```

Database schema changes are managed using Alembic migrations.

Backend development follows a layered architecture:

- API Layer
- Service Layer
- Repository Layer
- Database Layer

---

## Clone the Repository

```bash
git clone https://github.com/ParagWadhai/AURA-OS.git

cd AURA-OS
```

---

## Start All Services

```bash
docker compose up --build
```

---

## Running Containers

The following services are started:

| Service    | Port |
| ---------- | ---- |
| FastAPI    | 8000 |
| PostgreSQL | 5432 |
| Redis      | 6379 |
| ChromaDB   | 8001 |
| MLflow     | 5000 |

---

# Available Endpoints

## Root

```
GET /
```

Response

```json
{
    "message": "Welcome to AURA-OS"
}
```

---

## Health Check

```
GET /health
```

Response

```json
{
    "status": "healthy"
}
```

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

---

# Development Roadmap

## Sprint 1 ✅ Completed

- Project Structure
- Docker Infrastructure
- FastAPI Setup
- Configuration Management
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migrations
- User Database Model

---

## Sprint 2 🚧 Next

- Authentication
- JWT
- User Registration
- Login
- Refresh Tokens
- RBAC

---

## Sprint 3

- Android Notification Listener
- SMS Collector
- Calendar Collector
- Background Synchronization

---

## Sprint 4

- Embedding Pipeline
- ChromaDB Integration
- Semantic Search

---

## Sprint 5

- RAG Pipeline
- LLM Integration
- AI Chat

---

## Sprint 6

- React Dashboard
- Timeline
- Analytics
- Search Interface

---

## Sprint 7

- MLflow Tracking
- Kubernetes
- AWS Deployment

---

# Engineering Principles

This project follows production-oriented software engineering practices:

* Clean Architecture
* SOLID Principles
* Repository Pattern
* Service Layer
* Dependency Injection
* Async Programming
* Type Hints
* RESTful APIs
* Docker-first Development
* OpenAPI Documentation
* Modular Design

---

# Long-Term Features

The following features are planned for future development:

* Android notification synchronization
* SMS synchronization
* Calendar synchronization
* Notes synchronization
* Contact synchronization
* Semantic search
* Retrieval-Augmented Generation (RAG)
* AI chat assistant
* Daily AI summaries
* Weekly AI reports
* Vector embeddings
* Knowledge graph integration
* Gmail integration
* OCR support
* Voice note processing
* Screenshot indexing

---

# License

This project is licensed under the MIT License.

---

# Author

**Parag Wadhai**

AI/ML Engineer

This project is being developed as a production-grade AI Full Stack application to demonstrate modern software engineering, machine learning, LLM integration, and cloud deployment practices.
