from models import Favorite, User, session as Session
from models import Character, Item, Planet, Starship

class BDManagement:
    @staticmethod
    def get_item_list():
        query = Session.query(Item).all()
        response = [item.serialize() for item in query]
        return response

    @staticmethod
    def get_item_by_id(item_id):
        query = Session.query(Item).filter(Item.id == int(item_id)).first()
        if query:
            return query.serialize()
        else:
            return None

    @staticmethod
    def add_new_item(item):
        item_type = Item.get_enum_type(item["type"])
        new_item = Item(
            name=item["name"],
            description=item["description"],
            img=item["img"],
            type=item_type
        )
        Session.add(new_item)
        Session.commit()
        return new_item.serialize()

    @staticmethod
    def get_character_list():
        characters = Session.query(Character).all()
        response = [character.serialize() for character in characters]
        return response

    @staticmethod
    def get_character_by_id(character_id):
        query = Session.query(Character).filter(Character.id == int(character_id)).first()
        if query:
            return query.serialize()
        else:
            return None

    @staticmethod
    def get_planet_list():
        planets = Session.query(Planet).all()
        response = [planet.serialize() for planet in planets]
        return response

    @staticmethod
    def get_planet_by_id(planet_id):
        query = Session.query(Planet).filter(Planet.id == str(planet_id)).first()
        if query:
            return query.serialize()
        else:
            return None

    @staticmethod
    def get_starship_list():
        starships = Session.query(Starship).all()
        response = [starship.serialize() for starship in starships]
        return response

    @staticmethod
    def get_starship_by_id(starship_id):
        query = Session.query(Starship).filter(Starship.id == str(starship_id)).first()
        if query:
            return query.serialize()
        else:
            return None

    @staticmethod
    def get_user_list():
        users = Session.query(User).all()
        response = [user.serialize() for user in users]
        return response

    @staticmethod
    def get_user_by_id(user_id):
        query = Session.query(User).filter(User.id == user_id).first()
        if query:
            return query.serialize()
        else:
            return None

    @staticmethod
    def get_user_favorites(user_id):
        favorites = Session.query(Favorite).filter(Favorite.user_id == user_id).all()
        response = [favorite.serialize() for favorite in favorites]
        return response

    @staticmethod
    def add_user_favorite(favorite_info):
        new_favourite = Favorite(
            user_id=favorite_info["user_id"],
            item_id=favorite_info["item_id"]
        )
        Session.add(new_favourite)
        Session.commit()
        return new_favourite.serialize()