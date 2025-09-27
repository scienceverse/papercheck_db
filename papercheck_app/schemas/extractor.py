"""Extractor Pydantic schemas."""

from typing import Optional, Dict, Any
from datetime import date
from pydantic import Field

from .base import BaseSchema, BaseCreateSchema, BaseUpdateSchema, BaseReadSchema, BaseDeleteSchema


class ExtractorBase(BaseCreateSchema):
    """Base extractor schema with common fields."""

    # Extractor information
    extractor_type: str = Field(..., max_length=20, description="Extractor type (e.g., grobid, docling)")
    version: Optional[str] = Field(None, max_length=30, description="Extractor version")
    author: Optional[str] = Field(None, max_length=50, description="Author or organization")
    variant: Optional[str] = Field(None, max_length=50, description="Variant (e.g., delft, crf)")
    release_date: Optional[date] = Field(None, description="Release date")
    release_git_hash: Optional[str] = Field(None, max_length=64, description="Git commit hash of the release")
    description: Optional[str] = Field(None, description="Extractor description")

    # Parser information
    parser_name: Optional[str] = Field(None, max_length=100, description="Parser used (e.g., papercheck, langextract)")
    parser_version: Optional[str] = Field(None, max_length=50, description="Version of the parser")
    parser_git_hash: Optional[str] = Field(None, max_length=64, description="Git commit hash of the parser")
    parser_config: Optional[Dict[str, Any]] = Field(None, description="Configuration used for the parser")
    parser_config_hash: Optional[str] = Field(None, max_length=64, description="Hash of the parser config")

    # Configuration
    config_schema: Optional[Dict[str, Any]] = Field(None, description="Schema for configuration parameters")
    config_hash: Optional[str] = Field(None, max_length=64, description="Hash of the config schema")
    default_config: Optional[Dict[str, Any]] = Field(None, description="Default configuration")

    # Docker (where applicable)
    docker_image: Optional[str] = Field(None, max_length=255, description="Docker image name")
    docker_tag: Optional[str] = Field(None, max_length=100, description="Docker image tag/version")
    docker_digest: Optional[str] = Field(None, max_length=100, description="Docker image digest (sha256)")

    # Endpoints
    development_endpoint: Optional[str] = Field(None, max_length=255, description="URL for development endpoint")
    development_endpoint_enabled: bool = Field(False, description="Is the dev endpoint active?")
    production_endpoint: Optional[str] = Field(None, max_length=255, description="URL for production endpoint")
    production_endpoint_enabled: bool = Field(False, description="Is the prod endpoint active?")

    # Status
    is_enabled: bool = Field(True, description="Whether extractor is enabled")


class ExtractorCreate(ExtractorBase):
    """Schema for creating an extractor."""

    pass


class ExtractorUpdate(BaseUpdateSchema):
    """Schema for updating an extractor."""

    # Extractor information
    extractor_type: Optional[str] = Field(None, max_length=20)
    version: Optional[str] = Field(None, max_length=30)
    author: Optional[str] = Field(None, max_length=50)
    variant: Optional[str] = Field(None, max_length=50)
    release_date: Optional[date] = Field(None)
    release_git_hash: Optional[str] = Field(None, max_length=64)
    description: Optional[str] = Field(None)

    # Parser information
    parser_name: Optional[str] = Field(None, max_length=100)
    parser_version: Optional[str] = Field(None, max_length=50)
    parser_git_hash: Optional[str] = Field(None, max_length=64)
    parser_config: Optional[Dict[str, Any]] = Field(None)
    parser_config_hash: Optional[str] = Field(None, max_length=64)

    # Configuration
    config_schema: Optional[Dict[str, Any]] = Field(None)
    config_hash: Optional[str] = Field(None, max_length=64)
    default_config: Optional[Dict[str, Any]] = Field(None)

    # Docker
    docker_image: Optional[str] = Field(None, max_length=255)
    docker_tag: Optional[str] = Field(None, max_length=100)
    docker_digest: Optional[str] = Field(None, max_length=100)

    # Endpoints
    development_endpoint: Optional[str] = Field(None, max_length=255)
    development_endpoint_enabled: Optional[bool] = Field(None)
    production_endpoint: Optional[str] = Field(None, max_length=255)
    production_endpoint_enabled: Optional[bool] = Field(None)

    # Status
    is_enabled: Optional[bool] = Field(None)


class ExtractorRead(BaseReadSchema, ExtractorBase):
    """Schema for reading an extractor."""

    @property
    def name(self) -> str:
        """Generate a human-readable name from other fields."""
        parts = []
        
        # Add basic fields
        for field in [self.extractor_type, self.variant, self.version]:
            if field is not None:
                parts.append(str(field))
        
        # Add config hash prefixes if they exist (first 8 characters)
        if hasattr(self, 'config_hash') and self.config_hash:
            parts.append(f"c{self.config_hash[:8]}")
        
        if hasattr(self, 'parser_config_hash') and self.parser_config_hash:
            parts.append(f"p{self.parser_config_hash[:8]}")
            
        return "_".join(parts) if parts else "unnamed_extractor"


class ExtractorDelete(BaseDeleteSchema):
    """Schema for deleting an extractor."""

    pass


class ExtractorSummary(BaseReadSchema):
    """Summary schema for extractor with minimal fields."""

    extractor_type: str
    version: Optional[str] = None
    variant: Optional[str] = None
    description: Optional[str] = None
    is_enabled: bool = True
    
    @property
    def name(self) -> str:
        """Generate a human-readable name from other fields."""
        parts = []
        
        # Add basic fields
        for field in [self.extractor_type, self.variant, self.version]:
            if field is not None:
                parts.append(str(field))
        
        return "_".join(parts) if parts else "unnamed_extractor"


class Extractor(ExtractorBase, BaseSchema):
    """Complete extractor schema for responses, matching the DB model."""

    @property
    def name(self) -> str:
        """Generate a human-readable name from other fields."""
        parts = []
        
        # Add basic fields
        for field in [self.extractor_type, self.variant, self.version]:
            if field is not None:
                parts.append(str(field))
        
        # Add config hash prefixes if they exist (first 8 characters)
        if hasattr(self, 'config_hash') and self.config_hash:
            parts.append(f"c{self.config_hash[:8]}")
        
        if hasattr(self, 'parser_config_hash') and self.parser_config_hash:
            parts.append(f"p{self.parser_config_hash[:8]}")
            
        return "_".join(parts) if parts else "unnamed_extractor"
