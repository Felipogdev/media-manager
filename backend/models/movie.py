from typing import override

from backend.models.media import Media


class Movie(Media):
    def __init__(self, id: int, title: str, director:str, duration_minutes:int):
        super().__init__(id, title)
        self.__director = director
        self.__duration_minutes = duration_minutes

    @override
    def get_info(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "director": self.__director,
            "duration_minutes": self.__duration_minutes,
        }

