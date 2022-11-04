from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Float)
    color = db.Column(db.String)
    has_moon = db.Column(db.Boolean)

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["diameter"] = self.diameter
        planet_as_dict["gravity"] = self.gravity
        planet_as_dict["color"] = self.color
        planet_as_dict["has_moon"] = self.has_moon

        return planet_as_dict

    @classmethod
    def from_dict(cls,data_dict):
        # check if data_dict has all valid attributes
        if "name" in data_dict and "diameter" in data_dict and "gravity" in data_dict and "color" in data_dict and "has_moon" in data_dict:
            new_obj= cls(name=data_dict["name"],diameter=data_dict["diameter"],
            gravity=data_dict["gravity"],
            color=data_dict["color"],
            has_moon=data_dict["has_moon"],)

            return new_obj