import uuid
from unittest import mock
from datetime import datetime

from pytest import fixture
from src.dto.comment import CreateComment

from src.entities.comment import Comment
from src.use_cases.use_cases import UseCases


@fixture
def comments():
    iso = "2021-11-18T17:16:17.818543"
    comment1 = Comment(
        id=uuid.uuid4(),
        comment="test comment 1",
        commentOn="test_blog_1",
        commentBy="test_user_1",
        createdAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        updatedAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
    )
    comment2 = Comment(
        id=uuid.uuid4(),
        comment="test comment 1",
        commentOn="test_blog_2",
        commentBy="test_user_2",
        createdAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        updatedAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
    )
    comment3 = Comment(
        id=uuid.uuid4(),
        comment="test comment 1",
        commentOn="test_blog_3",
        commentBy="test_user_3",
        createdAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        updatedAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
    )
    comment4 = Comment(
        id=uuid.uuid4(),
        comment="test comment 1",
        commentOn="test_blog_4",
        commentBy="test_user_4",
        createdAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        updatedAt=datetime.fromisoformat("2021-11-18T17:16:17.818543"),
    )
    return [comment1, comment2, comment3, comment4]


@fixture
def init_comment():
    return {
        "id": uuid.uuid4(),
        "comment": "test comment 1",
        "commentOn": "test_blog_3",
        "commentBy": "test_user_3",
        "createdAt": datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        "updatedAt": datetime.fromisoformat("2021-11-18T17:16:17.818543"),
    }


def test_add_comment(init_comment):
    repo = mock.Mock()
    repo.createComment.return_value = Comment.from_dict(init_comment)

    request: CreateComment = {
        "comment": "test comment 1",
        "commentOn": "test_blog_3",
        "commentBy": "test_user_3",
    }

    use_case = UseCases(repo)
    comment = use_case.addComment(request)

    assert repo.createComment.assert_called_once
    assert comment.id == init_comment.get("id")
    assert comment.comment == init_comment.get("comment")
    assert comment.commentOn == init_comment.get("commentOn")
    assert comment.commentBy == init_comment.get("commentBy")
    assert comment.createdAt == init_comment.get("createdAt")
    assert comment.updatedAt == init_comment.get("updatedAt")
