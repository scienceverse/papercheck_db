"""Dataset model - named collections of papers."""

from sqlalchemy import Column, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from .base import BaseModel


# Association table for many-to-many relationship between datasets and papers
dataset_paper_association = Table(
    "dataset_papers",
    BaseModel.metadata,
    Column("dataset_id", ForeignKey("datasets.id"), primary_key=True),
    Column("paper_id", ForeignKey("papers.id"), primary_key=True),
)


class Dataset(BaseModel):
    """Dataset model representing a named collection of papers."""

    __tablename__ = "datasets"

    # Dataset information
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    version = Column(String(50), nullable=True)

    # Metadata
    source = Column(String(255), nullable=True)
    license = Column(String(100), nullable=True)

    folder_path = Column(String(500), nullable=True)  # Path to dataset folder if applicable


    # Relationships
    papers = relationship(
        "Paper",
        secondary=dataset_paper_association,
        back_populates="datasets",
        lazy="select",
    )

    def __repr__(self):
        return f"<Dataset(id={self.id}, name='{self.name}', papers_count={len(self.papers)})>"
