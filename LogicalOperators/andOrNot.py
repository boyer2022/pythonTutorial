# 3 Logical operators
# and 
    # both must be true
# or
    # If at least one is true
# not
    # Reverses the condition
high_income = True
good_credit = True
student = True

# if not student:
#     print("Not Eligible, Not")
# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# More conditions (uncomment above examples first)
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
