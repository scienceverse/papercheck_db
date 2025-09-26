"""ExtractEval model - evaluation results comparing extracts with ground truth."""

from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON, Float, Boolean
from sqlalchemy.orm import relationship

from .base import BaseModel


class ExtractEval(BaseModel):
    """ExtractEval model representing evaluation results of extractors against ground truth."""

    __tablename__ = "extractevals"

    # References
    extractor_id = Column(
        Integer, ForeignKey("extractors.id"), nullable=False, index=True
    )
    ground_truth_id = Column(
        Integer, ForeignKey("ground_truths.id"), nullable=False, index=True
    )

    # Evaluation metadata
    evaluation_date = Column(String(50), nullable=True)

    # Performance metrics below

    # title
    title_exact_match = Column(
        Boolean, nullable=True
    )  # 1.0 if titles match exactly, else 0.0
    title_levenshtein_distance = Column(
        Integer, nullable=True
    )  # Edit distance between titles
    title_semantic_similarity = Column(
        Float, nullable=True
    )  # Semantic similarity score between titles
    title_length_ratio = Column(
        Float, nullable=True
    )  # Ratio of lengths between extracted and ground truth titles

    # doi
    doi_exact_match = Column(
        Boolean, nullable=True
    )  # 1.0 if DOIs match exactly, else 0.0
    doi_is_valid = Column(
        Boolean, nullable=True
    )  # 1.0 if extracted DOI is valid, else 0.0

    abstract_rouge_l = Column(
        Float, nullable=True
    )  # ROUGE-L score between extracted and ground truth abstracts
    abstract_bert_score = Column(
        Float, nullable=True
    )  # BERTScore between extracted and ground truth abstracts

    keywords_jaccard_index = Column(
        Float, nullable=True
    )  # Jaccard index between extracted and ground truth keyword sets
    keywords_f1 = Column(
        Float, nullable=True
    )  # F1 score for keyword set matching
    keywords_precision = Column(
        Float, nullable=True
    )  # Precision for keyword set matching
    keywords_recall = Column(
        Float, nullable=True
    )  # Recall for keyword set matching
    keywords_avg_jaro_winkler = Column(
        Float, nullable=True
    )  # Average Jaro-Winkler similarity for individual keywords

    # Authors, TODO add later
    # authors table in jsonb
    # authors_order_preserved = Column(
    #     Boolean, nullable=True
    # )  # 1.0 if author order is preserved, else 0.0
    
    # Author list comparison metrics, need to define exact criteria for matching tho
    # authors_f1 = Column(Float, nullable=True) # F1 score for author matching
    # authors_precision = Column(Float, nullable=True) # Precision for author matching
    # authors_recall = Column(Float, nullable=True) # Recall for author matching
    # authors_jaccard_index = Column(Float, nullable=True) # Jaccard index for author lists

    # # Averaged field-level metrics across matched authors
    # authors_avg_name_jaro_winkler = Column(Float, nullable=True) # Avg Jaro-Winkler for full names
    # authors_avg_surname_jaro_winkler = Column(Float, nullable=True) # Avg Jaro-Winkler for surnames
    # authors_avg_given_name_jaro_winkler = Column(Float, nullable=True) # Avg Jaro-Winkler for given names
    # authors_avg_affiliation_semantic_similarity = Column(Float, nullable=True) # Avg semantic similarity for affiliations
    # authors_email_match_rate = Column(Float, nullable=True) # Rate of exact email matches for matched authors

    # References, TODO add later

    # refs_f1 = Column(Float, nullable=True)  # F1 score for reference matching
    # refs_precision = Column(Float, nullable=True)  # Precision for reference matching
    # refs_recall = Column(Float, nullable=True)  # Recall for reference matching
    # refs_jaccard_index = Column(Float, nullable=True)  # Jaccard index
    # refs_avg_title_levenshtein = Column(Float, nullable=True)  # Avg Levenshtein distance for reference titles
    # refs_avg_ref_levenshtein = Column(Float, nullable=True)  # Avg Levenshtein distance for full reference strings



    # Cross-references, TODO add later
    
    
    # Evaluation context
    notes = Column(Text, nullable=True)
    evaluation_details = Column(
        JSON, nullable=True
    )  # Details on evaluation methods used

    # Relationships
    extractor = relationship("Extractor", back_populates="extract_evals")
    ground_truth = relationship("GroundTruth", back_populates="extract_evals")

    def __repr__(self):
        return f"<ExtractEval(id={self.id}, extractor_id={self.extractor_id}, ground_truth_id={self.ground_truth_id}, f1_score={self.f1_score})>"
