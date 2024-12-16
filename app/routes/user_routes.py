from flask import Blueprint, request, jsonify

user_routes = Blueprint("user", __name__)

@user_routes.route("/users", methods=["POST"])
def create_user():
    from app.models.user import User
    from app import db

    data = request.get_json()
    new_user = User(name=data["name"], email=data["email"], username=data["username"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

@user_routes.route("/users", methods=["GET"])
def get_users():
    from app.models.user import User

    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email, "username": u.username} for u in users])

