from datetime import datetime
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, Index
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.core.database import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    unique_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)

    batch_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('batches.id', ondelete='CASCADE'), nullable=False, index=True
    )

    is_aggregated: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    aggregated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    batch: Mapped['Batch'] = relationship('Batch', back_populates='products')

    __table_args__ = (
        Index('idx_product_batch_aggregated', 'batch_id', 'is_aggregated'),
    )
