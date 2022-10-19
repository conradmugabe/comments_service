from typing import TypedDict


CommentId = str
Comment = str
CommentBy = str
CommentOn = str


class CreateComment(TypedDict):
    comment: Comment
    commentBy: CommentBy
    commentOn: CommentOn


class UpdateComment(CreateComment, TypedDict):
    id: CommentId


class DeleteComment(TypedDict):
    id: CommentId
    commentBy: CommentBy


class GetComments(TypedDict):
    commentOn: CommentOn
