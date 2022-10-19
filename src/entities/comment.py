import uuid
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class Comment:
    id: uuid.UUID
    comment: str
    commentOn: str
    commentBy: str
    createdAt: datetime
    updatedAt: datetime

    @classmethod
    def from_dict(cls, kwargs):
        return cls(**kwargs)

    def to_dict(self):
        return asdict(self)
