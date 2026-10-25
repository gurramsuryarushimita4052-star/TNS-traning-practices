# Find the largest element in a list without using max()

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

# Compare each element with largest
for num in numbers:
    if num > largest:
        largest = num

print("Largest element =", largest)
