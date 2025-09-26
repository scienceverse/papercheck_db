"""Extractor model - extraction tools and methods."""

from sqlalchemy import Column, String, Text, Date, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import JSONB
import re


from .base import BaseModel


class Extractor(BaseModel):
    """Extractor model representing extraction tools and methods."""

    __tablename__ = "extractors"

    __table_args__ = (
        UniqueConstraint('extractor_type', 'version', 'variant', 'config_hash', 'parser_config_hash', 
                        name='_extractor_version_variant_config_uc'),
    )

    # Extractor information
    extractor_type = Column(String(20), nullable=False, index=True) # grobid, docling
    version = Column(String(30), nullable=True) # 0.8.3-SNAPSHOT
    author = Column(String(50), nullable=True)  # Author or organization
    variant = Column(String(50), nullable=True) # delft, crf... where applicable
    release_date = Column(Date, nullable=True) # YYYY-MM-DD
    release_git_hash = Column(String(64), nullable=True)  # Git commit hash of the release
    description = Column(Text, nullable=True)

    # Parser information
    parser_name = Column(String(100), nullable=True)  # parser used (papercheck, langextract...)
    parser_version = Column(String(50), nullable=True)  # version of the parser
    parser_git_hash = Column(String(64), nullable=True)  # Git commit hash of the parser
    parser_config = Column(JSONB, nullable=True)  # Configuration used for the parser
    parser_config_hash = Column(String(64), nullable=True, index=True)  # Hash of the parser config

    # Configuration
    config_schema = Column(JSONB, nullable=True)  # Schema for configuration parameters
    config_hash = Column(String(64), nullable=True, index=True)  # Hash of the config schema
    default_config = Column(JSONB, nullable=True)  # Default configuration

    # docker (where applicable)
    docker_image = Column(String(255), nullable=True)  # Docker image name
    docker_tag = Column(String(100), nullable=True)  # Docker image tag/version
    docker_digest = Column(String(100), nullable=True)  # Docker image digest (sha256)

    # Status and metadata
    is_enabled = Column(Boolean, default=True, nullable=False)

    @property
    def name(self):
        """Generate a human-readable name from other fields."""
        parts = []
        
        # Add basic fields
        for field in [self.extractor_type, self.variant, self.version]:
            if field is not None:
                parts.append(str(field))
        
        # Add config hash prefixes if they exist (first 8 characters)
        config_hash_val = getattr(self, 'config_hash', None)
        if config_hash_val:
            parts.append(f"c{config_hash_val[:8]}")
        
        parser_config_hash_val = getattr(self, 'parser_config_hash', None)
        if parser_config_hash_val:
            parts.append(f"p{parser_config_hash_val[:8]}")
            
        return "_".join(parts)

    @validates('development_endpoint', 'production_endpoint')
    def validate_endpoint_url(self, key, value):
        """Validate endpoint URLs."""
        if value is not None:
            # Basic URL validation
            url_pattern = re.compile(
                r'^https?://'  # http:// or https://
                r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)*'  # domain
                r'[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?'  # host
                r'(?::\d+)?'  # optional port
                r'(?:/.*)?$', re.IGNORECASE)  # optional path
            
            if not url_pattern.match(value):
                raise ValueError(f"Invalid URL format for {key}: {value}")
        return value

    @validates('release_git_hash', 'parser_git_hash')
    def validate_git_hash(self, key, value):
        """Validate git hash format (40 hex characters)."""
        if value is not None:
            if not re.match(r'^[a-fA-F0-9]{40}$', value):
                raise ValueError(f"Invalid git hash format for {key}: {value}. Must be 40 hexadecimal characters.")
        return value

    @validates('docker_image')
    def validate_docker_image(self, key, value):
        """Validate docker image name format."""
        if value is not None:
            # Basic docker image name validation
            # Allows: registry.com/namespace/image or namespace/image or image
            docker_pattern = re.compile(
                r'^(?:[a-zA-Z0-9.-]+(?::[0-9]+)?/)?'  # optional registry and port
                r'(?:[a-zA-Z0-9._-]+/)*'  # optional namespace(s)
                r'[a-zA-Z0-9._-]+$'  # image name
            )
            if not docker_pattern.match(value):
                raise ValueError(f"Invalid docker image name format for {key}: {value}")
        return value

    @validates('config_hash', 'parser_config_hash')
    def validate_hash(self, key, value):
        """Validate hash format (64 hex characters for SHA-256)."""
        if value is not None:
            if not re.match(r'^[a-fA-F0-9]{64}$', value):
                raise ValueError(f"Invalid hash format for {key}: {value}. Must be 64 hexadecimal characters.")
        return value

    # endpoints, might later abstract this into a separate table
    development_endpoint = Column(String(255), nullable=True)  # URL for development endpoint
    development_endpoint_enabled = Column(Boolean, default=False, nullable=False)  # Is the dev endpoint active?
    production_endpoint = Column(String(255), nullable=True)  # URL for production endpoint
    production_endpoint_enabled = Column(Boolean, default=False, nullable=False)  # Is the prod endpoint active?
    
    # Relationships
    extracts = relationship(
        "Extract", back_populates="extractor", cascade="all, delete-orphan"
    )
    extract_evals = relationship(
        "ExtractEval", back_populates="extractor", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Extractor(id={self.id}, name='{self.name}', type='{self.extractor_type}')>"
