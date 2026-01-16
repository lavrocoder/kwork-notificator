from sqlalchemy import Integer, select
from sqlalchemy.orm import mapped_column, Mapped, Session

from app.db.base import Base


class SentTask(Base):
    __tablename__ = 'sent_tasks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=False)

    @classmethod
    def add(cls, db: Session, task_id: int) -> "SentTask":
        task = cls(id=task_id)
        db.add(task)
        db.commit()
        return task

    @classmethod
    def get_all_ids(cls, db: Session) -> list[int]:
        result = db.execute(select(cls.id))
        return [row[0] for row in result.fetchall()]