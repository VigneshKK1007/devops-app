from flask import Blueprint, jsonify

from routes.auth import get_current_user


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/user")
def user_profile():
    user = get_current_user()

    if user is None:
        return jsonify({"error": "Authentication required"}), 401

    return jsonify(user.to_dict())
