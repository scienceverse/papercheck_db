"""ExtractEval Pydantic schemas."""

from typing import Optional, Dict, Any
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class ExtractEvalBase(BaseCreateSchema):
    """Base extractor evaluation schema with common fields."""

    extract_id: int = Field(..., description="ID of the extract being evaluated")
    extractor_id: int = Field(..., description="ID of the extractor used")
    ground_truth_id: int = Field(..., description="ID of the ground truth for comparison")
    evaluation_date: Optional[str] = Field(
        None, max_length=50, description="Evaluation date"
    )
    title_exact_match: Optional[bool] = Field(None)
    title_levenshtein_distance: Optional[int] = Field(None)
    title_semantic_similarity: Optional[float] = Field(None)
    title_length_ratio: Optional[float] = Field(None)
    doi_exact_match: Optional[bool] = Field(None)
    doi_is_valid: Optional[bool] = Field(None)
    abstract_rouge_l: Optional[float] = Field(None)
    abstract_bert_score: Optional[float] = Field(None)
    keywords_jaccard_index: Optional[float] = Field(None)
    keywords_f1: Optional[float] = Field(None)
    keywords_precision: Optional[float] = Field(None)
    keywords_recall: Optional[float] = Field(None)
    keywords_avg_jaro_winkler: Optional[float] = Field(None)
    notes: Optional[str] = Field(None, description="Additional notes")
    evaluation_details: Optional[Dict[str, Any]] = Field(
        None, description="Details on evaluation methods used"
    )


class ExtractEvalCreate(ExtractEvalBase):
    """Schema for creating an extractor evaluation."""

    pass


class ExtractEvalUpdate(BaseUpdateSchema):
    """Schema for updating an extractor evaluation."""

    evaluation_date: Optional[str] = Field(None, max_length=50)
    title_exact_match: Optional[bool] = Field(None)
    title_levenshtein_distance: Optional[int] = Field(None)
    title_semantic_similarity: Optional[float] = Field(None)
    title_length_ratio: Optional[float] = Field(None)
    doi_exact_match: Optional[bool] = Field(None)
    doi_is_valid: Optional[bool] = Field(None)
    abstract_rouge_l: Optional[float] = Field(None)
    abstract_bert_score: Optional[float] = Field(None)
    keywords_jaccard_index: Optional[float] = Field(None)
    keywords_f1: Optional[float] = Field(None)
    keywords_precision: Optional[float] = Field(None)
    keywords_recall: Optional[float] = Field(None)
    keywords_avg_jaro_winkler: Optional[float] = Field(None)
    notes: Optional[str] = Field(None)
    evaluation_details: Optional[Dict[str, Any]] = Field(None)


class ExtractEvalRead(BaseReadSchema, ExtractEvalBase):
    """Schema for reading an extractor evaluation."""

    pass


class ExtractEvalDelete(BaseDeleteSchema):
    """Schema for deleting an extractor evaluation."""

    pass


class ExtractEvalSummary(BaseReadSchema):
    """Summary schema for extractor evaluation with minimal fields."""

    extract_id: int
    extractor_id: int
    ground_truth_id: int
    evaluation_date: Optional[str] = None


class ExtractEval(ExtractEvalBase, BaseSchema):
    """Complete extractor evaluation schema for responses, matching the DB model."""

    pass
