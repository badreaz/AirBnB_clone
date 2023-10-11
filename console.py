#!/usr/bin/python3
""" The entry point of the command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """ represents the command interpreter
    """

    prompt = "(hbnb) "

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
        """ creates a new instance of a class,
        saves it (to JSON file) and prints id
        """

        if (!arg):
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """ prints the string representation of an instance
        based on the class name and id
        """

        args = arg.split()
        if !arg[0]:
            print("** class name missing **")
            return
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif !arg[1]:
            print("** instance id missing **")
            return
        objs = storage.all()
        k = "{}.{}".format(arg[0], arg[1])
        instance = objs[k]
        if !instance:
            print("** no instance found **")
            return
        print(instance)



if __name__ == '__main__':
    """ main function to run the interpreter """

    HBNBCommand().cmdloop()
