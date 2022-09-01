c = 36
f = c * 9/5 +32

print(f)

def celcius_to_fahrenheit(c):
    return c * 9 / 5 + 32

height_of_person = 65
print(celcius_to_fahrenheit(height_of_person))


x = "hello"
x.upper()

x = 5
print(type(x))
# x.upper()

class Temperature:
    value = 0

t1 = Temperature()

print(t1.value)


# ##################################################

def perimeter(length, width):
    return 2 * (length + width)

def area(length, width):
    return length * width

class Rectangle:
    length = 10
    breadth = 5

    def perimeter(self):
        return 2 * (self.length  + self.breadth)

    def area(self):
        return self.length * self.breadth

    # perimeter, area


x = Rectangle()

print(x.length)
print(x.area())
print(x.perimeter())

y = Rectangle()
print(y.area())
