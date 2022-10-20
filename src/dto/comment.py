from typing import TypedDict


CommentId = str
Comment = str
CommentBy = str
CommentOn = str


class CreateComment(TypedDict):
    comment: Comment
    commentBy: CommentBy
    commentOn: CommentOn


class UpdateComment(TypedDict):
    id: CommentId
    commentBy: CommentBy
    comment: Comment


class DeleteComment(TypedDict):
    id: CommentId
    commentBy: CommentBy


class GetComments(TypedDict):
    commentOn: CommentOn
