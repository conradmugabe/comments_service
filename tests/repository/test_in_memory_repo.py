import pytest
from src.domain.comment import Comment
from src.repository.in_memory_repository import InMemoryRepository


@pytest.fixture
def comment_dicts():
    return [
        {
            "id": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "commentOnId": "f853578c-329a-4e65-81b8-566c5dffa35b",
            "commentBy": "f853578c-fc0f-4e65-61bf-743c5dffa35d",
            "body": "test comment 1",
        },
        {
            "id": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "commentOnId": "fe2c3196-aedd-487a-a08f-e0bdc0ec6e9a",
            "commentBy": "fe2d3195-3e11-487a-a0ad-e0bdc0ec8b2c",
            "body": "test comment 1",
        },
        {
            "id": "913694c6-435a-4366-ba0d-da5334a611b2",
            "commentOnId": "913694c6-435a-4366-ba0d-da5334a611b2",
            "commentBy": "913694c6-435a-4366-ba0d-da5334a611b2",
            "body": "test comment 1",
        },
        {
            "id": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "commentOnId": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "commentBy": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "body": "test comment 1",
        },
    ]


def test_repository_list_without_parameters(comment_dicts):
    repo = InMemoryRepository(comment_dicts)

    comments = [Comment.from_dict(i) for i in comment_dicts]

    assert repo.list() == comments
