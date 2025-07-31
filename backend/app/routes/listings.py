from flask import Blueprint, jsonify

bp = Blueprint("listings", __name__, url_prefix="/listings")

# Sample static listing (replace with DB or API later)
listings_data = [
    {"id": 1, "address": "123 Main St, Santa Ana", "rent": 850, "zip": "92701", "program": "Section 8"},
    {"id": 2, "address": "456 Orange Ave, Anaheim", "rent": 900, "zip": "92801", "program": "Income Restricted"}
]

@bp.route("/", methods=["GET"])
def get_listings():
    return jsonify(listings_data)
