"""ExtractorEval model - evaluation results comparing extracts with ground truth."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship

from .base import BaseModel


class ExtractorEval(BaseModel):
    """ExtractorEval model representing evaluation results of extractors against ground truth."""

    __tablename__ = "extractorevals"

    # References
    extractor_id = Column(
        Integer, ForeignKey("extractors.id"), nullable=False, index=True
    )
    canon_id = Column(Integer, ForeignKey("canons.id"), nullable=False, index=True)

    # Evaluation metadata
    evaluation_date = Column(String(50), nullable=True)
    evaluator = Column(String(255), nullable=True)
    evaluation_method = Column(
        String(100), nullable=True
    )  # e.g., "manual", "automated", "hybrid"

    # Performance metrics
    accuracy = Column(Float, nullable=True)
    precision = Column(Float, nullable=True)
    recall = Column(Float, nullable=True)
    f1_score = Column(Float, nullable=True)

    # Detailed evaluation results
    field_level_scores = Column(JSON, nullable=True)  # Per-field performance metrics
    confusion_matrix = Column(JSON, nullable=True)
    detailed_results = Column(JSON, nullable=True)  # Detailed comparison results

    # Qualitative assessment
    overall_rating = Column(
        String(50), nullable=True
    )  # e.g., "excellent", "good", "fair", "poor"
    strengths = Column(Text, nullable=True)
    weaknesses = Column(Text, nullable=True)
    recommendations = Column(Text, nullable=True)

    # Evaluation context
    evaluation_criteria = Column(JSON, nullable=True)  # Criteria used for evaluation
    notes = Column(Text, nullable=True)

    # Relationships
    extractor = relationship("Extractor", back_populates="extractor_evals")
    canon = relationship("Canon", back_populates="extractor_evals")

    def __repr__(self):
        return f"<ExtractorEval(id={self.id}, extractor_id={self.extractor_id}, canon_id={self.canon_id}, f1_score={self.f1_score})>"
