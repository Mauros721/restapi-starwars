from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enum import Enum

db = SQLAlchemy()

class ItemType(Enum):
    CHARACTER = "Character"
    PLANET = "Planet"
    STARSHIP = "Starship"
    NULL = None

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    type = db.Column(db.Enum(ItemType), nullable=False)

    characters = db.relationship("Character", back_populates="items")
    planets = db.relationship("Planet", back_populates="items")
    starships = db.relationship("Starship", back_populates="items")
    favorites = db.relationship("Favorite", back_populates="items")

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, type={self.type})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "img": self.img,
            "description": self.description,
            "type": self.type.value,
        }

    @staticmethod
    def get_enum_type(type_str):
        for item_type in ItemType:
            if item_type.value == type_str:
                return item_type
        return ItemType.NULL

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)
    homeworld = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="characters")

    def __repr__(self):
        return f"<Character(id={self.id}, name={self.items.name})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.items.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "homeworld": self.homeworld,
        }

class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)
    diameter = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    surface_water = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="planets")

    def __repr__(self):
        return f"<Planet(id={self.id}, name={self.items.name})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.items.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
        }

class Starship(db.Model):
    __tablename__ = "starships"
    id = db.Column(db.Integer, db.ForeignKey("items.id"), primary_key=True)
    model = db.Column(db.String, nullable=False)
    starship_class = db.Column(db.String, nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphere_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.String, nullable=False)
    MGLT = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="starships")

    def __repr__(self):
        return f"<Starship(id={self.id}, name={self.items.name})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.items.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphere_speed": self.max_atmosphere_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "created": self.created,
            "edited": self.edited,
        }

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    items = db.relationship("Item", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite(id={self.id}, item_id={self.item_id})>"

    def serialize(self):
        return {
            "id": self.item_id,
            "name": self.items.name,
            "description": self.items.description,
            "img": self.items.img,
            "type": self.items.type.value
        }


engine = create_engine("postgresql://gitpod:postgres@localhost:5432/example")
db.Model.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()