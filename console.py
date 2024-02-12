import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all instances"""
        if arg and arg not in storage.classes():
            print("** class doesn't exist **")
            return
        objects = []
        for key, obj in storage.all().items():
            if not arg or key.split('.')[0] == arg:
                objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        try:
            attr_type = type(getattr(obj, args[2]))
            setattr(obj, args[2], attr_type(args[3]))
            obj.save()
        except AttributeError:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
