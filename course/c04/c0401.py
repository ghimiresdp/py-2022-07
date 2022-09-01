"""
If Condition
- It is written with `if` keyword
- all the conditions that are enclosed within the `if` statement are
  indented.
- Unlike other programming languages, it do not need curley brackets
  or braces and might not need brackets for simple logical operations
- to end the statements inside of if condition, we just un-indent it

When the condition matches, it goes inside the if block otherwise skips
the execution part inside of the if block

Syntax
```
if <condition>:
    <statements>
```

## If else
- if else condition is same as if condition
- we use else for the condition that does not satisfy the if condition

Structure
```
if <condition>:
    <statements to run when the condition is satisfied>
else:
    <alternative statements that does not satisfy if condition>
```

## If elif else
- elif contains multiple conditions.
- if previous condition fail and we still need condition in the alternative conditions we can use
  elif.
- we can use any number of elif conditions in python.

Structure
```
if <condition>:
    <statements>
elif <alternative condition>:
    <alternative statements that satisfies elif>
else:
    <statements that does not satisfy any of above>
```
"""

x = 6
if x <= 5:
    print('The condition is true')
    # print(5/0)
print('I am outside if condition')

# Write a program to input a number from console and check whether the number is odd or not
# x = int(input('Enter a number: '))

# if x % 2:
#     # This code block runs only if the condition is true
#     print(f'{x} is odd')
# else:
#     print(f'{x} is even')

# print(f"The number {x} is {'odd' if x%2 else 'even'}")

# Write a program to input a number from console and check whether it is divisible
# by both 2 and 3

# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 3 == 0:
#     print("The number is divisible by both 2 and 3")
# elif num % 2 == 0:
#     print("The number is divisible by only 2")
# elif num % 3 == 0:
#     print("The number is divisible by only 3")
# else:
#     print("The number is not divisible by 2 and 3")
# #

# Write a program to check whether a word is palindrome word
word = 'Rotator'
if word.lower() == word[::-1].lower():
    print(f'{word} is the palindrome')
else:
    print(f'{word} is not palindrome')
    #

# John has $1000 in his pocket and he asks Jane her money in her pocket.
# He wants to find whether John is rich or Jane is. Write a program that
# solves John's problem.

# amount_jane =float(input("How much money does Jane have?: "))
# amount_john = 1000

# if amount_john > amount_jane:
#     print('John is Richer')
# elif amount_jane > amount_john:
#     print('Jane is Richer')
# else:
#     print("Both have equal amount of money")

#

x = 6

size = 'small' if x < 7 else ('medium' if (x >= 7 and x < 10) else 'large')

print(size)

# write a program to check whether a number exists in the given list or not
num = 29
list1 = [1, 5, 7, 9, 12, 24, 28, 41, 56]

if num in list1:
    print(f'{num}  exists in list')
else:
    print(f'{num} does not exist in list')

# Write a program to check whether a number is divisible
# by all of 2, 3, 4, 5, and 6
num = 60
# num = 30
# if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0:
# if num % 2 == num % 3 == num % 4 == num % 5 == num % 6 == 0:
# if all([not num % 2, not num % 3, not num % 4, not num % 5, not num % 6]):
# if sum([num % 2, num % 3, num % 4, num % 5, num % 6]) == 0:
if {num % 2, num % 3, num % 4, num % 5, num % 6} == {0}:
    print('the number is divisible by all of above')
else:
    print('not divisible')

#
# list2 = [1, 1, 1, 0, 1]
# print(all(list2))

number = 20
if number < 10:
    if number % 2 == 0:
        print('The number is even and less than 10')
    else:
        print('The number is odd and less than 10')
else:
    if number % 3 == 0:
        print('The number is divisible by 3 and greater than 10')
    else:
        print('The number is not divisible by 3 and greater than 10')

#

# find the division of a student according to their percentage

# 40% and above: Third Division
# 50% and above: Second Division
# 60% and above: First Division
# 80% and above: First Division with distinction
percent = 80

if percent >= 60:
    print('First Division')
    if percent >= 80:
        print('with distinction')
elif percent >= 50:
    print('Second Division')
else:
    print('Third Division')


#
