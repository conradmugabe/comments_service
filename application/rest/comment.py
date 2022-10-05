import json
from flask import Blueprint, Response
from src.repository.in_memory_repository import InMemoryRepository
from src.use_cases.comment_list import comment_list_use_case
from src.serializers.comment import CommentJsonEncoder

blueprint = Blueprint("comment", __name__)


@blueprint.route("/api/v1/comments", methods=["GET"])
def comment_list():
    repository = InMemoryRepository([])
    comments = comment_list_use_case(repository)

    return Response(
        json.dumps(comments, cls=CommentJsonEncoder),
        mimetype="application/json",
        status=200,
    )
