#!/usr/bin/python3

"""this module contains the super class"""
import json


class Base:

    """contains a private class attribute and class constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
    
        """returns JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        
        """write JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dict = [inst.to_dictionary() for inst in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        
        """returns the list of JSON string representation"""
        if json_string is None:
            return []
        if json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        new = None
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            cls.update(new, **dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """return a list of class instantiated from a JSON file"""
        filename = str(cls.__name__) + ".json"
        new_list = []
        try:
            with open(filename, "r", encoding="utf-8") as jsonfile:
                list_dict = cls.from_json_string(jsonfile.read())
                for o in list_dict:
                    new_list.append(cls.create(**o))
        except Exception:
            pass
        return new_list
