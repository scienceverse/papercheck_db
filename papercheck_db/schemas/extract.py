"""Extract Pydantic schemas."""

from typing import Optional, Dict, Any
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class ExtractBase(BaseCreateSchema):
    """Base extract schema with common fields."""

    paper_id: int = Field(..., description="ID of associated paper")
    extractor_id: int = Field(..., description="ID of associated extractor")
    extraction_date: Optional[str] = Field(
        None, max_length=50, description="Extraction date"
    )
    extractor_version: Optional[str] = Field(
        None, max_length=50, description="Extractor version used"
    )
    config_used: Optional[Dict[str, Any]] = Field(
        None, description="Configuration used"
    )
    extracted_data: Dict[str, Any] = Field(..., description="Extracted data")
    raw_output: Optional[str] = Field(None, description="Raw extractor output")
    processing_time_seconds: Optional[float] = Field(
        None, description="Processing time in seconds"
    )
    status: str = Field("completed", max_length=50, description="Extraction status")
    error_message: Optional[str] = Field(None, description="Error message if failed")
    confidence_scores: Optional[Dict[str, Any]] = Field(
        None, description="Confidence scores"
    )
    extraction_quality: Optional[str] = Field(
        None, max_length=50, description="Overall quality"
    )
    is_validated: str = Field("false", max_length=10, description="Validation status")
    validator: Optional[str] = Field(None, max_length=255, description="Validator name")
    validation_notes: Optional[str] = Field(None, description="Validation notes")


class ExtractCreate(ExtractBase):
    """Schema for creating an extract."""

    pass


class ExtractUpdate(BaseUpdateSchema):
    """Schema for updating an extract."""

    extraction_date: Optional[str] = Field(None, max_length=50)
    extractor_version: Optional[str] = Field(None, max_length=50)
    config_used: Optional[Dict[str, Any]] = Field(None)
    extracted_data: Optional[Dict[str, Any]] = Field(None)
    raw_output: Optional[str] = Field(None)
    processing_time_seconds: Optional[float] = Field(None)
    status: Optional[str] = Field(None, max_length=50)
    error_message: Optional[str] = Field(None)
    confidence_scores: Optional[Dict[str, Any]] = Field(None)
    extraction_quality: Optional[str] = Field(None, max_length=50)
    is_validated: Optional[str] = Field(None, max_length=10)
    validator: Optional[str] = Field(None, max_length=255)
    validation_notes: Optional[str] = Field(None)


class Extract(BaseSchema, ExtractBase):
    """Complete extract schema for responses."""

    pass


class ExtractSummary(BaseSchema):
    """Summary extract schema for list responses."""

    paper_id: int
    extractor_id: int
    status: str
    extraction_quality: Optional[str]
    is_validated: str
