"""Paper model - core document entities."""

from sqlalchemy import Column, String, Text, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class Paper(BaseModel):
    """Paper model representing a research document."""

    __tablename__ = "papers"

    # Core paper information
    doi = Column(String(255), unique=True, index=True, nullable=True)
    title = Column(Text, nullable=False)
    abstract = Column(Text, nullable=True)
    authors = Column(Text, nullable=True)  # JSON string or comma-separated
    publication_date = Column(String(50), nullable=True)  # Allow flexible date formats
    journal = Column(String(255), nullable=True)

    # File information
    pdf_path = Column(String(500), nullable=True)
    pdf_url = Column(String(500), nullable=True)

    # Processing status
    is_processed = Column(Boolean, default=False, nullable=False)
    processing_status = Column(String(100), default="pending", nullable=False)

    # Relationships
    extracts = relationship(
        "Extract", back_populates="paper", cascade="all, delete-orphan"
    )
    canons = relationship("Canon", back_populates="paper", cascade="all, delete-orphan")
    datasets = relationship(
        "Dataset", secondary="dataset_papers", back_populates="papers"
    )

    def __repr__(self):
        return f"<Paper(id={self.id}, title='{self.title[:50]}...', doi='{self.doi}')>"
