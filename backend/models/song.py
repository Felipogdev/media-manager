from typing import override

from backend.models.media import Media


class Song(Media):
    def __init__(self, id: int, title: str, ):
        super().__init__(id, title)
        self.__album = None

    @property
    def album(self):
        return self.__album

    def _set_album(self, album):
        self.__album = album

    @override
    def get_info(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "album": self.__album.name if self.__album else None,
            "artist": self.__album.artist if self.__album else None,
        }





