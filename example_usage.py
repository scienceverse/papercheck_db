#!/usr/bin/env python3
"""Example script showing how to use the papercheck_db models and schemas."""

import os
from datetime import datetime
from pprint import pprint

# Set environment variables for demo
os.environ.update({
    'DATABASE_URL': 'postgresql://username:password@localhost:5432/papercheck_db',
    'SECRET_KEY': 'demo-secret-key',
    'POSTGRES_USER': 'username',
    'POSTGRES_PASSWORD': 'password', 
    'POSTGRES_DB': 'papercheck_db'
})

def demo_schemas():
    """Demonstrate how to use Pydantic schemas."""
    print("🔧 Demonstrating Pydantic Schemas\n")
    
    from papercheck_db.schemas import (
        PaperCreate, Paper,
        DatasetCreate, Dataset,
        ExtractorCreate, Extractor,
        CanonCreate, Canon,
        ExtractCreate, Extract,
        ExtractorEvalCreate, ExtractorEval
    )
    
    # Create a paper
    paper_data = PaperCreate(
        title="A Study of Machine Learning in Research Paper Analysis",
        abstract="This paper investigates the application of ML techniques...",
        doi="10.1000/182",
        authors="Smith, J., Doe, A., Johnson, M.",
        publication_date="2024-01-15",
        journal="Journal of AI Research",
        pdf_path="/papers/smith_2024.pdf"
    )
    print("Paper creation schema:")
    pprint(paper_data.model_dump())
    print()
    
    # Create a dataset
    dataset_data = DatasetCreate(
        name="AI Research Papers 2024",
        description="Collection of AI research papers from 2024",
        version="1.0",
        tags="ai,machine-learning,2024",
        source="arXiv",
        license="CC BY 4.0"
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
        author="Research Team",
        contact_email="team@university.edu"
    )
    print("Extractor creation schema:")
    pprint(extractor_data.model_dump())
    print()

def demo_model_relationships():
    """Demonstrate model relationships."""
    print("🔗 Demonstrating Model Relationships\n")
    
    from papercheck_db.models import Paper, Dataset, Extractor, Extract, Canon
    
    print("Model relationships:")
    print("- Papers ↔ Datasets (many-to-many via dataset_papers)")
    print("- Papers → Extracts (one-to-many)")
    print("- Papers → Canons (one-to-many)")
    print("- Extractors → Extracts (one-to-many)")
    print("- Extractors + Canons → ExtractorEvals (evaluation)")
    print()
    
    print("Example table structures:")
    print(f"Paper table: {Paper.__tablename__}")
    print(f"Dataset table: {Dataset.__tablename__}")
    print(f"Extractor table: {Extractor.__tablename__}")
    print()

def demo_configuration():
    """Demonstrate configuration management."""
    print("⚙️  Demonstrating Configuration\n")
    
    from papercheck_db.core.config import settings
    
    print("Configuration settings:")
    print(f"- Environment: {settings.environment}")
    print(f"- Database URL: {settings.database_url}")
    print(f"- API prefix: {settings.api_v1_str}")
    print(f"- Debug mode: {settings.debug}")
    print(f"- Is development: {settings.is_development}")
    print(f"- Is production: {settings.is_production}")
    print()

def main():
    """Run all demonstrations."""
    print("📋 PaperCheck DB - Usage Examples")
    print("=" * 50)
    print()
    
    try:
        demo_configuration()
        demo_schemas()
        demo_model_relationships()
        
        print("✅ All demonstrations completed successfully!")
        print("\nNext steps:")
        print("1. Set up your PostgreSQL database")
        print("2. Copy .env.example to .env and configure")
        print("3. Run: poetry run alembic upgrade head")
        print("4. Start the API: poetry run python main.py")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()