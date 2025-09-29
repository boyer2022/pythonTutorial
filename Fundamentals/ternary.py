
# Ternary operator
age = 22 # Change to see difference
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
# Cleaner code
if age >= 18:
    message = "Eligible Cleaner"
else:
    message = "Not Eligible Cleaner"
print(message)

# Simpler
message = "Eligible,Simple" if age >= 18 else "Not Eligible,Simple"
print(message)