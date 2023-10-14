#!/usr/bin/python3
""" The entry point of the command interpreter """
import cmd
import re
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


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
        if not line:
            return '\n'
        regex = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        matches = regex.findall(line)
        if not matches:
            return super().precmd(line)
        args = matches[0]
        if not args[2]:
            if args[1] == "count":
                objs = storage.all()
                count = 0
                for v in objs.values():
                    if type(v).__name__ == args[0]: 
                        count += 1
                print(f"{count}")
                return '\n'
            return f"{args[1]} {args[0]}"
        else:
            attr = args[2].split(", ")
            if len(attr) == 1:
                id = re.sub("[\"\']", "", attr[0])
                return f"{args[1]} {args[0]} {id}"
            else:
                dic_json = re.findall(r"{.*}", args[2])
                if dic_json:
                    id = re.sub("[\"\']", "", attr[0])
                    dic = re.sub("\'", "\"", dic_json[0])
                    return f"{args[1]} {args[0]} {id} {dic}"
                id = re.sub("[\"\']", "", attr[0])
                attr1 = re.sub("[\"\']", "", attr[1])
                attr2 = re.sub("[\"\']", "", attr[2])
                return f"{args[1]} {args[0]} {id} {attr1} {attr2}"

    def do_quit(self, arg):
        """ Quit command to exit the program
        """

        return 1

    def do_EOF(self, arg):
        """ EOF command to catch end of a file
        """

        print()
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
            return
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        else:
            new = classes[args[0]]()
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
        if k not in objs:
            print("** no instance found **")
            return
        print(objs[k])

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
        if k not in objs:
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
        key = "{}.{}".format(args[0], args[1])
        if key not in objs:
            print("** no instance found **")
            return
        dic_json = re.findall(r"{.*}", arg)
        if dic_json:
            try:
                dic = json.loads(dic_json[0])
            except Exception:
                return
            for k, v in dic.items():
                setattr(objs[key], k, v)
            storage.save()
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if attr:
            setattr(objs[key], args[2], attr[0])
        else:
            value = re.sub("\"", "", args[3])
            if '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    pass
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass
            setattr(objs[key], args[2], value)
        storage.save()


if __name__ == "__main__":
    """ main function to run the interpreter """

    HBNBCommand().cmdloop()
