# Remove duplicate elements from a list

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

# Check each element
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list =", numbers)
print("List without duplicates =", unique)
