"""Schemas package for papercheck_db."""

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema
from .paper import Paper, PaperCreate, PaperUpdate, PaperSummary
from .dataset import Dataset, DatasetCreate, DatasetUpdate, DatasetSummary
from .ground_truth import GroundTruth, GroundTruthCreate, GroundTruthUpdate, GroundTruthSummary
from .extractor import Extractor, ExtractorCreate, ExtractorUpdate, ExtractorSummary
from .extract import Extract, ExtractCreate, ExtractUpdate, ExtractSummary
from .extractoreval import (
    ExtractorEval,
    ExtractorEvalCreate,
    ExtractorEvalUpdate,
    ExtractorEvalSummary,
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
    # Canon schemas
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
    # ExtractorEval schemas
    "ExtractorEval",
    "ExtractorEvalCreate",
    "ExtractorEvalUpdate",
    "ExtractorEvalSummary",
]
