# Problem: Print subsequences whose sum is k
# Eg: arr = [1,2,1], k = 2 then
# Output: [1,1], [2]
'''
def sum_is_k(arr, i, subarr, k):
    if i>=len(arr):
        if sum(subarr) == k:
            print(subarr)
        return
    subarr.append(arr[i])
    sum_is_k(arr, i+1, subarr, k)
    subarr.remove(arr[i])
    sum_is_k(arr, i+1, subarr, k)

arr = [1,2,1]
k = 2
sum_is_k(arr, 0, [], k)
'''
# Modify: Print only first subsequence
'''
def sum_is_k(arr, i, subarr, k):
    if i==len(arr):
        if sum(subarr) == k:
            print(subarr)
            return True
        return False
    subarr.append(arr[i])
    if sum_is_k(arr, i+1, subarr, k):
        return True
    subarr.remove(arr[i])
    if sum_is_k(arr, i+1, subarr, k):
        return True

arr = [1,2,1]
k = 2
sum_is_k(arr, 0, [], k)
'''

# Modify: Print count of subsequences whose sum is k
'''
def sum_is_k(arr, i, sum, k):
    if i==len(arr):
        if sum == k:
            return 1
        return 0
    sum += arr[i]
    l = sum_is_k(arr, i+1, sum, k)
    sum -= arr[i]
    r = sum_is_k(arr, i+1, sum, k)
    return l + r
arr = [1,2,1]
k = 2
print(sum_is_k(arr, 0, 0, k))
'''