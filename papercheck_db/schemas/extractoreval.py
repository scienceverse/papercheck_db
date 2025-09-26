"""ExtractEval Pydantic schemas."""

from typing import Optional, Dict, Any
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema


class ExtractEvalBase(BaseCreateSchema):
    """Base extractor evaluation schema with common fields."""

    extractor_id: int = Field(..., description="ID of associated extractor")
    ground_truth_id: int = Field(..., description="ID of associated ground truth")
    evaluation_date: Optional[str] = Field(
        None, max_length=50, description="Evaluation date"
    )
    evaluator: Optional[str] = Field(None, max_length=255, description="Evaluator name")
    evaluation_method: Optional[str] = Field(
        None, max_length=100, description="Evaluation method"
    )
    accuracy: Optional[float] = Field(None, ge=0, le=1, description="Accuracy score")
    precision: Optional[float] = Field(None, ge=0, le=1, description="Precision score")
    recall: Optional[float] = Field(None, ge=0, le=1, description="Recall score")
    f1_score: Optional[float] = Field(None, ge=0, le=1, description="F1 score")
    field_level_scores: Optional[Dict[str, Any]] = Field(
        None, description="Per-field scores"
    )
    confusion_matrix: Optional[Dict[str, Any]] = Field(
        None, description="Confusion matrix"
    )
    detailed_results: Optional[Dict[str, Any]] = Field(
        None, description="Detailed results"
    )
    overall_rating: Optional[str] = Field(
        None, max_length=50, description="Overall rating"
    )
    strengths: Optional[str] = Field(None, description="Identified strengths")
    weaknesses: Optional[str] = Field(None, description="Identified weaknesses")
    recommendations: Optional[str] = Field(None, description="Recommendations")
    evaluation_criteria: Optional[Dict[str, Any]] = Field(
        None, description="Evaluation criteria"
    )
    notes: Optional[str] = Field(None, description="Additional notes")


class ExtractEvalCreate(ExtractEvalBase):
    """Schema for creating an extractor evaluation."""

    pass


class ExtractEvalUpdate(BaseUpdateSchema):
    """Schema for updating an extractor evaluation."""

    evaluation_date: Optional[str] = Field(None, max_length=50)
    evaluator: Optional[str] = Field(None, max_length=255)
    evaluation_method: Optional[str] = Field(None, max_length=100)
    accuracy: Optional[float] = Field(None, ge=0, le=1)
    precision: Optional[float] = Field(None, ge=0, le=1)
    recall: Optional[float] = Field(None, ge=0, le=1)
    f1_score: Optional[float] = Field(None, ge=0, le=1)
    field_level_scores: Optional[Dict[str, Any]] = Field(None)
    confusion_matrix: Optional[Dict[str, Any]] = Field(None)
    detailed_results: Optional[Dict[str, Any]] = Field(None)
    overall_rating: Optional[str] = Field(None, max_length=50)
    strengths: Optional[str] = Field(None)
    weaknesses: Optional[str] = Field(None)
    recommendations: Optional[str] = Field(None)
    evaluation_criteria: Optional[Dict[str, Any]] = Field(None)
    notes: Optional[str] = Field(None)


class ExtractEval(BaseSchema, ExtractEvalBase):
    """Complete extractor evaluation schema for responses."""

    pass


class ExtractEvalSummary(BaseSchema):
    """Summary extractor evaluation schema for list responses."""

    extractor_id: int
    ground_truth_id: int
    f1_score: Optional[float]
    overall_rating: Optional[str]
    evaluator: Optional[str]
