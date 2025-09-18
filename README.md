# papercheck_db

Config and API for papercheck database -> datasets, papers, extractors, extractor evaluations

## Overview

A modern Python API built with FastAPI, SQLAlchemy, and Alembic for managing research paper collections, extraction tools, and evaluation metrics.

## Features

- **Papers**: Core document entities with DOI, title, PDF handling, and processing status
- **Datasets**: Named collections of papers with many-to-many relationships
- **Canons**: Ground truth extractions for papers with structured annotation data
- **Extractors**: Configurable extraction tools and methods
- **Extracts**: Results from extraction processes with validation and metrics
- **ExtractorEvals**: Performance evaluations comparing extracts with ground truth

## Quick Start

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
- **canons**: Ground truth annotations and extractions
- **extractors**: Tool definitions with configuration schemas
- **extracts**: Extraction results with confidence and validation data
- **extractorevals**: Performance metrics and evaluation results

### Relationships

- Papers ↔ Datasets (many-to-many)
- Papers → Extracts (one-to-many)
- Papers → Canons (one-to-many)
- Extractors → Extracts (one-to-many)
- Extractors ↔ Canons → ExtractorEvals (evaluation relationships)

## Development

### Code Quality

The project uses modern Python tooling:

- **Black**: Code formatting
- **Ruff**: Fast linting and import sorting
- **Poetry**: Dependency management
- **Pydantic**: Data validation and settings

### Testing

```bash
poetry run pytest
```

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
