## Task - 5

# 1. Filter People Under 18 and Map Names

people = [
    {"name": "Kokila", "age": 32},
    {"name": "Suresh", "age": 38},
    {"name": "Sathvik", "age": 5},
    {"name": "Thanisha", "age": 6}
]

# Checks if a person is 18 or older
check_age = lambda person: person["age"] >= 18
adults_filter = filter(check_age, people)

# Takes the name string
get_name = lambda person: person["name"]
names_map = map(get_name, adults_filter)

# Convert to a normal list
names_list = list(names_map)
print("Adult names:", names_list)
print("===================================================================")

# 2. Product of All Numbers Using Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Takes two numbers (total so far 'a', next number 'b') and multiplies them
multiply = lambda a, b: a * b

product = reduce(multiply, numbers)
print("Product of numbers:", product)
print("===================================================================")

# 3. Squares of Even Numbers

numbers = [1, 2, 3, 4, 5, 6]

# Checks if a number is even
check_even = lambda x: x % 2 == 0

# Comprehension loops through numbers and applies the logic
squares_of_evens = [x * x for x in numbers if check_even(x)]

print("Squares of even numbers:", squares_of_evens)
print("===================================================================")

# 4. Lambda Function to Check if String is a Number

# .isdigit() is a basic tool that checks if a string is made of numbers
is_number = lambda text: text.isdigit()

# Testing the lambda function
print("Is '12345' a number?", is_number("12345"))  # True
print("Is 'apple' a number?", is_number("apple"))  # False
print("===================================================================")

# 5. Extract Year, Month, and Day From Datetime

import datetime

# Create a sample date (August 9, 2026)
sample_date = datetime.datetime(2026, 8, 9)

# Lambda takes the date object and returns its basic attributes as a group
get_date_info = lambda dt: (dt.year, dt.month, dt.day)

# Break the group back into simple variables
year, month, day = get_date_info(sample_date)

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("===================================================================")

# 6. Lambda Function to Generate Fibonacci Series

# A simple lambda that builds the sequence by looking back at previous items
fibonacci = lambda n: [0] if n == 1 else [0, 1] if n == 2 else (
    lambda f: [f(i, f) for i in range(n)]
)(lambda i, self: 0 if i == 0 else 1 if i == 1 else self(i-1, self) + self(i-2, self))

print("Fibonacci terms:", fibonacci(7))
print("===================================================================")
