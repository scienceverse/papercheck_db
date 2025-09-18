"""Extractor model - extraction tools and methods."""

from sqlalchemy import Column, String, Text, JSON, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class Extractor(BaseModel):
    """Extractor model representing extraction tools and methods."""

    __tablename__ = "extractors"

    # Extractor information
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    version = Column(String(50), nullable=True)

    # Technical details
    extractor_type = Column(
        String(100), nullable=False
    )  # e.g., "rule-based", "ml", "llm"
    implementation = Column(String(100), nullable=True)  # e.g., "python", "r", "api"

    # Configuration
    config_schema = Column(JSON, nullable=True)  # Schema for configuration parameters
    default_config = Column(JSON, nullable=True)  # Default configuration

    # Status and metadata
    is_active = Column(Boolean, default=True, nullable=False)
    author = Column(String(255), nullable=True)
    contact_email = Column(String(255), nullable=True)
    documentation_url = Column(String(500), nullable=True)
    repository_url = Column(String(500), nullable=True)

    # Performance metadata
    supported_formats = Column(Text, nullable=True)  # JSON string or comma-separated
    performance_notes = Column(Text, nullable=True)

    # Relationships
    extracts = relationship(
        "Extract", back_populates="extractor", cascade="all, delete-orphan"
    )
    extractor_evals = relationship(
        "ExtractorEval", back_populates="extractor", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Extractor(id={self.id}, name='{self.name}', type='{self.extractor_type}')>"
