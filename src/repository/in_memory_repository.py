from src.domain.comment import Comment
from src.repository.repository import Repository


class InMemoryRepository(Repository):
    def __init__(self, data: list[Comment]):
        self.data = data

    def getComments(self):
        return self.data

    def addComment(self, comment):
        newComment = Comment.from_dict(comment)
        self.data.append(Comment.from_dict(comment))
        return newComment

    def list(self):
        return [Comment.from_dict(i) for i in self.data]
