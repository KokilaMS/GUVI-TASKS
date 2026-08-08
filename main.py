# TASK - 4
from sqlite3 import IntegrityError

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
