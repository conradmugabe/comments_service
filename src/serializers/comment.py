import json

from src.entities.comment import Comment


class CommentJsonEncoder(json.JSONEncoder):
    def default(self, o: Comment):
        try:
            to_serialize = {
                "id": str(o.id),
                "comment": o.comment,
                "commentOn": o.commentOn,
                "commentBy": o.commentBy,
                # "createdAt": o.createdAt.isoformat(),
                # "updatedAt": o.updatedAt.isoformat(),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
