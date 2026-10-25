# Program to calculate Simple Interest

# Taking input from the user
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time in years: "))

# Calculating Simple Interest
SI = (P * R * T) / 100

# Displaying the result
print("Simple Interest =", SI)
