import json

person = {
    "name":"John Doe",
    'age':20,
    'married':False,
    'occupation':'programmer',
    'organization': None,
    'programming_languages': [
        {
            "name": "Python",
            "version": 3.9,
            'level': "Beginner",
        },
        {
            "name": "Java",
            "version": 17,
            'level': "Expert",
        },
        {
            "name": "C++",
            "version": 2019,
            'level': "Mid",
        },
    ]
}


# print(json.dumps(person, indent=2))
with open("exports/person_1.json", 'w') as file:
    json.dump(person, file, indent=2)


with open("exports/person_1.json", 'r') as file:
    person2 = json.load(file)

print(person2)


str1 = json.dumps(person)

print(str1)

str2 = '{"name": "C++", "version": 2019, "level": "Mid"}'

obj1 = json.loads(str2)

print()
print(obj1)
