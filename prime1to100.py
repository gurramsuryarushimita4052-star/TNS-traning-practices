# Print prime numbers between 1 and 100

for num in range(2, 101):
    count = 0

    # Check whether the number has factors
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    # Prime number has exactly 2 factors
    if count == 2:
        print(num, end=" ")
