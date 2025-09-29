#  for loop
# Example: try to run 3 x's
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# Cleaner code:
for number in range(1, 4):
    print("Attempt, cleaner", number, number * ".")

# Passing third arguement as a step:
    # Arguements(Starting number, Up to, Stepping how many numbers)
for number in range(1, 10, 2):
    print("Attempt, cleaner, step", number, number * ".")