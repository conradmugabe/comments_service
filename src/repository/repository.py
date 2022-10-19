from abc import ABC, abstractclassmethod
from typing import List

from src.domain.comment import Comment


class Repository(ABC):
    @abstractclassmethod
    def getComments() -> List[Comment]:
        pass

    @abstractclassmethod
    def addComment() -> Comment:
        pass
