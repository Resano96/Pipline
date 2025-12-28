
# 🏗️ Housing Price Prediction MLOps Pipeline

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/GitHub%20Actions-Active-yellow.svg)](https://github.com/features/actions)
[![Manager](https://img.shields.io/badge/Manager-uv-purple.svg)](https://github.com/astral-sh/uv)

## 📋 Project Overview

This project implements a robust, production-ready MLOps pipeline for predicting housing prices. It is built with a focus on **Structural Integrity**, ensuring reliability, type safety, and reproducibility over algorithmic complexity.

The system consists of a Scikit-Learn inference engine served via a high-performance REST API (FastAPI), containerized with **Docker**, and validated via a **CI/CD pipeline**.

### Key Features
* **Modern Stack**: Built with `uv` for lightning-fast dependency management and `Ruff` for strict code quality.
* **TDD First**: Developed using Test-Driven Development methodologies.
* **Containerization**: Fully dockerized application using Multi-Stage Builds for optimized image size.
* **CI/CD**: Automated testing pipeline via GitHub Actions.
* **Resilience**: Synthetic data generation strategy implemented to bypass network constraints during development.

---

## 🏛️ Architecture

The project follows a modular structure separating source code, tests, ops config, and data exploration:

```text
housing_price_pipeline/
├── .github/
│   └── workflows/       # CI/CD Pipeline configuration (GitHub Actions)
├── artifacts/           # Serialized model storage (.pkl)
├── notebooks/           # Jupyter notebooks for EDA and prototyping
├── src/
│   └── housing/
│       ├── main.py      # FastAPI application & Lifecycle logic
│       ├── modeling.py  # Training pipeline & Data generation
│       └── schemas.py   # Pydantic contracts (Input/Output)
├── tests/               # Pytest suite (Integration & Smoke tests)
├── .dockerignore        # Docker build exclusion rules
├── Dockerfile           # Multi-stage container definition
├── pyproject.toml       # Project configuration & Dependencies
└── uv.lock              # Exact dependency versioning

```

---

## 🛠️ Setup & Installation

This project uses **[uv](https://github.com/astral-sh/uv)** for dependency management.

1. **Clone the repository**
```bash
git clone <repository-url>
cd housing_price_pipeline
```


2. **Initialize Environment**
```bash
uv sync
```



---

## 🐳 Docker (Production)

The application is containerized to ensure "Build once, run anywhere" capability.

### 1. Build the Image

We use a multi-stage build process to keep the final image lightweight.

```bash
docker build -t housing-api:v1 .
```

### 2. Run the Container

Map the container's port 80 to your local machine (e.g., port 8000).

```bash
docker run -p 8000:80 housing-api:v1
```

Once running, the API is available at: `http://localhost:8000/docs`

---

## 🚀 Local Usage (Without Docker)

### 1. Train the Model (The Machinery)

Before running the API, you must generate the model artifact.

```bash
uv run python src/housing/modeling.py
```

*Output: Creates `artifacts/housing_model.pkl*`

### 2. Run the API (The Factory)

Start the development server locally:

```bash
uv run uvicorn src.housing.main:app --reload
```

---

## 🤖 CI/CD (Automation)

This project uses **GitHub Actions** for Continuous Integration.
The pipeline is defined in `.github/workflows/ci.yml` and triggers automatically on `push` or `pull_request` to the main branch.

**Pipeline Steps:**

1. **Setup**: Installs `uv` and Python 3.13.
2. **Training**: Executes the training script to verify model generation logic.
3. **Testing**: Runs the full `pytest` suite to validate API endpoints and schemas.

---

## 🧪 Testing (Quality Control)

Rigorous testing is applied to both the API endpoints and the training pipeline logic.

```bash
uv run pytest -v
```

**Test Scope:**

* `test_health_check`: Verifies API availability and versioning.
* `test_prediction`: Validates inference logic and data contracts.
* `test_training_pipeline`: Smoke test for the model generation script.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/health` | Health check and version info. |
| `POST` | `/predict` | Predicts house price based on 8 features. |

### Example Request (POST /predict)

```json
{
  "MedInc": 3.5,
  "HouseAge": 30.0,
  "AveRooms": 6.0,
  "AveBedrms": 1.0,
  "Population": 800.0,
  "AveOccup": 3.0,
  "Latitude": 34.0,
  "Longitude": -118.0
}

```

---

## 📜 License

Project developed for educational and portfolio purposes.
