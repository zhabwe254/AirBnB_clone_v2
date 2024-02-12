import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objs = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objs = json.load(file)
                for key, value in objs.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        obj = User(**value)
                    elif class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    else:
                        obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
