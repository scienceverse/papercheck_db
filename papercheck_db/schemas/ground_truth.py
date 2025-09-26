"""GroundTruth Pydantic schemas."""

from typing import Optional, Dict, Any, List
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class GroundTruthBase(BaseCreateSchema):
    """Base ground truth schema with common fields."""

    paper_id: int = Field(..., description="ID of associated paper")
    title: Optional[str] = Field(None, description="Title of the paper")
    doi: Optional[str] = Field(None, max_length=255, description="DOI of the paper")
    authors: Optional[Dict[str, Any]] = Field(
        None, description="List of authors"
    )
    refs: Optional[Dict[str, Any]] = Field(
        None, description="List of references"
    )
    xrefs: Optional[Dict[str, Any]] = Field(
        None, description="List of cross-references"
    )
    abstract: Optional[str] = Field(None, description="Abstract text")
    keywords: Optional[List[str]] = Field(None, description="List of keywords")


class GroundTruthCreate(GroundTruthBase):
    """Schema for creating a ground truth."""

    pass


class GroundTruthUpdate(BaseUpdateSchema):
    """Schema for updating a ground truth."""

    title: Optional[str] = Field(None)
    doi: Optional[str] = Field(None, max_length=255)
    authors: Optional[Dict[str, Any]] = Field(None)
    refs: Optional[Dict[str, Any]] = Field(None)
    xrefs: Optional[Dict[str, Any]] = Field(None)
    abstract: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(None)


class GroundTruthRead(BaseReadSchema, GroundTruthBase):
    """Schema for reading a ground truth."""

    pass


class GroundTruthDelete(BaseDeleteSchema):
    """Schema for deleting a ground truth."""

    pass


class GroundTruthSummary(BaseReadSchema):
    """Summary schema for ground truth with minimal fields."""

    paper_id: int
    title: Optional[str] = None
    doi: Optional[str] = None


class GroundTruth(GroundTruthBase, BaseSchema):
    """Complete ground truth schema for responses, matching the DB model."""

    pass
