import json
from pathlib import Path
from ..models.media import Media

DATA_PATH = Path(__file__).parent.parent / "data" / "media.json"

class MediaRepository:

    @staticmethod
    def _load_raw():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            for item in json.load(f):
                yield item

    @staticmethod
    def find_all():
        for item in MediaRepository._load_raw():
            yield Media(
                id=item.get("id"),
                title=item.get("title"),
                media_type=item.get("type")
            )

    @staticmethod
    def find_by_id(media_id: int):
        for media in MediaRepository.find_all():
            if media.id == media_id:
                return media
        return None

    @staticmethod
    def save(media: Media):
        data = list(MediaRepository._load_raw())
        media.id = max((item["id"] for item in data), default=0) + 1
        data.append({
            "id": media.id,
            "title": media.title,
            "type": media.media_type
        })
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return media
