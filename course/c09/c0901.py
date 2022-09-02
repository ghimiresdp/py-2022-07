# file = open('exports/person_1.json', 'r')
# print(file.read())
# file.close()

# file = open('course/c09/test.txt', 'r')
# print(file.read())
# file.close()


# file = open('course/c09/test.txt', 'w')
# file.write('This is a new content')
# file.close()


# file = open('D:\\dev\\test.txt', 'w')
# file.write('This is a new content')
# file.close()


# file = open('course/c09/test.txt', 'a', encoding='utf-8')
# file2 = open('course/c09/test.txt', 'a', encoding='utf-8')
# file.write('This is a new content')
# file2.write('\nA')
# file.write('\n😄')
# file.close()


# with open('course/c09/test.txt', 'a', encoding='utf-8') as file:
#     file.write('This is a new content')
#     file.write('\nA')
#     file.write('\n😄')

# abc


file = open('course/c09/test.txt', 'r+', encoding='utf-8')
lines =file.readlines()
del lines[2]
file.seek(0)
file.truncate()
file.writelines(lines)
file.close()
