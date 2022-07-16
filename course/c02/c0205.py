# F-Strings
name = "John"
age = 20

intro = "My name is {} and I am {} years old".format(name,age,)
print(intro)

intro_1 = f"My name is {name} and I am {age} years old"
print(intro_1)


intro_2 = f'My name is {name} and I will be {age + 10} years old by 2032.'
print(intro_2)
mobile = 'iphone'
intro_3 = f'I have {mobile} and I like it.'
print(intro_3)
mobile = "Iphone"
intro_5 = f'I have {mobile} and I love it.'
print(intro_5)
#
intro_6 = f'My name is {name} and I will be {age:10d} years old by 2032.'
print(intro_6)


name_1 = 'Ram Oli'
name_2 = 'Shyam Chaudhary'

print(f"{name_1.ljust(20)} is in the USA.")
print(f"{name_2.ljust(20)} is in England.")


intro_6 = f'My name is {name} and I will be {(age+10):10d} years old by 2032.'
print(intro_6)
#
name = "Johnnathon Doe"
# print(f'The word {name}  is {"long" if name.__len__() > 10 else "short"}')




# String Methods

# 1. finding out the length

name = "John ssdfsdfsd sdlfsdf sdlf sdflsdf sdlf sldf sdlfls dfl dlf"
print(len(name))
print(name.__len__())

age = "125a"

print(type(age))

print(age.isnumeric())
print(age.isdecimal())

age = "125"
check = age.isnumeric()
print(check)

age = "125.6"
check = age.isnumeric()
print(check)

# replace

sentence = "I am John and John I am 20 John years old John"

print(sentence)

new_sentence = f"I am Jane and I am 20 years old"
print(new_sentence)
print(sentence.replace('John', "Jane"))
print(sentence.replace('John', "Jane", 3))

# Text Justification

_name = 'John'
# left justification

print(_name.ljust(50), 'abc')
print(_name.ljust(50, '_'), 'abc')

# right justification
print(_name.rjust(50), 'abc')
print(_name.rjust(50, '#'), 'abc')
print(_name.rjust(50, '~'), 'abc')


# center alignment
print(_name.center(50), 'abc')
print(_name.center(50, '='), 'abc')


# Download Bar
width = 100
print('\n\n\n')
print(f'[{("=" * 20).ljust(width, ".")}]')
print(f'[{("=" * 30).ljust(width, ".")}]')
print(f'[{("=" * 40).ljust(width, ".")}]')
print(f'[{("=" * 50).ljust(width, ".")}]')
print(f'[{("=" * 70).ljust(width, ".")}]')
print(f'[{("=" * 90).ljust(width, ".")}]')
print(f'[{("=" * 100).ljust(width, ".")}]')

bar_content = f'[abc \' {("#" * 50).ljust(width, ".")}]'

print('The field "Last Name" is not fulfilled.')

word = "ABC"
print(word.isalpha())

word = "ABC1"
print(word.isalpha())

word = "ABC1"
print(word.isalnum())

word = "ABc"
print(word.isupper())



# Joining and splitting Strings (After we complete List)

# finding out the index of the substring

data = "My name is John."

print(data.index('John'))

# finding if a string starts with the substring

print(data.startswith('Your'))


data = "      My name is John.        "
print(data, "Next Value")
print(data.strip(), "Next Value")
