from flask import Blueprint, jsonify, request

bp = Blueprint("media", __name__)

@bp.route("/media", methods=["GET"])
def get_media():
    return jsonify([{"id": 1, "name": "Movie A"}])

@bp.route("/media", methods=["POST"])
def add_media():
    data = request.json
    return jsonify({"status": "success", "item": data}), 201
