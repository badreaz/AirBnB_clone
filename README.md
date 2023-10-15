# AirBnB_clone

This project is to create a clone of AirBnB.
The goal of this project is to create a server copy of the AirBnB website(hbnb). 

#  Command Interpreter Description

# How to start the command
You can start the command interpreter in interactive mode like:
'''shell  
$ ./console.py   
(hbnb) help    
    
Documented commands (type help <topic>):   
========================================   
EOF  help  quit   
   
(hbnb)    
(hbnb)    
(hbnb) quit    
$    
or in non-interactive mode like:    
$ echo "help" | ./console.py   
(hbnb)   
   
Documented commands (type help <topic>):     
========================================     
EOF  help  quit    
(hbnb)     
$    
$ cat test_help   
help   
$    
$ cat test_help | ./console.py   
(hbnb)   
   
Documented commands (type help <topic>):     
========================================      
EOF  help  quit    
(hbnb)     
$   
'''   
   
# How to use the command
quit and EOF: exit the program. Ex: quit    
help: prints the description of the command. Ex: $ help <command>     
create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel     
show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234    
show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234    
all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all    
update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"    
   
