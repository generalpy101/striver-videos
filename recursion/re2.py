# This lecture will contain some basic problems related to recursion

# Problem 1:
# Print name 5 times
'''
def main(name, count):
    if count == 0:
        return
    print(name)
    main(name, count-1)
main("generalpy", 5)
'''
# Problem 2:
# Print 1 to N
'''
def main(i,n):
    if i > n:
        return
    print(i)
    main(i+1,n)
main(1,10)
'''

# Problem 3:
# Print N to 1
'''
def main(n):
    if n == 0:
        return
    print(n)
    main(n-1)
main(10)
'''

# Problem 4:
# Print 1 to N using backtracking
'''
def main(i,n):
    if i < 1:
        return
    main(i-1,n)
    print(i)
main(10,10)
'''
# Backtracking is a technique to solve a problem by breaking it into smaller sub-problems
# Here we put print statement after the recursive call
# So that the last statement will be printed first
# This is called backtracking. It is used to solve problems like DFS.

# Problem 5:
# Print N to 1 using backtracking
'''
def main(i,n):
    if i > n:
        return # 1. Stop condition
    main(i+1,n) # 2. Recursion
    print(i) # 3. Print
main(1,10)
'''
# Here is the explanation for the code above:
# 1. The main function is called with i = 1 and n = 10.
# 2. 1 is printed.
# 3. The main function is called with i = 2 and n = 10.
# 4. 2 is printed.
# 5. The main function is called with i = 3 and n = 10.
# 6. 3 is printed.
# 7. The main function is called with i = 4 and n = 10.
# 8. 4 is printed.
# 9. The main function is called with i = 5 and n = 10.
# 10. 5 is printed.
# 11. The main function is called with i = 6 and n = 10.
# 12. 6 is printed.
# 13. The main function is called with i = 7 and n = 10.
# 14. 7 is printed.
# 15. The main function is called with i = 8 and n = 10.
# 16. 8 is printed.
# 17. The main function is called with i = 9 and n = 10.
# 18. 9 is printed.
# 19. The main function is called with i = 10 and n = 10.
# 20. 10 is printed.
# 21. The main function is called with i = 11 and n = 10.
# 22. The main function returns.
# 23. The main function returns.
# 24. The main function returns.
# 25. The main function returns.
# 26. The main function returns.
# 27. The main function returns.
# 28. The main function returns.
# 29. The main function returns.
# 30. The main function returns.
# 31. The main function returns.
# 32. The main function returns.
# 33. The main function returns.
# 34. The main function returns.
# 35. The main function returns.