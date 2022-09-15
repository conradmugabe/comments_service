from src.responses import ResponseSuccess


def comment_list_use_case(repo, request):
    comments = repo.list()
    return comments
