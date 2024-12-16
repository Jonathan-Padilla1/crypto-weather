from flask import Blueprint
from app.controllers.main_controller import hello_world, johnny_function

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET"])
def home():
    return hello_world()


@main_routes.route("/johnny", methods=["GET"])
def johnny_page():
    return johnny_function()
