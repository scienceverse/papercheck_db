# papercheck-app

App wrapping the papercheck R library -> database, API, and web interface.

## Overview

Includes a Vue.js frontend wrapping the Papercheck R library, a PostgreSQL database and a modern Python API built with FastAPI, SQLAlchemy, and Alembic for managing research paper collections, extraction tools, and evaluation metrics.

## Features
- *Simple user-friendly web interface for quick paper validation using Papercheck  (TODO)*
- RESTful API for managing papers, datasets, extractors, and evaluations
- PostgreSQL database schema designed for research paper management
- *Admin interface to compare extraction testing results against ground truth data (TODO)*
- Close integration with dev-server (https://github.com/scienceverse/dev-server) ->
  - Using/managing custom Grobid/biblio-glutton
  - *Dashboards to monitor extraction/processing accuracy over time in Grafana (TODO)*

## Key DB Entities
- **Papers**: Core document entities with DOI, title, PDF handling, and processing status
- **Datasets**: Named collections of papers with many-to-many relationships
- **Ground Truths**: Ground truth extractions for papers
- **Extractors**: Configurable extraction tools and methods (Grobid)
- **Extracts**: Raw data from extraction
- **ExtractEvals**: Scores (f1, levenshtein, etc.) comparing extracts with ground truth

## Quick Start (API only, frontend TODO)

### Prerequisites

- Python 3.10+
- PostgreSQL database
- Poetry (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/scienceverse/papercheck_db.git
cd papercheck_db
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Run database migrations:
```bash
poetry run alembic upgrade head
```

5. Start the API server:
```bash
poetry run python main.py
```

The API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

## Environment Variables

Required environment variables (see `.env.example`):

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Secret key for cryptographic operations
- `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`: Database credentials
- `POSTGRES_HOST`, `POSTGRES_PORT`: Database connection details

## Database Schema

### Core Tables

- **papers**: Research documents with metadata and processing status
- **datasets**: Named collections linking to papers via junction table
- **ground_truths**: Ground truth annotations and extractions
- **extractors**: Tool definitions with configuration schemas
- **extracts**: Extraction results with confidence and validation data
- **extractevals**: Performance metrics and evaluation results

### Relationships

- Papers ↔ Datasets (many-to-many)
- Papers → Extracts (one-to-many)
- Papers → Ground Truths (one-to-many)
- Extractors → Extracts (one-to-many)
- Extractors ↔ Ground Truths → ExtractEvals (evaluation relationships)

## Development

### Code Quality

The project uses modern Python tooling:

- **Black**: Code formatting
- **Ruff**: Fast linting and import sorting
- **Poetry**: Dependency management
- **Pydantic**: Data validation and settings

### Database Migrations

Create a new migration:
```bash
poetry run alembic revision --autogenerate -m "Description"
```

Apply migrations:
```bash
poetry run alembic upgrade head
```

## API Documentation

Interactive API documentation is available at `/docs` when running the server. The API follows RESTful conventions with full CRUD operations for all entities.

## License

MIT License - see LICENSE file for details.
