"""Schemas package for papercheck_db."""

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseDeleteSchema
from .paper import Paper, PaperCreate, PaperUpdate, PaperRead, PaperDelete, PaperSummary
from .dataset import Dataset, DatasetCreate, DatasetUpdate, DatasetRead, DatasetDelete, DatasetSummary
from .ground_truth import GroundTruth, GroundTruthCreate, GroundTruthUpdate, GroundTruthRead, GroundTruthDelete, GroundTruthSummary
from .extractor import Extractor, ExtractorCreate, ExtractorUpdate, ExtractorRead, ExtractorDelete, ExtractorSummary
from .extract import Extract, ExtractCreate, ExtractUpdate, ExtractRead, ExtractDelete, ExtractSummary
from .extracteval import (
    ExtractEval,
    ExtractEvalCreate,
    ExtractEvalUpdate,
    ExtractEvalRead,
    ExtractEvalDelete,
    ExtractEvalSummary,
)

__all__ = [
    # Base schemas
    "BaseSchema",
    "BaseCreateSchema",
    "BaseUpdateSchema",
    "BaseDeleteSchema",
    # Paper schemas
    "Paper",
    "PaperCreate",
    "PaperUpdate",
    "PaperRead",
    "PaperDelete",
    "PaperSummary",
    # Dataset schemas
    "Dataset",
    "DatasetCreate",
    "DatasetUpdate",
    "DatasetRead",
    "DatasetDelete",
    "DatasetSummary",
    # Ground Truth schemas
    "GroundTruth",
    "GroundTruthCreate",
    "GroundTruthUpdate",
    "GroundTruthRead",
    "GroundTruthDelete",
    "GroundTruthSummary",
    # Extractor schemas
    "Extractor",
    "ExtractorCreate",
    "ExtractorUpdate",
    "ExtractorRead",
    "ExtractorDelete",
    "ExtractorSummary",
    # Extract schemas
    "Extract",
    "ExtractCreate",
    "ExtractUpdate",
    "ExtractRead",
    "ExtractDelete",
    "ExtractSummary",
    # ExtractEval schemas
    "ExtractEval",
    "ExtractEvalCreate",
    "ExtractEvalUpdate",
    "ExtractEvalRead",
    "ExtractEvalDelete",
    "ExtractEvalSummary",
]
