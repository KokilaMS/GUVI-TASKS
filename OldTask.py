
## Guess the Number Game##
import random
# 1. Computer randomly selects a number between 1 and 10
secret_number = random.randint(1, 10)
print("Welcome to Guess the number Game")
print("I am thinking of a number between 1 and 10.")

# Start with an incorrect guess to trigger the loop
guess = 0

# Loop until the player guesses the secret number
while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
                print("Too High! Try again.")
        elif guess < secret_number:
                print("Too Low! Try again.")
        else:
                print("Correct! The secret number was",secret_number)
                break # This stops the loop immediately because the game is over
print("Thank you for playing")

## Guess the Scramble word game ##
import random

# The list of words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Pick a random word from the list
original_word = random.choice(words)

# 1. STRING MANIPULATION: Break the word into single letters
letters = list(original_word)

# Mix up the letters randomly
random.shuffle(letters)

# Stitch the mixed letters back into a single scrambled word
jumbled_word = "".join(letters)

# Print the game greeting and the puzzle word
print("WELCOME TO THE WORD SCRAMBLE GAME")
print("Unscramble this word:", jumbled_word)

# 2. LOOP: Keep asking for a guess over and over
while True:
        guess = input("Enter your guess: ")

        # 3. CONDITION: Check if the guess is right or wrong
        if guess == original_word:
                print("Correct! You unscrambled the word:",original_word)
                break  # This stops the loop immediately because the game is over
        else:
                print("Wrong answer! Try again.")
print("Thank you for playing")


# TASK - 4

# 1. Even and Odd list

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)


print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)
print("===================================================================")

# 2. Count and List Prime and Odd numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list = []

for num in numbers:
    if num > 1:
        is_prime = True
        # Check for factors from 2 up to num - 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)


print("Prime Numbers List:", prime_list)
print("Total Prime Count:", len(prime_list))
print("===================================================================")

# 3. Identify Happy Numbers in a List

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count = 0
happy_numbers = []

for num in numbers:
    temp = num
    # Loop to check if the number resolves to 1 or gets stuck in a known loop
    while temp != 1 and temp != 4:
        total = 0
        # Split number into digits and square them
        for digit in str(temp):
            total += int(digit) ** 2
        temp = total

    if temp == 1:
        happy_count += 1
        happy_numbers.append(num)


print("Happy numbers found:", happy_numbers)
print("Total count:", happy_count)
print("===================================================================")

# 4. Sum of First and Last digit of an Integer

number = 4589

num_str = str(number)
first_digit = int(num_str[0])
last_digit = int(num_str[-1])

digit_sum = first_digit + last_digit

print("Sum of first and last digit:", digit_sum)
print("===================================================================")
# 5. Ways to Make Change for Rs. 10

ways_count = 0

# try every possible count of coins using simple loops
for r10 in range(0, 2):  # 10s can be 0 or 1
    for r5 in range(0, 3):  # 5s can be 0, 1, or 2
        for r2 in range(0, 6):  # 2s can be 0, 1, 2, 3, 4, or 5
            for r1 in range(0, 11):  # 1s can be anywhere from 0 to 10

                total_money = (r10 * 10) + (r5 * 5) + (r2 * 2) + (r1 * 1)

                if total_money == 10:
                    ways_count += 1
                    print("Way", ways_count, ": Rs10=", r10, " Rs5=", r5, " Rs2=", r2, " Rs1=", r1)

print("Total unique ways:", ways_count)
print("===================================================================")

# 6. Find Duplicates Across Three Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 6, 7, 8]

# Combine all items into one single list
all_items = list1 + list2 + list3
duplicates = []

for item in all_items:
    # Manual counting loop
    count = 0
    for x in all_items:
        if x == item:
            count += 1

    # If it appears more than once, it's a duplicate
    if count > 1:
        # Check if we already added it to our duplicate list
        already_added = False
        for d in duplicates:
            if d == item:
                already_added = True

        if already_added == False:
            duplicates.append(item)

print("Duplicate elements are:", duplicates)
print("===================================================================")

#7. Find First Non-Repeating Element

elements = [9, 4, 9, 6, 7, 4]
first_unique = None

for item in elements:
    # Count how many times 'item' appears in the list
    appearance_count = 0
    for x in elements:
        if x == item:
            appearance_count += 1

    # If it appears exactly once, we found it!
    if appearance_count == 1:
        first_unique = item
        break  # Exit the loop immediately to keep the first one

print("First non-repeating element is:", first_unique)
print("===================================================================")

# 8. Find Minimum Element in a List
rotated_list = [4, 5, 6, 1, 2, 3]

# Assume the first element is the smallest
minimum = rotated_list[0]

# Check every element against our current minimum
for item in rotated_list:
    if item < minimum:
        minimum = item

print("The minimum element is:", minimum)
print("===================================================================")

# 9. Find a Triplet whose Sum Equals 59

lst = [10, 20, 30, 9]
target = 59

# Nested loops to match three different items step-by-step
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):

            current_sum = lst[i] + lst[j] + lst[k]

            if current_sum == target:

                print("Triplet found:", lst[i], ",", lst[j], ",", lst[k])
print("===================================================================")

#10. Check if a Sub-list Sum Equals Zero

given_list = [4, 2, -3, 1, 6]
has_zero_sum = False

# Try every possible start point and end point
for start in range(len(given_list)):
    for end in range(start, len(given_list)):

        # Manually add up the numbers between start and end
        current_sub_sum = 0
        for index in range(start, end + 1):
            current_sub_sum += given_list[index]

        if current_sub_sum == 0:
            has_zero_sum = True
print("Does a zero-sum sub-list exist?:", has_zero_sum)
print("===================================================================")


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