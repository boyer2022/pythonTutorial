x = input("x: ")
# y = x + 1

# Type conversion 
# int(x)
# float(x)
# bool(x)
# str(x) # Already a string

# print(type(x)) # Prints the type of variable
# To fix: convert x to int
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Boolean conversion
# Falsy
    # ""
    # 0
    # None
    # Examples:
        # bool(0)
            # False
        # bool(1)
            # True
        # bool(-1)
            # True
        # bool(5)
            # True
        # bool("")
            # False
        # bool("False")
            # True