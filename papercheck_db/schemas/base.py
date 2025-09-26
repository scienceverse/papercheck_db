"""Base Pydantic schemas with common fields."""

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """Base schema with common configuration."""

    model_config = ConfigDict(from_attributes=True)


class BaseCreateSchema(BaseSchema):
    """Base schema for creating records."""

    pass


class BaseUpdateSchema(BaseSchema):
    """Base schema for updating records, all fields are optional."""

    pass


class BaseReadSchema(BaseSchema):
    """Base schema for reading records, includes database-generated fields."""

    id: int
    created_at: datetime
    updated_at: datetime


class BaseDeleteSchema(BaseSchema):
    """Base schema for deleting records."""

    id: int
