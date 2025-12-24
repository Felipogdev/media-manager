from flask import Blueprint, jsonify, request
from ..services.media_service import MediaService

bp = Blueprint("media", __name__, url_prefix="/media")

@bp.route("/", methods=["GET"])
def list_media():
    media = MediaService.list_media()
    return jsonify([
        {"id": m.id, "title": m.title, "media_type": m.media_type}
        for m in media
    ])

@bp.route("/", methods=["POST"])
def create_media():
    data = request.json
    media = MediaService.create_media(data["title"], data["type"])
    return jsonify({"id": media.id}), 201
