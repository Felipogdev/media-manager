from ..repositories.media_repository import MediaRepository
from ..models.media import Media

class MediaService:

    @staticmethod
    def list_media():
        return MediaRepository.find_all()

    @staticmethod
    def create_media(title, media_type):
        if not title:
            raise ValueError("Title is required")
        media = Media(id=None, title=title, media_type=media_type)
        return MediaRepository.save(media)
