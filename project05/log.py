'''Module log.py ''' 
from log_decorator import log
import time

@log()
def factorial(*num_list):
    results = []
    for number in num_list:
        res = number
        for i in range(number-1,0,-1):
            res = i*res
        results.append(res)
    return results

@log("logger.txt")
def waste_time(a, b, c):
    print("Wasting time.")
    time.sleep(5)
    return a, b, c

@log("logger.txt")
def gcd(a, b):
    print("The GCD of", a, "and", b, "is ", end="")
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    print(abs(a))
    return abs(a)

@log()
def print_hello():
    print("Hello!")

@log(10)
def print_goodbye():
    print("Goodbye!")

if __name__ == "__main__":
    factorial(4, 5)
    waste_time("one", 2, "3")
    gcd(15,9)
    print_hello()
    print_goodbye()
