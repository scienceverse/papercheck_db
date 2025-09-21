"""GroundTruth Pydantic schemas."""

from typing import Optional, Dict, Any
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class GroundTruthBase(BaseCreateSchema):
    """Base ground truth schema with common fields."""

    paper_id: int = Field(..., description="ID of associated paper")
    name: str = Field(..., max_length=255, description="GroundTruth name")
    description: Optional[str] = Field(None, description="GroundTruth description")
    version: Optional[str] = Field(None, max_length=50, description="GroundTruth version")
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
    """Schema for creating a ground truth."""

    pass


class GroundTruthUpdate(BaseUpdateSchema):
    """Schema for updating a ground truth."""

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
    """Complete ground truth schema for responses."""

    pass


class GroundTruthSummary(BaseSchema):
    """Summary ground truth schema for list responses."""

    paper_id: int
    name: str
    version: Optional[str]
    annotator: Optional[str]
    reviewed: str
