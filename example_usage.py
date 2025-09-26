#!/usr/bin/env python3
"""Example script showing how to use the papercheck_db models and schemas."""

import os
from datetime import datetime
from pprint import pprint
from pathlib import Path

# Load environment variables from .env file if it exists
def load_env_file():
    """Load environment variables from .env file."""
    env_file = Path(__file__).parent / '.env'
    if env_file.exists():
        print(f"Loading environment variables from {env_file}")
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    else:
        print(f"No .env file found at {env_file}. Using default environment variables.")
        # Set default environment variables for demo
        os.environ.update({
            'DATABASE_URL': 'postgresql://username:password@localhost:5432/papercheck_dev',
            'POSTGRES_USER': 'username',
            'POSTGRES_PASSWORD': 'password', 
            'POSTGRES_DB': 'papercheck_db',
            'POSTGRES_HOST': 'localhost',
            'POSTGRES_PORT': '5432',
            'ENVIRONMENT': 'development'
        })

# Load environment variables
load_env_file()

def demo_schemas():
    """Demonstrate how to use Pydantic schemas."""
    print("🔧 Demonstrating Pydantic Schemas\n")
    
    from papercheck_db.schemas import (
        PaperCreate, Paper,
        DatasetCreate, Dataset,
        ExtractorCreate, Extractor,
        GroundTruthCreate, GroundTruth,
        ExtractCreate, Extract,
        ExtractEvalCreate, ExtractEval
    )
    
    # Create a paper (using current schema fields)
    paper_data = PaperCreate(
        pdf_path="/papers/smith_2024.pdf",
        pdf_url="https://example.com/papers/smith_2024.pdf",
        pdf_hash="abc123def456789",  # SHA-256 hash would be longer in practice
        pdf_actual_start_page=1,
        pdf_actual_last_page=15,
        source="arXiv"
    )
    print("Paper creation schema:")
    pprint(paper_data.model_dump())
    print()
    
    # Create a dataset
    dataset_data = DatasetCreate(
        name="AI Research Papers 2024",
        description="Collection of AI research papers from 2024",
        version="1.0",
        source="arXiv",
        license="CC BY 4.0",
        folder_path="/datasets/ai_papers_2024"
    )
    print("Dataset creation schema:")
    pprint(dataset_data.model_dump())
    print()
    
    # Create an extractor
    extractor_data = ExtractorCreate(
        name="GPT-4 Citation Extractor",
        description="Uses GPT-4 to extract citations from research papers",
        version="1.2.0",
        extractor_type="llm",
        implementation="python",
        config_schema={
            "model": {"type": "string", "default": "gpt-4"},
            "temperature": {"type": "number", "default": 0.1},
            "max_tokens": {"type": "integer", "default": 1000}
        },
        default_config={
            "model": "gpt-4",
            "temperature": 0.1,
            "max_tokens": 1000
        },
        is_active=True,
        author="Research Team",
        contact_email="team@university.edu",
        documentation_url="https://example.com/docs/gpt4-extractor",
        repository_url="https://github.com/example/gpt4-extractor",
        supported_formats="PDF, HTML",
        performance_notes="Optimized for academic papers"
    )
    print("Extractor creation schema:")
    pprint(extractor_data.model_dump())
    print()
    
    # Create a ground truth (requires paper_id, so this is just showing structure)
    print("Ground Truth creation schema (example structure):")
    ground_truth_fields = {
        "paper_id": 1,  # Would be actual paper ID
        "title": "A Study of Machine Learning in Research Paper Analysis",
        "doi": "10.1000/182",
        "authors": {"authors": ["Smith, J.", "Doe, A.", "Johnson, M."]},
        "refs": {"references": ["Ref 1", "Ref 2", "Ref 3"]},
        "xrefs": {"cross_refs": ["XRef 1", "XRef 2"]},
        "abstract": "This paper investigates the application of ML techniques...",
        "keywords": ["machine learning", "research", "analysis"]
    }
    pprint(ground_truth_fields)
    print()
    
    # Create an extract (requires paper_id and extractor_id)
    print("Extract creation schema (example structure):")
    extract_fields = {
        "paper_id": 1,  # Would be actual paper ID
        "extractor_id": 1,  # Would be actual extractor ID
        "extraction_date": "2024-01-15",
        "extracted_title": "A Study of Machine Learning in Research Paper Analysis",
        "extracted_doi": "10.1000/182",
        "extracted_authors": {"authors": ["Smith, J.", "Doe, A.", "Johnson, M."]},
        "extracted_refs": {"references": ["Ref 1", "Ref 2", "Ref 3"]},
        "extracted_xrefs": {"cross_refs": ["XRef 1", "XRef 2"]},
        "extracted_abstract": "This paper investigates the application of ML techniques...",
        "extracted_keywords": ["machine learning", "research", "analysis"]
    }
    pprint(extract_fields)
    print()

def demo_model_relationships():
    """Demonstrate model relationships."""
    print("🔗 Demonstrating Model Relationships\n")
    
    from papercheck_db.models import Paper, Dataset, Extractor, Extract, GroundTruth, ExtractEval
    
    print("Model relationships:")
    print("- Papers ↔ Datasets (many-to-many via dataset_paper_association)")
    print("- Papers → Extracts (one-to-many)")
    print("- Papers → GroundTruths (one-to-many)")
    print("- Extractors → Extracts (one-to-many)")
    print("- Extracts + GroundTruths → ExtractEvals (evaluation)")
    print()
    
    print("Available models and their table names:")
    print(f"- Paper: {Paper.__tablename__}")
    print(f"- Dataset: {Dataset.__tablename__}")
    print(f"- Extractor: {Extractor.__tablename__}")
    print(f"- Extract: {Extract.__tablename__}")
    print(f"- GroundTruth: {GroundTruth.__tablename__}")
    print(f"- ExtractEval: {ExtractEval.__tablename__}")
    print()
    
    print("Schema types available for each model:")
    print("- Create: For creating new records")
    print("- Read: For reading records with relationships")
    print("- Update: For updating existing records")
    print("- Delete: For deletion operations")
    print("- Summary: For lightweight record representations")
    print()

def demo_configuration():
    """Demonstrate configuration management."""
    print("⚙️  Demonstrating Configuration\n")
    
    from papercheck_db.core.config import settings
    
    print("Configuration settings:")
    print(f"- Environment: {settings.environment}")
    print(f"- Database URL: {settings.database_url}")
    print(f"- Is development: {settings.is_development}")
    print(f"- Is production: {settings.is_production}")
    print()

def demo_environment():
    """Show current environment configuration."""
    print("🌍 Environment Configuration\n")
    
    env_vars = [
        'DATABASE_URL', 'POSTGRES_USER', 'POSTGRES_PASSWORD', 
        'POSTGRES_DB', 'POSTGRES_HOST', 'POSTGRES_PORT', 'ENVIRONMENT'
    ]
    
    print("Current environment variables:")
    for var in env_vars:
        value = os.environ.get(var, 'Not set')
        # Mask sensitive information
        if 'PASSWORD' in var or 'SECRET' in var:
            value = '****' if value != 'Not set' else 'Not set'
        print(f"  {var}: {value}")
    print()

def main():
    """Run all demonstrations."""
    print("📋 PaperCheck DB - Usage Examples")
    print("=" * 50)
    print()
    
    try:
        demo_environment()
        demo_configuration()
        demo_schemas()
        demo_model_relationships()
        
        print("✅ All demonstrations completed successfully!")
        print("\nNext steps:")
        print("1. Set up your PostgreSQL database")
        print("2. Copy .env.example to .env and configure your settings")
        print("3. Install dependencies: poetry install")
        print("4. Run database migrations: poetry run alembic upgrade head")
        print("5. Start the API server: poetry run python main.py")
        print()
        print("📚 Schema Usage Examples:")
        print("- Use *Create schemas for creating new records")
        print("- Use *Read schemas when fetching records with relationships")
        print("- Use *Update schemas for partial updates")
        print("- Use *Summary schemas for lightweight listings")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()