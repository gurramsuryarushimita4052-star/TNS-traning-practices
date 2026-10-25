# Print Pascal's Triangle

rows = 5

for i in range(rows):

    # Print spaces
    for space in range(rows - i - 1):
        print(" ", end=" ")

    number = 1

    # Print numbers
    for j in range(i + 1):
        print(number, end="   ")

        # Calculate next number
        number = number * (i - j) // (j + 1)

    print()
