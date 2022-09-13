import json


class CommentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "id": str(o.id),
                "commentOnId": o.commentOnId,
                "commentBy": o.commentBy,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
