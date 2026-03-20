from datetime import datetime, date
from sqlalchemy import (String, Integer, Boolean, Date,
                        DateTime, ForeignKey, UniqueConstraint, Index)
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.core.database import Base
from src.data.models.base import TimestampMixin


class Batch(Base, TimestampMixin):
    __tablename__ = 'batches'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    is_closed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    task_description: Mapped[str] = mapped_column(String(1000), nullable=False)

    work_center_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('work_centers.id', ondelete='RESTRICT'), nullable=False
    )
    shift: Mapped[str] = mapped_column(String(50), nullable=False)
    team: Mapped[str] = mapped_column(String(200), nullable=False)

    batch_number: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    batch_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    nomenclature: Mapped[str] = mapped_column(String(500), nullable=False)
    ekn_code: Mapped[str] = mapped_column(String(100), nullable=False)

    shift_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    shift_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    work_center: Mapped['WorkCenter'] = relationship('WorkCenter', back_populates='batches')
    products: Mapped[list['Product']] = relationship(
        'Product', back_populates='batch', lazy='selectin', cascade='all, delete-orphan'
    )

    __table_args__ = (
        UniqueConstraint('batch_number', 'batch_date', name='uq_batch_number_date'),
        Index('idx_batch_closed', 'is_closed'),
        Index('idx_batch_shift_times', 'shift_start', 'shift_end'),
    )
