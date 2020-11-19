''' Module lab06.py'''
# problem 1 - Iterator
def reverse_iter(iterable):
    result = []
    
    for elem in reversed(iterable):
        result.append(elem)
    return iter(result)

# problem 2 - Decorator
def return_logger(func):
    def print_value(a, b, c):
        val = func(a, b, c)
        print("Function returned: " + str(val))
        return val
    return print_value

#problem 3 - Generator
def get_fib_generator():
    x = 0
    y = 1

    while True:
        yield y
        x,y = y, x + y
