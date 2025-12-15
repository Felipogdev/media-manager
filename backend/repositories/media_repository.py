from ..models.media import Media
from ..extensions import db

class MediaRepository:

    @staticmethod
    def find_all():
        return Media.query.all()

    @staticmethod
    def save(media):
        db.session.add(media)
        db.session.commit()
        return media
