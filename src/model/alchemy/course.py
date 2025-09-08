from src.model.alchemy.base_alchemy import BaseSqlAlchemy
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime


class Course(BaseSqlAlchemy):
    __tablename__ = "courses"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    duration: Mapped[int] = mapped_column(nullable=False, default=4)
    max_grade: Mapped[int] = mapped_column(nullable=False, default=50)
    is_active: Mapped[bool] = mapped_column(
        nullable=False, default=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
