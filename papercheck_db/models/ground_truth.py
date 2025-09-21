"""Canon model - ground truth extractions for papers."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship

from .base import BaseModel


class GroundTruth(BaseModel):
    """Canon model representing ground truth extraction for papers."""
    
    __tablename__ = "ground_truths"
    
    # Reference to paper
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False, index=True)

   
    # Core paper information
    doi = Column(String(255), unique=True, index=True, nullable=True)
    title = Column(Text, nullable=False)
    keywords = Column(ARRAY(String(50)), nullable=True)  # PostgreSQL ARRAY
    description = Column(Text, nullable=True)
    abstract = Column(Text, nullable=True)
    authors = Column(JSONB, nullable=True)  # JSON in papercheck format
    # Relationships
    paper = relationship("Paper", back_populates="canons")
    extractor_evals = relationship(
        "ExtractorEval", back_populates="ground_truth", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<GroundTruth(id={self.id}, name='{self.name}', paper_id={self.paper_id})>"
