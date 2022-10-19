from abc import ABC, abstractclassmethod
from typing import List, Union

from src.entities.comment import Comment
from src.dto.comment import CommentId, CreateComment, GetComments, UpdateComment


class Repository(ABC):
    @abstractclassmethod
    def getComments(props: GetComments) -> List[Comment]:
        pass

    @abstractclassmethod
    def createComment(props: CreateComment) -> Comment:
        pass

    @abstractclassmethod
    def getCommentById(id: CommentId) -> Union[Comment, None]:
        pass

    @abstractclassmethod
    def updateCommentById(props: UpdateComment) -> Comment:
        pass

    @abstractclassmethod
    def deleteCommentById(id: CommentId) -> None:
        pass
