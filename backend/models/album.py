from backend.models.song import Song


class Album:
    def __init__(self, name: str, artist: str):
        self.__name = name
        self.__songs: list[Song] = []
        self.__artist = artist

    @property
    def name(self):
        return self.__name

    @property
    def artist(self):
        return self.__artist

    @property
    def songs(self):
        return self.__songs.copy()

    def add_song(self, song: Song):
        song._set_album(self)
        self.__songs.append(song)

