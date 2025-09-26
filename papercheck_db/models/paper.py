"""Paper model - core document entities."""

from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from .base import BaseModel


class Paper(BaseModel):
    """Paper model representing a research document."""

    __tablename__ = "papers"

    # File information
    pdf_path = Column(String(500), nullable=True)
    pdf_url = Column(String(500), nullable=True)

    pdf_hash = Column(String(64), unique=True, nullable=True, index=True)  # SHA-256 hash of the PDF

    pdf_actual_start_page = Column(Integer, default=1, nullable=False)
    pdf_actual_last_page = Column(Integer, nullable=True)  # last page number that is taken into account

    source = Column(String(255), nullable=True)  # Source of the paper (e.g., arXiv, manual upload)
    # Relationships
    extracts = relationship(
        "Extract", back_populates="paper", cascade="all, delete-orphan"
    )
    ground_truth = relationship("GroundTruth", back_populates="paper", cascade="all, delete-orphan", uselist=False)
    datasets = relationship(
        "Dataset", secondary="dataset_papers", back_populates="papers"
    )

    def __repr__(self):
        return f"<Paper(id={self.id}, title='{self.title[:50]}...', doi='{self.doi}')>"
