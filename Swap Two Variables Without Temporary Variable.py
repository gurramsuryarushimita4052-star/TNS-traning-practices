# Program to swap two variables without using a temporary variable

# Taking two values as input
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Displaying values before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping the values
a, b = b, a

# Displaying values after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
