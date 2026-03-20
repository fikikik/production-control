from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.core.database import Base
from src.data.models.base import TimestampMixin


class WorkCenter(Base, TimestampMixin):
    __tablename__ = 'work_centers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    identifier: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)

    batches: Mapped[list['Batch']] = relationship(
        'Batch', back_populates='work_center', lazy='selectin'
    )
