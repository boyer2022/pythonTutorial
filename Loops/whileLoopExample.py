#  To run: 
    # Terminal, python3, whileLoopExample.py
command = ""
while command.lower() != "quit": # Always creates the user's input to lowercase
    command = input(">")
    print("ECHO", command)