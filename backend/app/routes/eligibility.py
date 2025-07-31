from flask import Blueprint, request, jsonify

bp = Blueprint("eligibility", __name__, url_prefix="/eligibility")

@bp.route("/check", methods=["POST"])
def check_eligibility():
    data = request.get_json()
    income = data.get("income")
    household_size = data.get("household_size")

    threshold = 30000 + (household_size - 1) * 5000
    eligible = income <= threshold

    return jsonify({"eligible": eligible, "threshold": threshold})
