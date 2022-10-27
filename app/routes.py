from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, diameter, gravity, color, has_moon):
        self.id = id
        self.name = name
        self.diameter = diameter
        self.gravity = gravity 
        self.color = color
        self.has_moon = has_moon

planets = [
    Planet(1, "Mercury", 3031.9, 3.7, "slate gray", False),
    Planet(2, "Venus", 7520.8, 8.87, "yellow-white",False),
    Planet(3, "Earth", 7917.5, 9.807, "blue",True),
    Planet(4, "Mars", 4212.3, 3.721, "rusty red",True),
    Planet(5, "Jupiter", 86881, 24.79, "orangish", True),
    Planet(6, "Saturn", 72567, 10.44, "yellow-brown", True),
    Planet(7, "Uranus", 31518, 8.87, "blue-gren", True),
    Planet(8, "Neptune", 30599,11.15, "blue", True)
]
planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "diameter": planet.diameter,
            "gravity": planet.gravity,
            "color": planet.color,
            "has_moon": planet.has_moon,

        }
        response. append(planet_dict)
    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response_str = "Invalid planet id"
        return jsonify({"message": response_str}), 400

    for planet in planets:
        if planet.id == planet_id:
            planet_dict = {
                "id": planet.id,
                "name": planet.name,
                "diameter": planet.diameter,
                "gravity": planet.gravity,
                "color": planet.color,
                "has_moon": planet.has_moon,
            }
            return jsonify(planet_dict), 200

    response_message = "Could not find the planet id"
    return jsonify({"message": response_message}), 400






