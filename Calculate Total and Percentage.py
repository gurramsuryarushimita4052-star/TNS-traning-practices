# Program to calculate Total and Percentage of 5 subjects

# Taking marks as input
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculating total marks
total = m1 + m2 + m3 + m4 + m5

# Calculating percentage
percentage = total / 5

# Displaying the result
print("Total Marks =", total)
print("Percentage =", percentage, "%")
