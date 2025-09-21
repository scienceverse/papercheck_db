"""Base model with common fields for all tables."""

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr

from ..core.database import Base


class BaseModel(Base):
    """Base model class with common fields."""

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False
    )

    @declared_attr
    def __tablename__(cls):
        """Generate table name from class name."""
        return cls.__name__.lower()
