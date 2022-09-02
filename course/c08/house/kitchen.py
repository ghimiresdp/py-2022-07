try:
    from ..school import Student
except ImportError:
    from school import Student

utensils = [
    'plate',
    'fry-pan',
    'kettle'
]

jane = Student('Jane Doe', 2)
print(jane)
