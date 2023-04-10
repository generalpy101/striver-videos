# Recursion is when a function calls itself until a specified condition is met
# Example:
'''
def main(i):
    print(i)
    main(i+1)
main(1)   
'''
# Above is an example of a recursive function.
# It will print the value of i and then call itself again with i+1's value
# This will continue until the program crashes. Infinite recursion like infinite loop
# Function call takes space on call stack, so infinite recursion will crash the program
# after some time.
# Python has a recursion limit, which can be changed. Default is 1000 and RecursionError
# is triggered when limit is reached. It is known as stack overflow in other languages.

# To stop the recursion, we have a condition. It is known as base case.
'''
def main(i):
    if i == 10:
        return
    print(i)
    main(i+1)
main(1)
'''
# Above is an example of a recursive function with a base case.
# It will print the value till i is 10 and then return.
# Recursion tree is a tree representation of the recursive function calls.
# It is used to understand the recursive function calls.
# It is also used to find the time complexity of the recursive function.
