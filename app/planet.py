from flask import Blueprint, jsonify, request,abort, make_response
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, diameter, gravity, color, has_moon):
#         self.id = id
#         self.name = name
#         self.diameter = diameter
#         self.gravity = gravity 
#         self.color = color
#         self.has_moon = has_moon
# planets = [
#     Planet(1, "Mercury", 3031.9, 3.7, "slate gray", False),
#     Planet(2, "Venus", 7520.8, 8.87, "yellow-white",False),
#     Planet(3, "Earth", 7917.5, 9.807, "blue",True),
#     Planet(4, "Mars", 4212.3, 3.721, "rusty red",True),
#     Planet(5, "Jupiter", 86881, 24.79, "orangish", True),
#     Planet(6, "Saturn", 72567, 10.44, "yellow-brown", True),
#     Planet(7, "Uranus", 31518, 8.87, "blue-gren", True),
#     Planet(8, "Neptune", 30599,11.15, "blue", True)
# ]
planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")
def get_one_planet_or_abort(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response_str = f"Invalid bike_id: `{planet_id}`. ID must be an integer"
        abort(make_response(jsonify({"message":response_str}), 400))
    
    matching_planet = Planet.query.get(planet_id)

    if not matching_planet:
        response_str = f"Planet with id `{planet_id}` was not found in the database."
        abort(make_response(jsonify({"message":response_str}), 404))
    
    return matching_planet

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    name_param = request.args.get("name")

    if name_param is None:
        planets = Planet.query.all()
    else:
        planets = Planet.query.filter_by(name=name_param)
    
    response = []
    # for planet in planets:
    #     planet_dict = {
    #         "id": planet.id,
    #         "name": planet.name,
    #         "diameter": planet.diameter,
    #         "gravity": planet.gravity,
    #         "color": planet.color,
    #         "has_moon": planet.has_moon,

    #     }
    #     response. append(planet_dict)
    for planet in planets:
        response.append(planet.to_dict())
    return jsonify(response), 200

# @books_bp.route("", methods=["GET"])
# def read_all_books():
    
#     title_query = request.args.get("title")
#     if title_query:
#         books = Book.query.filter_by(title=title_query)
#     else:
#         books = Book.query.all()

#     books_response = []
#     for book in books:
#         books_response.append(book.to_dict())
#     return jsonify(books_response)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id)
    # planet_dict = {
    #         "id": planet.id,
    #         "name": planet.name,
    #         "diameter": planet.diameter,
    #         "gravity": planet.gravity,
    #         "color": planet.color,
    #         "has_moon": planet.has_moon,
    #     }

    return jsonify ({f"message": chosen_planet.to_dict()}), 400



@planets_bp.route("", methods = ["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    # Planet(
    #     name = request_body["name"],
    #     diameter = request_body["diameter"],
    #     gravity = request_body["gravity"],
    #     color = request_body["color"],
    #     has_moon = request_body["has_moon"]

    # for planet in planets:
    #     if planet.id == planet_id:
    #         planet_dict = {
    #             "id": planet.id,
    #             "name": planet.name,
    #             "diameter": planet.diameter,
    #             "gravity": planet.gravity,
    #             "color": planet.color,
    #             "has_moon": planet.has_moon,
    #         }
    #         return jsonify(planet_dict), 200

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

    
