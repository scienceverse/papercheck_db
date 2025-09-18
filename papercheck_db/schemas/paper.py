"""Paper Pydantic schemas."""

from typing import Optional
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class PaperBase(BaseCreateSchema):
    """Base paper schema with common fields."""

    doi: Optional[str] = Field(
        None, max_length=255, description="Digital Object Identifier"
    )
    title: str = Field(..., description="Paper title")
    abstract: Optional[str] = Field(None, description="Paper abstract")
    authors: Optional[str] = Field(
        None, description="Authors (JSON string or comma-separated)"
    )
    publication_date: Optional[str] = Field(
        None, max_length=50, description="Publication date"
    )
    journal: Optional[str] = Field(None, max_length=255, description="Journal name")
    pdf_path: Optional[str] = Field(
        None, max_length=500, description="Local PDF file path"
    )
    pdf_url: Optional[str] = Field(None, max_length=500, description="PDF URL")
    is_processed: bool = Field(False, description="Whether paper has been processed")
    processing_status: str = Field(
        "pending", max_length=100, description="Processing status"
    )


class PaperCreate(PaperBase):
    """Schema for creating a paper."""

    pass


class PaperUpdate(BaseUpdateSchema):
    """Schema for updating a paper."""

    doi: Optional[str] = Field(None, max_length=255)
    title: Optional[str] = Field(None)
    abstract: Optional[str] = Field(None)
    authors: Optional[str] = Field(None)
    publication_date: Optional[str] = Field(None, max_length=50)
    journal: Optional[str] = Field(None, max_length=255)
    pdf_path: Optional[str] = Field(None, max_length=500)
    pdf_url: Optional[str] = Field(None, max_length=500)
    is_processed: Optional[bool] = Field(None)
    processing_status: Optional[str] = Field(None, max_length=100)


class Paper(BaseSchema, PaperBase):
    """Complete paper schema for responses."""

    # Note: extracts, canons, and datasets would be included via relationships
    # but we'll keep them optional to avoid circular imports
    pass


class PaperSummary(BaseSchema):
    """Summary paper schema for list responses."""

    doi: Optional[str]
    title: str
    authors: Optional[str]
    journal: Optional[str]
    is_processed: bool
    processing_status: str
