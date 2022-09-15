from src.requests.comment_list import CommentListRequest


def test_build_comment_list_request_without_parameters():
    request = CommentListRequest()
    assert bool(request) is True


def test_build_comment_list_request_from_empty_dict():
    request = CommentListRequest.from_dict({})
    assert bool(request) is True
