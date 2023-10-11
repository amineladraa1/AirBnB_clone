#!/usr/bin/python3
"""Console module: entry point
of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class body"""
    prompt = "(hbnb) "

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
        if line:
            if line == "BaseModel":
                new_instance = eval(line)()
                print(new_instance.id)
                storage.new(new_instance)
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        tokens = line.split()
        if len(tokens) == 2:
            cls_name, o_id = tokens
            if cls_name == "BaseModel":
                storage.reload()
                objects = storage.all()
                for key, value in objects.items():
                    if key[len(cls_name) + 1:] == o_id:
                        print(value)
                        return
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            err_msg = "** instance id missing **" if len(tokens) == 1\
                      else "** class name missing **"
            print(err_msg)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and saves the change into the JSON file"""
        tokens = line.split()
        if len(tokens) == 2:
            cls_name, o_id = tokens
            if cls_name == "BaseModel":
                storage.reload()
                objects = storage.all()
                for key in objects.keys():
                    if key[len(cls_name) + 1:] == o_id:
                        del objects[key]
                        storage.save()
                        return
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            err_msg = "** instance id missing **" if len(tokens) == 1\
                      else "** class name missing **"
            print(err_msg)

    def do_all(self, line):
        """Prints the string representation of all instances
        of a specified class"""
        if line:
            if line == "BaseModel":
                str_objs = []
                storage.reload()
                objects = storage.all()
                for key in objects.keys():
                    if key[:len(line)] == line:
                        str_objs.append(str(objects[key]))
                print(str_objs)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
