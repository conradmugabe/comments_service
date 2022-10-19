import uuid
from datetime import datetime

from src.entities.comment import Comment


def test_comment_entity_init():
    id = uuid.uuid4()
    timestamp = datetime.fromisoformat("2022-10-19T18:17:18.818543")
    comment_body = "test comment"
    commentOn = "postId"
    commentBy = "userId"
    createdAt = timestamp
    updatedAt = timestamp

    comment = Comment(
        id,
        comment_body,
        commentOn,
        commentBy,
        createdAt,
        updatedAt,
    )

    assert comment.id == id
    assert comment.comment == comment_body
    assert comment.commentOn == commentOn
    assert comment.commentBy == commentBy
    assert comment.createdAt == createdAt
    assert comment.updatedAt == updatedAt


def test_comment_entity_from_dict():
    id = uuid.uuid4()
    timestamp = datetime.fromisoformat("2022-10-19T18:17:18.818543")
    comment_dict = {
        "id": id,
        "comment": "test comment",
        "commentOn": "postId",
        "commentBy": "userId",
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    comment = Comment.from_dict(comment_dict)

    assert comment.id == id
    assert comment.comment == "test comment"
    assert comment.commentOn == "postId"
    assert comment.commentBy == "userId"
    assert comment.createdAt == timestamp
    assert comment.updatedAt == timestamp


def test_comment_to_dict():
    id = uuid.uuid4()
    timestamp = datetime.fromisoformat("2022-10-19T18:17:18.818543")
    comment_dict = {
        "id": id,
        "comment": "test comment",
        "commentOn": "postId",
        "commentBy": "userId",
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    comment = Comment.from_dict(comment_dict)

    assert comment.to_dict() == comment_dict


def test_comment_comparison_match():
    id = uuid.uuid4()
    timestamp = datetime.fromisoformat("2022-10-19T18:17:18.818543")
    comment_dict = {
        "id": id,
        "comment": "test comment",
        "commentOn": "postId",
        "commentBy": "userId",
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    comment1 = Comment.from_dict(comment_dict)
    comment2 = Comment.from_dict(comment_dict)

    assert comment1 == comment2


def test_comment_comparison_mismatch():
    id = uuid.uuid4()
    timestamp = datetime.fromisoformat("2022-10-19T18:17:18.818543")
    comment_dict = {
        "id": id,
        "comment": "test comment",
        "commentOn": "postId",
        "commentBy": "userId",
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    id_1 = uuid.uuid4()
    timestamp_1 = datetime.fromisoformat("2021-11-18T17:16:17.818543")
    comment_dict_1 = {
        "id": id_1,
        "comment": "test comment 1",
        "commentOn": "postId1",
        "commentBy": "userId1",
        "createdAt": timestamp_1,
        "updatedAt": timestamp_1,
    }

    comment1 = Comment.from_dict(comment_dict)
    comment2 = Comment.from_dict(comment_dict_1)

    assert comment1 != comment2
