# Formatting styles in Python

first = "Matt"
last = "Boyer"
full = first + " " + last

# formatting
full_formatted = f"{first} {last}"

print(full)
print(full_formatted)

# Length
    # Printing the length of the first name, adding to 2
full_length = f"{len(first)} {2 + 2}"
print(full_length)