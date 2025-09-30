# Creating lists of numbers [2, 3, 4, 5]---- tuples
# tuples are a collection of lists that cannot be modified
    # but are interable- used in a loop

def multiply (*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        # OR
        total *= number
    return total


print(multiply(2, 3, 4, 5))