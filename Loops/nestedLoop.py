# Nested Loops
    # Putting one loop inside of another loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# How it works:
# The first run of for(x) loop starts,
#     then first run of 2nd(y) loop starts,
#         The (y) loop must run 3x, then jumps back to (x) loop.
# Process is repeated until (x) reaches 5 loops iterations.