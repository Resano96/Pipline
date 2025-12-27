# 🏗️ Housing Price Prediction MLOps Pipeline

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Ruff](https://img.shields.io/badge/Linter-Ruff-black.svg)](https://docs.astral.sh/ruff/)
[![Test](https://img.shields.io/badge/Tests-Pytest-yellow.svg)](https://docs.pytest.org/)
[![Manager](https://img.shields.io/badge/Manager-uv-purple.svg)](https://github.com/astral-sh/uv)

## 📋 Project Overview

This project implements a robust, production-ready MLOps pipeline for predicting housing prices. It is built with a focus on **Structural Integrity**, ensuring reliability, type safety, and reproducibility over algorithmic complexity.

The system consists of a Scikit-Learn inference engine served via a high-performance REST API (FastAPI), managed with modern Python tooling (`uv`).

### Key Features
* **Modern Stack**: Built with `uv` for lightning-fast dependency management and `Ruff` for strict code quality.
* **TDD First**: Developed using Test-Driven Development methodologies.
* **Type Safety**: Full use of Python Type Hints and Pydantic V2 for strict data validation (Schemas).
* **Reproducibility**: Automated training pipeline with artifact management (`.pkl`).
* **Resilience**: Synthetic data generation strategy implemented to bypass network constraints during development.

---

## 🏛️ Architecture

The project follows a modular structure separating source code, tests, and data exploration:

```text
housing_price_pipeline/
├── artifacts/           # serialized model storage (.pkl)
├── notebooks/           # Jupyter notebooks for EDA and prototyping
├── src/
│   └── housing/
│       ├── main.py      # FastAPI application & Lifecycle logic
│       ├── modeling.py  # Training pipeline & Data generation
│       └── schemas.py   # Pydantic contracts (Input/Output)
├── tests/               # Pytest suite (Integration & Smoke tests)
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


2. **Initialize Environment & Install Dependencies**
```bash
uv sync
```
---

## 🚀 Usage

### 1. Train the Model (The Machinery)

Before running the API, you must generate the model artifact. Due to network restrictions, this step currently generates synthetic data structurally identical to the California Housing dataset.

```bash
uv run python src/housing/modeling.py
```

*Output: Creates `artifacts/housing_model.pkl*`

### 2. Run the API (The Factory)

Start the production server locally:

```bash
uv run uvicorn src.housing.main:app --reload
```

### 3. Access Documentation

Once running, navigate to the auto-generated Swagger UI:
👉 **https://www.google.com/search?q=http://127.0.0.1:8000/docs**

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
