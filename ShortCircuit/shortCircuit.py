# Change the variables to see different results
high_income = False
good_credit = True
student = True

# By leaving out the () on either pair of conditions
# python ignores the rest of the conditions
if high_income or good_credit and not student:
    print("Eligible")
else:
    print("Nope!")