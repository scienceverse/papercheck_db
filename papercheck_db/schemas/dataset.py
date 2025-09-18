"""Dataset Pydantic schemas."""

from typing import Optional
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class DatasetBase(BaseCreateSchema):
    """Base dataset schema with common fields."""

    name: str = Field(..., max_length=255, description="Dataset name")
    description: Optional[str] = Field(None, description="Dataset description")
    version: Optional[str] = Field(None, max_length=50, description="Dataset version")
    tags: Optional[str] = Field(
        None, description="Tags (JSON string or comma-separated)"
    )
    source: Optional[str] = Field(None, max_length=255, description="Data source")
    license: Optional[str] = Field(
        None, max_length=100, description="License information"
    )


class DatasetCreate(DatasetBase):
    """Schema for creating a dataset."""

    pass


class DatasetUpdate(BaseUpdateSchema):
    """Schema for updating a dataset."""

    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None)
    version: Optional[str] = Field(None, max_length=50)
    tags: Optional[str] = Field(None)
    source: Optional[str] = Field(None, max_length=255)
    license: Optional[str] = Field(None, max_length=100)


class Dataset(BaseSchema, DatasetBase):
    """Complete dataset schema for responses."""

    # papers_count can be computed property
    pass


class DatasetSummary(BaseSchema):
    """Summary dataset schema for list responses."""

    name: str
    description: Optional[str]
    version: Optional[str]
    # papers_count: Optional[int] = Field(None, description="Number of papers in dataset")
