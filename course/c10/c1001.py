def divide(x, y):
    try:
        return x / y

    except ZeroDivisionError:
        print("We can not divide a number by zero so we are returning zero")
        return 0

    except Exception:
        print('Unknown Error')

    # except TypeError:
    #     print('We cannot perform division on non-numeric characters')




out = divide(10, 0)

print(out)


print('Hello World !!')

out = divide(10, 'a')

print('Hello World 2 !!')
