def greet ():
    print("hello, world")

greet()


def personalized_greeting(name):
    print(f"hello, {name}!")

personalized_greeting("regan")


def square(number):
    return number ** 2

result = square(5)
print(result)


def rectangle_area(length, width):
    return length * width

result = rectangle_area(4, 5)
print(result)


def apply_operation (func, num):
    return func(num)

def double(num):
    return num * 2

result_double = apply_operation(double, 7)
print(result_double)

result_square = apply_operation(square, 5)
print(result_square)