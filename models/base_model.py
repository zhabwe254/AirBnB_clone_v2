""" Module for BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
<<<<<<< HEAD
        """ Return the print/str representation of an instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
=======
        """Returns a human-readable string representation
        of an instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87

    def save(self):
        """ Update the updated_at attribute and save the instance """
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.save()
=======
        storage.save()
        storage.new(self)
>>>>>>> 4b4e94bc6446dad7559491f6d66e681e2b57fc87

    def to_dict(self):
        """ Return a dictionary representation of an instance """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
