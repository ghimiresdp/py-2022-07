x = 10  # global variable


def my_function():
    y = 20  # local variable (it's scope is only inside a function)
    print(x)  # 10
    print(y)  # 20

# print(x)  # 10


def my_next_function():
    # print(x)  # raises exception since x is accessed before assignment
    global x
    x = 30
    print(x)



# my_function()
# print(y)
# print(y)      # raises an exception since it is a local variable.

my_next_function()

print(x)
