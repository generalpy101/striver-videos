# Problem:
# Summation of N numbers
# Parameterwise way
'''
def main(n, sum):
    if n == 0:
        print(sum)
        return  
    sum += n
    main(n-1, sum)
main(10,0)
'''
# Functional recursion
# Value is returned, no parameter is passed
'''
def main(n):
    if n == 0:
        return 0
    return n + main(n - 1)
print(main(10))
'''