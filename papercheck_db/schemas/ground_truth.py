"""Canon Pydantic schemas."""

from typing import Optional, Dict, Any
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class GroundTruthBase(BaseCreateSchema):
    """Base canon schema with common fields."""

    paper_id: int = Field(..., description="ID of associated paper")
    name: str = Field(..., max_length=255, description="Canon name")
    description: Optional[str] = Field(None, description="Canon description")
    version: Optional[str] = Field(None, max_length=50, description="Canon version")
    ground_truth_data: Dict[str, Any] = Field(
        ..., description="Structured ground truth data"
    )
    annotation_schema: Optional[Dict[str, Any]] = Field(
        None, description="Annotation schema"
    )
    annotator: Optional[str] = Field(None, max_length=255, description="Annotator name")
    annotation_date: Optional[str] = Field(
        None, max_length=50, description="Annotation date"
    )
    confidence_score: Optional[str] = Field(
        None, max_length=50, description="Confidence score"
    )
    reviewed: str = Field("false", max_length=10, description="Review status")
    reviewer: Optional[str] = Field(None, max_length=255, description="Reviewer name")
    review_notes: Optional[str] = Field(None, description="Review notes")


class GroundTruthCreate(GroundTruthBase):
    """Schema for creating a canon."""

    pass


class GroundTruthUpdate(BaseUpdateSchema):
    """Schema for updating a canon."""

    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None)
    version: Optional[str] = Field(None, max_length=50)
    ground_truth_data: Optional[Dict[str, Any]] = Field(None)
    annotation_schema: Optional[Dict[str, Any]] = Field(None)
    annotator: Optional[str] = Field(None, max_length=255)
    annotation_date: Optional[str] = Field(None, max_length=50)
    confidence_score: Optional[str] = Field(None, max_length=50)
    reviewed: Optional[str] = Field(None, max_length=10)
    reviewer: Optional[str] = Field(None, max_length=255)
    review_notes: Optional[str] = Field(None)


class GroundTruth(BaseSchema, GroundTruthBase):
    """Complete canon schema for responses."""

    pass


class GroundTruthSummary(BaseSchema):
    """Summary canon schema for list responses."""

    paper_id: int
    name: str
    version: Optional[str]
    annotator: Optional[str]
    reviewed: str
