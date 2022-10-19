from src.repository.repository import Repository


class UseCases:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def listComments(self):
        self.repository.getComments()
