from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from uuid import uuid4, UUID
from sqlalchemy.orm import relationship
from src.model.alchemy.base_alchemy import BaseSqlAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class CourseUser(BaseSqlAlchemy):
    __tablename__ = "course_users"
    __doc__= "Courses for Users"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    course_id: Mapped[UUID] = mapped_column(ForeignKey("courses.id"), nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)     