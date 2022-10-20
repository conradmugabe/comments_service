import uuid
from unittest import mock
from datetime import datetime

from pytest import fixture, raises
from src.dto.comment import CreateComment, DeleteComment, UpdateComment

from src.entities.comment import Comment
from src.use_cases.use_cases import UseCases


@fixture
def comments():
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
def use_id() -> uuid.UUID:
    return uuid.uuid4()


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


@fixture
def comment_without_id(init_comment):
    comment = init_comment
    del comment["id"]
    return comment


@fixture
def comment_not_found() -> UseCases:
    repo = mock.Mock()
    repo.getCommentById.return_value = None
    use_cases = UseCases(repo)
    return use_cases


@fixture
def comment_found(init_comment):
    repo = mock.Mock()
    repo.getCommentById.return_value = Comment.from_dict(init_comment)
    use_cases = UseCases(repo)
    return use_cases


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


def test_update_comment_successful(comment_without_id, use_id):
    init_comment = comment_without_id
    init_comment["id"] = use_id
    repo = mock.Mock()
    repo.getCommentById.return_value = Comment.from_dict(init_comment)
    repo.updateCommentById.return_value = Comment.from_dict(
        {
            "id": use_id,
            "comment": "new test comment 1",
            "commentBy": "test_user_3",
            "commentOn": "test_blog_3",
            "createdAt": datetime.fromisoformat("2021-11-18T17:16:17.818543"),
            "updatedAt": datetime.fromisoformat("2021-11-18T17:16:17.818543"),
        }
    )

    request: UpdateComment = {
        "id": use_id,
        "comment": "new test comment 1",
        "commentBy": "test_user_3",
    }

    use_case = UseCases(repo)
    comment = use_case.updateComment(request)

    assert comment.id == use_id
    assert comment.commentBy == request["commentBy"]
    assert comment.comment == "new test comment 1"
    assert comment.comment != init_comment["comment"]


def test_updated_comment_raises_exception_if_comment_not_found(
    comment_not_found: UseCases,
):
    request: UpdateComment = {
        "id": use_id,
        "comment": "new test comment 1",
        "commentBy": "test_user_3",
    }
    use_cases = comment_not_found

    with raises(Exception):
        use_cases.updateComment(request)


def test_update_comment_raises_exception_if_user_not_comment_author(
    comment_found: UseCases,
):
    request: UpdateComment = {
        "id": use_id,
        "comment": "new test comment 1",
        "commentBy": "unauthorized_user",
    }
    use_cases = comment_found

    with raises(Exception):
        use_cases.updateComment(request)


def test_delete_comment_successful():
    pass


def test_delete_comment_raises_exception_if_comment_not_found(
    use_id: uuid.UUID,
    comment_not_found: UseCases,
):
    request: DeleteComment = {"id": use_id, "commentBy": use_id}
    use_cases = comment_not_found

    with raises(Exception):
        use_cases.deleteComment(request)


def test_delete_comment_raises_exception_if_user_not_comment_author(
    comment_found: UseCases,
):
    request: DeleteComment = {
        "id": use_id,
        "commentBy": "unauthorized_user",
    }
    use_cases = comment_found

    with raises(Exception):
        use_cases.deleteComment(request)
