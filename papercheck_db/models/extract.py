"""Extract model - results from extraction processes."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

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

    # Extraction results, this might change often based on extractor capabilities
    extracted_title = Column(Text, nullable=True) # Title of the paper
    extracted_doi = Column(String(255), nullable=True)  # DOI of the paper
    extracted_authors = Column(JSONB, nullable=True)  # List of authors, along with affiliations and emails, etc.
    extracted_refs = Column(JSONB, nullable=True)  # List of references
    extracted_xrefs = Column(JSONB, nullable=True) # List of cross-references
    extracted_abstract = Column(Text, nullable=True)  # Abstract text
    extracted_keywords = Column(ARRAY(String), nullable=True)  # List of keywords

    # Processing information
    processing_time_seconds = Column(Float, nullable=True)
    status = Column(
        String(50), default="completed", nullable=False
    )  # completed, failed, partial
    error_message = Column(Text, nullable=True)

    # Relationships
    paper = relationship("Paper", back_populates="extracts")
    extractor = relationship("Extractor", back_populates="extracts")

    def __repr__(self):
        return f"<Extract(id={self.id}, paper_id={self.paper_id}, extractor_id={self.extractor_id}, status='{self.status}')>"
