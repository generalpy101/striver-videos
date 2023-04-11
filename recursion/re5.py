# Multiple recursion
# Many recursive calls are made to the same function

# Problem 1:
# Fibonacci sequence using recursion
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(7))
'''
# Here is the explanation for the code above:
# 1. We define a function, fib, that takes one parameter, n.
# 2. If n is 0, fib returns 0.
# 3. If n is 1, fib returns 1.
# 4. Otherwise, fib returns fib(n-1) + fib(n-2). In other words, the function calls itself twice, once with n-1 and once with n-2.


