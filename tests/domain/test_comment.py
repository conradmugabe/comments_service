import uuid
from src.domain.comment import Comment


def test_comment_model_init():
    id = uuid.uuid4()
    commentOnId = "test_blog_id"
    commentBy = "test_user_id"
    body = "test comment 1"

    comment = Comment(id, commentOnId, commentBy, body)

    assert comment.commentOnId == commentOnId
    assert comment.commentBy == commentBy
    assert comment.body == body
    assert comment.id == id


def test_comment_model_from_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "commentOnId": "test_blog_id",
        "commentBy": "test_user_id",
        "body": "test comment 1",
    }

    comment = Comment.from_dict(init_dict)

    assert comment.commentBy == "test_user_id"
    assert comment.commentOnId == "test_blog_id"
    assert comment.body == "test comment 1"
    assert comment.id == id


def test_comment_to_dict():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "commentOnId": "test_blog_id",
        "commentBy": "test_user_id",
        "body": "test comment 1",
    }

    comment = Comment.from_dict(init_dict)

    assert comment.to_dict() == init_dict


def test_comment_model_comparison_match():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "commentOnId": "test_blog_id",
        "commentBy": "test_user_id",
        "body": "test comment 1",
    }

    comment1 = Comment.from_dict(init_dict)
    comment2 = Comment.from_dict(init_dict)

    assert comment1 == comment2


def test_comment_model_comparison_mismatch():
    id = uuid.uuid4()
    init_dict = {
        "id": id,
        "commentOnId": "test_blog_id",
        "commentBy": "test_user_id",
        "body": "test comment",
    }

    id = uuid.uuid4()
    init_dict_1 = {
        "id": id,
        "commentOnId": "test_blog_id_1",
        "commentBy": "test_user_id_1",
        "body": "test comment 1",
    }

    comment1 = Comment.from_dict(init_dict)
    comment2 = Comment.from_dict(init_dict_1)

    assert comment1 != comment2
