#!/usr/bin/python3
""" The entry point of the command interpreter """
import cmd
import re
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel, 'User': User,
            'Amenity': Amenity, 'City': City, 'State': State,
            'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ represents the command interpreter
    """

    prompt = "(hbnb) "

    def precmd(self, line):
        """ Execute instructions before the command line 'line' is interpreted
        """
        """
        if not line:
            return '\n'
        """

    def do_quit(self, arg):
        """ Quit command to exit the program
        """

        return 1

    def do_EOF(self, arg):
        """ EOF command to catch end of a file
        """

        return 1

    def do_help(self, arg):
        """ help command to get a command information
        """

        return super().do_help(arg)

    def emptyline(self):
        """ method called when empty line is entered to the prompt
        """

        pass

    def do_create(self, arg):
        """ Creates a new instance of a class,
        saves it (to JSON file) and prints id
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            new = classes[arg[0]]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        k = "{}.{}".format(args[0], args[1])
        instance = objs[k]
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name ann id
        (save the change into the JSON file)
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        k = "{}.{}".format(args[0], args[1])
        if not objs[k]:
            print("** no instance found **")
            return
        del objs[k]
        storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        """

        if arg and arg not in classes.keys():
            print("** class doesn't exist **")
            return
        objs = storage.all()
        for instance in objs.values():
            if arg and type(instance).__name__ != arg:
                continue
            print(str(instance))

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        k = "{}.{}".format(args[0], args[1])
        if not objs[k]:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        objs[k].name = args[2]
        objs[k].my_number = int(args[3])
        storage.save()



if __name__ == '__main__':
    """ main function to run the interpreter """

    HBNBCommand().cmdloop()
