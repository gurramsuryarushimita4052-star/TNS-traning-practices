# Find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Start checking from the bigger number
if a > b:
    lcm = a
else:
    lcm = b

# Find the first number divisible by both
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + 1

print("LCM =", lcm)
