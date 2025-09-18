"""Base Pydantic schemas with common fields."""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema with common fields."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class BaseCreateSchema(BaseModel):
    """Base schema for creating records."""

    model_config = ConfigDict(from_attributes=True)


class BaseUpdateSchema(BaseModel):
    """Base schema for updating records."""

    model_config = ConfigDict(from_attributes=True)
