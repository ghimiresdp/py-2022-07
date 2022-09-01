x = 1
# A condition to check whether it satisfies to run further
# A statement that runs when it satisfied

# An update statement that is capable of dynamically changing the state
# that eventually changes the condition
while x <= 5:
    print('Hello !!')
    x += 1
"""
1:  x = 1, print,   x = 2
2:  x = 2, print,   x = 3
3:  x = 3, print, x = 4
..

5: x = 5, print, x = 6
6: x= 6 (6 <= 5)-> False
"""

print('hi')

# using while loop to create a list of first 10 odd numbers
lst = []
count = 0
number = 1

while count < 10:
    if number % 2 == 1:
        lst.append(number)
        count += 1
    number += 1

print(lst)

# solution 2
lst = []
number = 1

while len(lst) < 10:
    if number % 2 == 1:
        lst.append(number)
    number += 1

print(lst)

# solution 3
number = 1
lst.clear()
while number <= 10:
    lst.append(number * 2 - 1)
    number += 1
print(lst)
#

# solution 4
number = 1
lst.clear()
while number < 20:
    lst.append(number)
    number += 2
print(lst)

# While Else
x = 1
while x <= 10:
    print('The current value of x is: ', x)
    x += 1
else:
    print('Now the value is greater than 10')

# continue
x = 0
while x < 10:
    x += 1
    if x == 7:
        print('skipping')
        continue
    print('The current value of x is: ', x)

# Write a program that inputs names of students until the user
# enters exit and display the list at the end.
# lst = []
# while True:
#     user_input = input("Enter student name: ")
#     if user_input == "exit":
#         break
#     lst.append(user_input)
# print(lst)
##

x = 0
while x < 100:  # this indicates x can loop until it is 100
    x += 1
    if x % 3 == 0:
        continue  # this statement skips for all multiples of x
    if x > 10:
        break  # This statement terminates the loop whenever the value of x > 10
    print('The current value of x is: ', x)

#
"""
Write a program that displays all words entered by the user.
- The program should sensor slightly offensive words and skip execution for one time
- The program should immediately exit when highly offensive words are used
- Check the word if it is palindrome if it is not offensive.
"""
offensive = ['dull', 'ugly', 'short']
highly_offensive = ['dog', 'shit', 'damn', 'beat']


while True:
    word = input('Enter a word: ').lower()

    if word in offensive:
        print(f'The word {word[0]}{"*" * (len(word) - 1)} is offensive, so skipping execution...')
        continue

    if word in highly_offensive:
        print("You used Highly offensive word, Good Bye!!")
        break

    if word[::-1] == word:
        print(f'The word {word} is palindrome')
    else:
        print(f'The word {word} is not palindrome')






#
