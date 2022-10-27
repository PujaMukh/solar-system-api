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
            "id": planets.id,
            "name": planets.name,
            "diameter": planets.diameter,
            "gravity": planets.gravity,
            "color": planets.color,
            "has_moon": planets.has_moon,

        }
        response. append(planet_dict)
    return jsonify(response), 200


    

