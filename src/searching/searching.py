# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        x = (start + end)// 2
        print(start,target,end,x)
        if arr[x] == target:
            return x
        elif target < arr[x]:
            return binary_search(arr, target, start, x - 1)
        else:
            return binary_search(arr, target, x + 1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

arr = [ 2, 3, 4, 10, 40 ] 
target = 10 
binary_search(arr,target,0,len(arr))