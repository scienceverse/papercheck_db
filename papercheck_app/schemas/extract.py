"""Extract Pydantic schemas."""

from typing import Optional, Dict, Any, List
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class ExtractBase(BaseCreateSchema):
    """Base extract schema with common fields."""

    paper_id: int = Field(..., description="ID of associated paper")
    extractor_id: int = Field(..., description="ID of associated extractor")
    extraction_date: Optional[str] = Field(
        None, max_length=50, description="Extraction date"
    )
    extracted_title: Optional[str] = Field(None, description="Extracted title")
    extracted_doi: Optional[str] = Field(None, max_length=255, description="Extracted DOI")
    extracted_authors: Optional[Dict[str, Any]] = Field(
        None, description="Extracted authors"
    )
    extracted_refs: Optional[Dict[str, Any]] = Field(
        None, description="Extracted references"
    )
    extracted_xrefs: Optional[Dict[str, Any]] = Field(
        None, description="Extracted cross-references"
    )
    extracted_abstract: Optional[str] = Field(None, description="Extracted abstract")
    extracted_keywords: Optional[List[str]] = Field(
        None, description="Extracted keywords"
    )
    processing_time_seconds: Optional[float] = Field(
        None, description="Processing time in seconds"
    )
    status: str = Field("completed", max_length=50, description="Extraction status")
    error_message: Optional[str] = Field(None, description="Error message if failed")


class ExtractCreate(ExtractBase):
    """Schema for creating an extract."""

    pass


class ExtractUpdate(BaseUpdateSchema):
    """Schema for updating an extract."""

    extraction_date: Optional[str] = Field(None, max_length=50)
    extracted_title: Optional[str] = Field(None)
    extracted_doi: Optional[str] = Field(None, max_length=255)
    extracted_authors: Optional[Dict[str, Any]] = Field(None)
    extracted_refs: Optional[Dict[str, Any]] = Field(None)
    extracted_xrefs: Optional[Dict[str, Any]] = Field(None)
    extracted_abstract: Optional[str] = Field(None)
    extracted_keywords: Optional[List[str]] = Field(None)
    processing_time_seconds: Optional[float] = Field(None)
    status: Optional[str] = Field(None, max_length=50)
    error_message: Optional[str] = Field(None)


class ExtractRead(BaseReadSchema, ExtractBase):
    """Schema for reading an extract."""

    pass


class ExtractDelete(BaseDeleteSchema):
    """Schema for deleting an extract."""

    pass


class ExtractSummary(BaseReadSchema):
    """Summary schema for extract with minimal fields."""

    paper_id: int
    extractor_id: int
    extracted_title: Optional[str] = None
    status: str = "completed"


class Extract(ExtractBase, BaseSchema):
    """Complete extract schema for responses, matching the DB model."""

    pass
