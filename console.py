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



if __name__ == '__main__':
    """ main function to run the interpreter """

    HBNBCommand().cmdloop()
