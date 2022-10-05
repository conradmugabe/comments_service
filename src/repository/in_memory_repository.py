from src.domain.comment import Comment


class InMemoryRepository:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Comment.from_dict(i) for i in self.data]
