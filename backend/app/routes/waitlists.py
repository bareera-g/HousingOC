from flask import Blueprint, jsonify

bp = Blueprint("waitlists", __name__, url_prefix="/waitlists")

waitlist_data = [
    {"city": "Santa Ana", "status": "open", "deadline": "2025-08-15"},
    {"city": "Anaheim", "status": "closed", "deadline": None}
]

@bp.route("/", methods=["GET"])
def get_waitlists():
    return jsonify(waitlist_data)
