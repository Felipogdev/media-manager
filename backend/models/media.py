from abc import ABC, abstractmethod


class Media(ABC):
    def __init__(self, id: int, title: str):
        self._id = id
        self._title = title

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @abstractmethod
    def get_info(self) -> dict:...
