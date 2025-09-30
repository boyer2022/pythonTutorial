# Infinite loop is a loop that runs forever

# From whileLoopExample.py
#  To run: 
    # Terminal, python3, whileLoopExample.py

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break