# Problems on functional recursion

# Problem 1:
# Reverse an array
'''
def main(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    main(arr, l + 1, r - 1)
arr = [1,2,3,4,5,6,7,8,9]
print(f"Before: {arr}")
main(arr, 0, len(arr) - 1)
print(f"After: {arr}")
'''
# The code above does the following, explained in English:
# 1. If the left index is less than or equal to the right index, continue. Otherwise, stop.
# 2. Swap the left index with the right index.
# 3. Recursively call main() with the left index increased by 1 and the right index decreased by 1. 

# Reverse array recursively using single parameter
'''
def rev(arr, i):
    n = len(arr)
    if i >= n // 2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    rev(arr, i + 1)
arr = [1,2,3,4,5,6,7,8,9]
print(f"Before: {arr}")
rev(arr, 0)
print(f"After: {arr}")
'''

# Problem 2:
# Write functional code to check if a string is a palindrome
'''
def main(string, i):
    n = len(string)
    if i >= n // 2:
        return True
    if string[i] != string[n-i-1]:
        return False
    return main(string, i + 1)
print(main("racecar", 0))
'''
# Time complexity: O(n/2) and space complexity: O(1) [auxiliary space]