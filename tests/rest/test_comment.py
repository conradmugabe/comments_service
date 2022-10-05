from unittest import mock
from src.domain.comment import Comment

comment_dict = {
    "id": "3251a5bd-86be-428d-8ae9-6e51a8048c33",
    "commentBy": "3251a5bd-96fa-428e-8ae4-2bc1a8048c33",
    "commentOnId": "43bfa5bd-86be-7bfc-9bce-6ebda8048c33",
    "body": "this is a test comment",
}

comments = [Comment.from_dict(comment_dict)]


@mock.patch("application.rest.comment.comment_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = comments
    http_response = client.get("/api/v1/comments")
    
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
