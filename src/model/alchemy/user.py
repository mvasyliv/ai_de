from src.model.alchemy.base_alchemy import BaseSqlAlchemy
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing_extensions import Optional
class User(BaseSqlAlchemy):
    __tablename__ = 'users'
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(75), unique=True, index=True, nullable=False)
    mobile: Mapped[str] = mapped_column(String(15), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        nullable=False, default=True
    )
    nick_name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now
    )


