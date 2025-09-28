course = "  Python Programming"
# Length function
course_length = "The length of your string is: " + f"{len(course)}"
print(course_length)

# Methods
    # Add a . 
    # Everything in Python is an object
    # All objects have functions called Methods that can be accessed using . notation
    # Does not change original string
course.upper()
print(course.upper())   # uppercase
print(course.lower())   # lowercase
print(course.title())   # Capitalizes first letter of every word
print(course.strip())   # Removes whitespace at the beginning and end of string
print(course.lstrip())  # Removes whitespace from the left(beginning)of string
print(course.rstrip())  # Removes whitespace from the end of a string
# print(course.find("pro"))   # Finds idex of parts of a string (displaying as -1, not correct due to lowercase)
print(course.replace("P", "j")) # Subsitutes one value for another for whole string
print("Pro" in course)  # Check if an expression is in a string (True/False)
print("swift" not in course)    # Checks if a value is NOT in a string (True/False)