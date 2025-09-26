"""Schemas package for papercheck_db."""

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema
from .paper import Paper, PaperCreate, PaperUpdate, PaperSummary
from .dataset import Dataset, DatasetCreate, DatasetUpdate, DatasetSummary
from .ground_truth import GroundTruth, GroundTruthCreate, GroundTruthUpdate, GroundTruthSummary
from .extractor import Extractor, ExtractorCreate, ExtractorUpdate, ExtractorSummary
from .extract import Extract, ExtractCreate, ExtractUpdate, ExtractSummary
from .extracteval import (
    ExtractEval,
    ExtractEvalCreate,
    ExtractEvalUpdate,
    ExtractEvalSummary,
)

__all__ = [
    # Base schemas
    "BaseSchema",
    "BaseCreateSchema",
    "BaseUpdateSchema",
    # Paper schemas
    "Paper",
    "PaperCreate",
    "PaperUpdate",
    "PaperSummary",
    # Dataset schemas
    "Dataset",
    "DatasetCreate",
    "DatasetUpdate",
    "DatasetSummary",
    # Ground Truth schemas
    "GroundTruth",
    "GroundTruthCreate",
    "GroundTruthUpdate",
    "GroundTruthSummary",
    # Extractor schemas
    "Extractor",
    "ExtractorCreate",
    "ExtractorUpdate",
    "ExtractorSummary",
    # Extract schemas
    "Extract",
    "ExtractCreate",
    "ExtractUpdate",
    "ExtractSummary",
    # ExtractEval schemas
    "ExtractEval",
    "ExtractEvalCreate",
    "ExtractEvalUpdate",
    "ExtractEvalSummary",
]
