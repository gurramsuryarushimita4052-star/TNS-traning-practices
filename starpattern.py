# Print a star pattern

rows = 5

# Outer loop controls rows
for i in range(1, rows + 1):

    # Inner loop prints stars
    for j in range(i):
        print("*", end=" ")

    print()
