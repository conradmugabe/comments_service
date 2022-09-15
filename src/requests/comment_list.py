class CommentListRequest:
    @classmethod
    def from_dict(cls, a_dict):
        return cls()

    def __bool__(self):
        return True
