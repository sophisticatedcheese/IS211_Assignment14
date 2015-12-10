__author__ = 'Terence J - November 2015'

def fib(n):
    """this function was taken from http://en.literateprograms.org/Fibonacci_numbers_(Python)"""
    if n == 0: return 0
    elif n == 1:
        return 1
    else: return fib(n-1) + fib(n-2)

def gcd(a, b):
    while b:
        (a, b) = (b, (a % b))
    return a

if __name__ == '__main__':
    fib(7)
    gcd(18, 2)
