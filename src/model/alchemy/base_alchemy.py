from sqlalchemy.orm import DeclarativeBase
class BaseSqlAlchemy(DeclarativeBase):
    class Config:
        allow_mutation = False
        extra = "forbid"
