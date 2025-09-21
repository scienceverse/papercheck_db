"""Canon model - ground truth extractions for papers."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class Canon(BaseModel):
    """Canon model representing ground truth extraction for papers."""
    
    __tablename__ = "canons"
    
    # Reference to paper
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False, index=True)

    # Canon information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    version = Column(String(50), nullable=True)

    # Ground truth data
    ground_truth_data = Column(JSON, nullable=False)  # Structured extraction data
    annotation_schema = Column(
        JSON, nullable=True
    )  # Schema describing the annotation format

    # Metadata
    annotator = Column(String(255), nullable=True)
    annotation_date = Column(String(50), nullable=True)
    confidence_score = Column(
        String(50), nullable=True
    )  # e.g., "high", "medium", "low"

    # Quality assurance
    reviewed = Column(
        String(10), default="false", nullable=False
    )  # "true"/"false" as string
    reviewer = Column(String(255), nullable=True)
    review_notes = Column(Text, nullable=True)

    # Relationships
    paper = relationship("Paper", back_populates="canons")
    extractor_evals = relationship(
        "ExtractorEval", back_populates="canon", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Canon(id={self.id}, name='{self.name}', paper_id={self.paper_id})>"
