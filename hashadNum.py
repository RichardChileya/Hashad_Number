# Get input from user
num = int(input("Enter a number: "))

# Find sum of digits
sum_of_digits = sum(int(digit) for digit in str(num))

# Check if it's a Harshad number
if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
