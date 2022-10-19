import json
import uuid
from datetime import datetime

from src.serializers.comment import CommentJsonEncoder
from src.entities.comment import Comment


def test_serialize_domain_comment():
    id = uuid.uuid4()
    iso_time = "2022-10-19T18:17:18.818543"
    timestamp = datetime.fromisoformat(iso_time)
    comment_body = "test comment"
    commentOn = "postId"
    commentBy = "userId"
    comment_dict = {
        "id": id,
        "comment": comment_body,
        "commentOn": commentOn,
        "commentBy": commentBy,
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    comment = Comment.from_dict(comment_dict)
    expected_json = f"""
        {{
            "id": "{id}",
            "comment": "{comment_body}",
            "commentOn": "{commentOn}",
            "commentBy": "{commentBy}"
        }}
    """
            # "createdAt: "{iso_time}"
            # "updatedAt: "{iso_time}",

    assert comment.id == id
    json_comment = json.dumps(comment, cls=CommentJsonEncoder)
    print(json_comment)
    assert json.loads(json_comment) == json.loads(expected_json)
