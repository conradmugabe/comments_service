import pytest
import json
import uuid
from src.serializers.comment import CommentJsonEncoder
from src.domain.comment import Comment


def test_serialize_domain_comment():
    id = uuid.uuid4()

    comment = Comment(id, "test_blog_id", "test_user_id")
    expected_json = f"""
        {{
            "id": "{id}",
            "commentOnId": "test_blog_id",
            "commentBy": "test_user_id"
        }}
    """
    json_comment = json.dumps(comment, cls=CommentJsonEncoder)
    assert json.loads(json_comment) == json.loads(expected_json)
