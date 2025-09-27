"""Dataset Pydantic schemas."""

from typing import Optional, List
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class DatasetBase(BaseCreateSchema):
    """Base dataset schema with common fields."""

    name: str = Field(..., max_length=255, description="Dataset name")
    description: Optional[str] = Field(None, description="Dataset description")
    version: Optional[str] = Field(None, max_length=50, description="Dataset version")
    source: Optional[str] = Field(None, max_length=255, description="Data source")
    license: Optional[str] = Field(
        None, max_length=100, description="License information"
    )
    folder_path: Optional[str] = Field(
        None, max_length=500, description="Path to dataset folder"
    )


class DatasetCreate(DatasetBase):
    """Schema for creating a dataset."""

    pass


class DatasetUpdate(BaseUpdateSchema):
    """Schema for updating a dataset."""

    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None)
    version: Optional[str] = Field(None, max_length=50)
    source: Optional[str] = Field(None, max_length=255)
    license: Optional[str] = Field(None, max_length=100)
    folder_path: Optional[str] = Field(None, max_length=500)


class DatasetRead(BaseReadSchema, DatasetBase):
    """Schema for reading a dataset."""

    # The 'papers' field will be populated from the relationship
    # To avoid circular dependency issues, we might not include the full PaperRead here
    # depending on the use case. For now, we can omit it or use a forward reference.
    # For simplicity, we'll define a minimal paper representation or just IDs.
    papers: List[int] = Field([], description="List of paper IDs in the dataset")


class DatasetDelete(BaseDeleteSchema):
    """Schema for deleting a dataset."""

    pass


class DatasetSummary(BaseReadSchema):
    """Summary schema for dataset with minimal fields."""

    name: str
    description: Optional[str] = None
    version: Optional[str] = None


class Dataset(DatasetBase, BaseSchema):
    """Complete dataset schema for responses, matching the DB model."""

    pass
