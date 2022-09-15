import uuid
import pytest
import uuid
from unittest import mock

from src.domain.comment import Comment
from src.use_cases.comment_list import comment_list_use_case
from src.requests.comment_list import CommentListRequest


@pytest.fixture
def domain_comments():
    comment1 = Comment(
        id=uuid.uuid4(),
        commentOnId="test_blog_1",
        commentBy="test_user_1",
        body="test comment 1",
    )
    comment2 = Comment(
        id=uuid.uuid4(),
        commentOnId="test_blog_2",
        commentBy="test_user_2",
        body="test comment 1",
    )
    comment3 = Comment(
        id=uuid.uuid4(),
        commentOnId="test_blog_3",
        commentBy="test_user_3",
        body="test comment 1",
    )
    comment4 = Comment(
        id=uuid.uuid4(),
        commentOnId="test_blog_4",
        commentBy="test_user_4",
        body="test comment 1",
    )
    return [comment1, comment2, comment3, comment4]


def test_comment_list_without_parameters(domain_comments):
    repo = mock.Mock()
    repo.list.return_value = domain_comments

    request = CommentListRequest()
    response = comment_list_use_case(repo, request)

    repo.list.assert_called_with()
    assert response == domain_comments
