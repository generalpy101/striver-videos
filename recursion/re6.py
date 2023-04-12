# Recursion on subsequence
# A subsequence is a sequence that can be derived from another sequence
# by deleting some elements without changing the order of the remaining elements.
# It can be bot continuous or discontinuous.
# Eg: For arr=[1,2,3] the subsequences can be:
# [1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], []
# Order must be preserved.
# A subarray is a contiguous subsequence. 
# eg: For arr=[1,2,3] the subarrays can be:
# [1,2,3], [1,2], [2,3]
'''
def subseq(arr, i, subarr):
    if i == len(arr):
        print(subarr)
        return
    subseq(arr, i+1, subarr)
    subseq(arr, i+1, subarr+[arr[i]])
arr = [1,2,3]
subseq(arr, 0, [])
'''
# Here is the explanation for the code above:
# 1. The function subseq takes three parameters:
#     a. The array to be traversed
#     b. The index of the element in the array to be traversed
#     c. The array to be printed
# 2. The base case for this problem is when the index of the element to be traversed equals the length of the array.
# 3. On each level of recursion, two recursive calls are made. The first recursive call is made without the current element added to the array to be printed. The second recursive call is made with the current element added to the array to be printed.
# 4. When the base case is reached, the array to be printed is printed.
# 5. The function is called with the index of the element to be traversed as 0 and the array to be printed as an empty array.
'''
def subseq(arr, i, subarr):
    if i >= len(arr):
        print(subarr)
        return
    subarr.append(arr[i])
    subseq(arr, i+1, subarr)
    subarr.remove(arr[i])
    subseq(arr, i+1, subarr)
arr = [1,2,3]
subseq(arr, 0, [])
'''
# Here is the explanation for the code above:
# 1. The function subseq takes three arguments, an array, an initial index and an empty array as subarr.
# 2. If the index is greater than the length of the array, then we print the array and return.
# 3. We append the element at the index to the subarr array and call the function recursively by incrementing the index by 1.
# 4. After the recursive call, we remove the element from the subarr array and call the function again by incrementing the index by 1.
# 5. We call the function with the empty array as subarr by passing 0 as the initial index.
