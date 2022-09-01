"""
Logical Operators
- logical operators are used to combined 2 or more relational operators or conditions
- They use human readable words as operators
    - and
    - or
    - not
"""

# %% and
"""
- it is used between two statements or conditions
- the value is true if and only if both of the conditions are true
"""
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(5 == (10 // 2) and False)  # False
print(True and True and True)    # True


is_student = False
is_course_running = True

is_visa_valid = is_student and is_course_running

print('Visa Valid: ', is_visa_valid)


x = 5
y = 10

print(True and  x)


# %% or
"""
- it is used between two statements or conditions
- the value is true if any of the conditions is true

"""
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(5 or 6)


is_married = False
is_living_with_partner = False

chance_of_child = is_married or is_living_with_partner


# Not
"""
- it is used  before a condition or statement
- the value is opposite of the condition
"""
print(not True)  # False
print(not False)  # True


nepali = False

print(not nepali)


print(not ((4 < 5) or (5 < 3)))


# Explanation
# not( (4<5) or (5<3) )
# not( True or (5<3) )
# not( True or False )
# not( True )
# False

x = 4 < 5 or 6 > 7
y = True and 10 > 12

print(x and y)


# complex Logical operation example
can_cat_fly = False
can_snake_walk = False
can_dog_bark = True
can_john_speak_French = True

print(not ((not (can_cat_fly or can_dog_bark) or (can_snake_walk)) and can_john_speak_French))


#
# If we do not use brackets in complex logical operations, we
# might not get the expected output

print(not True or not False)  # True
print(not (True or not False))  # False
print((not True) or (not False))  # True


# if it is cloudy today and if it rained yesterday, then it rains today
# in other conditions it doesn't rain
cloudy_today = True
rained_yesterday = True
print(cloudy_today and rained_yesterday)

#
