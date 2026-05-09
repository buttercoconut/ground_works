# Ground Works Project

## Overview

This repository contains a minimal full‑stack example for a **Ground Works** data collection system.  The backend is a FastAPI application that exposes CRUD endpoints for *boring* records and a placeholder for *task* management.  The frontend is a Vue 3 + Vite SPA that consumes the API and displays boring data.

The goal of this template is to provide a working skeleton that can be extended with:

* **Machine‑learning** models for soil‑layer classification.
* **Data‑quality** checks and validation.
* **Deployment** scripts (Docker, CI/CD, etc.).

Feel free to copy the directory structure and adapt the code to your own needs.

---

## Directory layout

```
project/
├─ backend/
│  ├─ api/
│  │  ├─ boring.py
│  │  └─ task.py
│  ├─ models/
│  │  ├─ boring.py
│  │  └─ task.py
│  ├─ services/
│  │  ├─ boring_service.py
│  │  └─ task_service.py
│  └─ main.py
├─ frontend/
│  ├─ components/
│  │  ├─ BoringList.vue
│  │  └─ BoringView.vue
│  ├─ views/
│  │  └─ BoringView.vue
│  └─ App.vue
└─ README.md
```

## Running the backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Running the frontend

```bash
cd frontend
npm install
npm run dev
```

The Vue app will be served at `http://localhost:5173`.

## Extending the project

* **Add ML logic** – create a new service in `backend/services/ml_service.py` and expose endpoints in `api/ml.py`.
* **Add database migrations** – use Alembic.
* **Add authentication** – integrate OAuth2 or JWT.

---

Happy coding!
