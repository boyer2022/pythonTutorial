# Print only even numbers from 1-10
# Display message "You have 4 even numerbers"

count = 0
for number in range(1, 10):
    if number % 2 == 0:     # Check to see if remainder by division by 2 equals 0
        count += 1          # Increments count by 1 for each iteration of loop
        print(number)
print(f"You have {count} even numbers")