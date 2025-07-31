from flask import Blueprint, request, jsonify
from ..models.roommate import roommate_profiles
from ..services.matcher import find_matches

bp = Blueprint("roommates", __name__, url_prefix="/roommates")

@bp.route("/create", methods=["POST"])
def create_profile():
    data = request.get_json()
    roommate_profiles.append(data)
    return jsonify({"message": "Profile created", "profile": data}), 201

@bp.route("/matches", methods=["POST"])
def get_matches():
    user = request.get_json()
    matches = find_matches(user, roommate_profiles)
    return jsonify({"matches": matches})
