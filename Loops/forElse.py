# for else loop
    # Sending a message 3 times/Attempts

successful = False
for number in range(3):
    print("Attempt",number, number * ".")        # First attempt
    if successful:      
        print("Successful") # If 1st attempt is True, print
        break               # No other attempts are needed, exit program
else:   # only get executed if 3 attempts are made. Change successful to False
    print("Attempted 3 times and failed")