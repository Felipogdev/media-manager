from typing import override

from backend.models.media import Media

class Book(Media):
    def __init__(self,id:int, title: str, author: str, publisher: str):
        super().__init__(id, title)
        self.__author = author
        self.__publisher = publisher

    @override
    def get_info(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.__author,
            "publisher": self.__publisher
        }
