"""Extractor Pydantic schemas."""

from typing import Optional, Dict, Any, List
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class ExtractorBase(BaseCreateSchema):
    """Base extractor schema with common fields."""

    name: str = Field(..., max_length=255, description="Extractor name")
    description: Optional[str] = Field(None, description="Extractor description")
    version: Optional[str] = Field(None, max_length=50, description="Extractor version")
    extractor_type: str = Field(..., max_length=100, description="Extractor type")
    implementation: Optional[str] = Field(
        None, max_length=100, description="Implementation language/platform"
    )
    config_schema: Optional[Dict[str, Any]] = Field(
        None, description="Configuration schema"
    )
    default_config: Optional[Dict[str, Any]] = Field(
        None, description="Default configuration"
    )
    is_active: bool = Field(True, description="Whether extractor is active")
    author: Optional[str] = Field(None, max_length=255, description="Author name")
    contact_email: Optional[str] = Field(
        None, max_length=255, description="Contact email"
    )
    documentation_url: Optional[str] = Field(
        None, max_length=500, description="Documentation URL"
    )
    repository_url: Optional[str] = Field(
        None, max_length=500, description="Repository URL"
    )
    supported_formats: Optional[str] = Field(None, description="Supported formats")
    performance_notes: Optional[str] = Field(None, description="Performance notes")


class ExtractorCreate(ExtractorBase):
    """Schema for creating an extractor."""

    pass


class ExtractorUpdate(BaseUpdateSchema):
    """Schema for updating an extractor."""

    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None)
    version: Optional[str] = Field(None, max_length=50)
    extractor_type: Optional[str] = Field(None, max_length=100)
    implementation: Optional[str] = Field(None, max_length=100)
    config_schema: Optional[Dict[str, Any]] = Field(None)
    default_config: Optional[Dict[str, Any]] = Field(None)
    is_active: Optional[bool] = Field(None)
    author: Optional[str] = Field(None, max_length=255)
    contact_email: Optional[str] = Field(None, max_length=255)
    documentation_url: Optional[str] = Field(None, max_length=500)
    repository_url: Optional[str] = Field(None, max_length=500)
    supported_formats: Optional[str] = Field(None)
    performance_notes: Optional[str] = Field(None)


class ExtractorRead(BaseReadSchema, ExtractorBase):
    """Schema for reading an extractor."""

    pass


class ExtractorDelete(BaseDeleteSchema):
    """Schema for deleting an extractor."""

    pass


class ExtractorSummary(BaseReadSchema):
    """Summary schema for extractor with minimal fields."""

    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    extractor_type: str
    is_active: bool = True


class Extractor(ExtractorBase, BaseSchema):
    """Complete extractor schema for responses, matching the DB model."""

    pass
