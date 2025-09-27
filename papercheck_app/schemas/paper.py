"""Paper Pydantic schemas."""

from typing import Optional, List

from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema
from .extract import ExtractRead
from .ground_truth import GroundTruthRead
from .dataset import DatasetRead


class PaperBase(BaseCreateSchema):
    """Base paper schema with common fields."""

    pdf_path: Optional[str] = Field(
        None, max_length=500, description="Local PDF file path"
    )
    pdf_url: Optional[str] = Field(None, max_length=500, description="PDF URL")
    pdf_hash: Optional[str] = Field(
        None, max_length=64, description="SHA-256 hash of the PDF"
    )
    pdf_actual_start_page: int = Field(1, description="Actual start page of the PDF")
    pdf_actual_last_page: Optional[int] = Field(
        None, description="Last page number to consider"
    )
    source: Optional[str] = Field(
        None, max_length=255, description="Source of the paper"
    )


class PaperCreate(PaperBase):
    """Schema for creating a paper."""

    pass


class PaperUpdate(BaseUpdateSchema):
    """Schema for updating a paper."""

    pdf_path: Optional[str] = Field(None, max_length=500)
    pdf_url: Optional[str] = Field(None, max_length=500)
    pdf_hash: Optional[str] = Field(None, max_length=64)
    pdf_actual_start_page: Optional[int] = Field(None)
    pdf_actual_last_page: Optional[int] = Field(None)
    source: Optional[str] = Field(None, max_length=255)


class PaperRead(BaseReadSchema, PaperBase):
    """Schema for reading a paper, includes relationships."""

    extracts: List[ExtractRead] = []
    ground_truth: Optional[GroundTruthRead] = None
    datasets: List[DatasetRead] = []


class PaperDelete(BaseDeleteSchema):
    """Schema for deleting a paper."""

    pass


class PaperSummary(BaseReadSchema):
    """Summary schema for paper with minimal fields."""

    pdf_path: Optional[str] = None
    pdf_url: Optional[str] = None
    source: Optional[str] = None


class Paper(PaperBase, BaseSchema):
    """Complete paper schema for responses, matching the DB model."""

    pass
