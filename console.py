#!/usr/bin/python3
"""Console module: entry point
of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class body"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "FileStorage", "User", "State",
               "City", "Place", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Terminates the command interpreter"""
        print()
        return True

    def emptyline(self):
        """Does nothing if user presses ENTER with an empty line"""
        return

    def do_create(self, line):
        """Creates an instance of a class and
        stores it in a file in JSON format"""
        if not line:
            print("** class name missing **")
            return
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(line)()
        print(new_instance.id)
        storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        tokens = line.split()

        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return

        key_val = f"{tokens[0]}.{tokens[1]}"

        if key_val not in storage.all().keys():
            print("** no instance found **")
            return

        print(storage.all()[key_val])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and saves the change into the JSON file"""
        if not line:
            print("** class name missing **")
            return

        tokens = line.split()

        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return

        key_val = f"{tokens[0]}.{tokens[1]}"

        if key_val not in storage.all().keys():
            print("** no instance found **")
            return

        del storage.all()[key_val]
        storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances
        of a specified class"""
        if not line:
            print([str(obj) for obj in storage.all().values()])
            return

        tokens = line.split()

        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print([str(val) for key, val in storage.all().items()
               if key[:len(tokens[0])] == tokens[0]])

    def do_update(self, line):
        """Updates the attributes of a given instance of a class"""

        tokens = line.split()

        err_msg = ["** class name missing **", "** instance id missing **",
                   "** attribute name missing **", "** value missing **"]
        for i in range(4):

            if len(tokens) == 1 and tokens[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            if len(tokens) == i:
                print(err_msg[i])
                return

        key_val = f"{tokens[0]}.{tokens[1]}"

        if key_val not in storage.all().keys():
            print("** no instance found **")
            return

        setattr(storage.all()[key_val], tokens[2], tokens[3][1:-1])
        storage.save()

    def default(self, line):
        """Triggered when the user inputs an unrecognized command"""
        tokens = line.split(".")
        if len(tokens) == 2:
            if line.endswith(".all()"):
                HBNBCommand.do_all(self, tokens[0])
                return
            elif line.endswith(".count()"):
                if tokens[0] == "count()":
                    print("** class name missing **")
                    return
                if tokens[0] in HBNBCommand.classes:
                    print(sum(1 for key in storage.all().keys()
                              if key.startswith(tokens[0])))
                    return
                else:
                    print("** class doesn't exist **")
                    return
        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
