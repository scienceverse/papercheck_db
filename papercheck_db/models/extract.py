"""Extract model - results from extraction processes."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship

from .base import BaseModel


class Extract(BaseModel):
    """Extract model representing results from extraction processes."""

    __tablename__ = "extracts"

    # References
    paper_id = Column(Integer, ForeignKey("papers.id"), nullable=False, index=True)
    extractor_id = Column(
        Integer, ForeignKey("extractors.id"), nullable=False, index=True
    )

    # Extraction metadata
    extraction_date = Column(String(50), nullable=True)
    extractor_version = Column(String(50), nullable=True)
    config_used = Column(JSON, nullable=True)  # Configuration parameters used

    # Extraction results
    extracted_data = Column(JSON, nullable=False)  # The actual extracted information
    raw_output = Column(
        Text, nullable=True
    )  # Raw output from extractor (if applicable)

    # Processing information
    processing_time_seconds = Column(Float, nullable=True)
    status = Column(
        String(50), default="completed", nullable=False
    )  # completed, failed, partial
    error_message = Column(Text, nullable=True)

    # Quality metrics
    confidence_scores = Column(JSON, nullable=True)  # Per-field confidence scores
    extraction_quality = Column(String(50), nullable=True)  # overall quality assessment

    # Validation
    is_validated = Column(
        String(10), default="false", nullable=False
    )  # "true"/"false" as string
    validator = Column(String(255), nullable=True)
    validation_notes = Column(Text, nullable=True)

    # Relationships
    paper = relationship("Paper", back_populates="extracts")
    extractor = relationship("Extractor", back_populates="extracts")

    def __repr__(self):
        return f"<Extract(id={self.id}, paper_id={self.paper_id}, extractor_id={self.extractor_id}, status='{self.status}')>"
