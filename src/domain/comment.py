import uuid
import dataclasses


@dataclasses.dataclass
class Comment:
    id: uuid.UUID
    commentOnId: str
    commentBy: str

    @classmethod
    def from_dict(cls, kwargs):
        return cls(**kwargs)

    def to_dict(self):
        return dataclasses.asdict(self)
