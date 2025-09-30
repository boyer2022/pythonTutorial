# Default Arguements
    # Taken from arguementsexample.py

# Adding default arguement value
def increment(number, by=1):
    return number + by

results = increment(2, 1)
print (results)

# Simplify
print(increment(2, 1)) 

# Removing arguement value
print(increment(2))

# Adding custom arguement, bypasses default value
print(increment(2, 5))