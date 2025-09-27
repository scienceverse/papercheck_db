"""Ground Truth model - ground truth extractions for papers."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship

from .base import BaseModel


class GroundTruth(BaseModel):
    """Ground Truth model representing ground truth extraction for papers."""
    
    __tablename__ = "ground_truths"
    
    # Reference to paper
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False, index=True)

   
    # Extraction results, this might change often based on extractor capabilities
    title = Column(Text, nullable=True) # Title of the paper
    doi = Column(String(255), nullable=True)  # DOI of the paper
    authors = Column(JSONB, nullable=True)  # List of authors, along with affiliations and emails, etc.
    refs = Column(JSONB, nullable=True)  # List of references
    xrefs = Column(JSONB, nullable=True) # List of cross-references
    abstract = Column(Text, nullable=True)  # Abstract text
    keywords = Column(ARRAY(String), nullable=True)  # List of keywords
    # Relationships
    paper = relationship("Paper", back_populates="ground_truth", uselist=False)
    extract_evals = relationship(
        "ExtractEval", back_populates="ground_truth", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<GroundTruth(id={self.id}, name='{self.name}', paper_id={self.paper_id})>"
