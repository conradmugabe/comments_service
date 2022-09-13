import uuid
from src.domain.comment import Comment


def test_room_model_init():
    id = uuid.uuid4()
    commentOnId = "test_blog_id"
    commentBy = "test_user_id"

    comment = Comment(id, commentOnId, commentBy)

    assert comment.commentOnId == commentOnId
    assert comment.commentBy == commentBy
    assert comment.id == id


def test_comment_model_from_dict():
    id = uuid.uuid4()
    init_dict = {"id": id, "commentOnId": "test_blog_id", "commentBy": "test_user_id"}

    comment = Comment.from_dict(init_dict)

    assert comment.commentBy == "test_user_id"
    assert comment.commentOnId == "test_blog_id"
    assert comment.id == id
