from src.entities.comment import Comment
from src.repository.repository import Repository
from src.dto.comment import (
    CommentBy,
    CommentId,
    CreateComment,
    DeleteComment,
    GetComments,
    UpdateComment,
)


class UseCases:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def listComments(self, props: GetComments):
        return self.repository.getComments(props)

    def addComment(self, props: CreateComment):
        return self.repository.createComment(props)

    def updateComment(self, props: UpdateComment):
        commentId, commentBy = props["id"], props["commentBy"]
        comment = self.__getCommentById(commentId)
        self.__isCommentAuthor(comment, commentBy)
        return self.repository.updateCommentById(props)

    def deleteComment(self, props: DeleteComment):
        commentId, commentBy = props["id"], props["commentBy"]
        comment = self.__getCommentById(commentId)
        self.__isCommentAuthor(comment, commentBy)
        return self.repository.deleteCommentById(commentId)

    def getCommentById(self, id: CommentId):
        return self.__getCommentById(id)

    def __getCommentById(self, id: CommentId):
        comment = self.repository.getCommentById(id)
        if comment is None:
            raise Exception("No comment with given Id found")
        return comment

    @staticmethod
    def __isCommentAuthor(comment: Comment, id: CommentBy):
        if comment.commentBy == id:
            return True
        raise Exception("403! you don't have the permission to update this resource")
