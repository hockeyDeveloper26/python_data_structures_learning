# Merge Sort : Time Complexity O(n log n) = Bad But Way Better Than O(n^2), Space Complexity O(n) - Fair

# import math

# numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# def mergeSort(numbers):

#     numbers_length = len(numbers)
    
#     if numbers_length == 1:
#         return  # Handles edge case of list size 1
    
#     half_index = math.floor(numbers_length/2)
    
#     left_half = numbers[0 : half_index]

#     right_half = numbers[half_index+1 : numbers_length-1]

#     print(f'{left_half} | {right_half}')

#     # left_half = sortLeft(left_half)
#     # right_half = sortRight(right_half)

#     numbers = merge(left_half, right_half)

#     return numbers

# def merge(left, right):

#     result = []

#     leftIndex = 0

#     rightIndex = 0

#     while(leftIndex < len(left) and rightIndex < len(right)):
#         if(left[leftIndex] < right[rightIndex]):
#             result.append(left[leftIndex])
#             leftIndex += 1
#         else:
#             result.append(right[rightIndex])
#             rightIndex += 1

#     print(result)

#     return result

# # def sortLeft(left):





# # def sortRight(right):


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" " )
print("\n\n")


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers_length = len(numbers)

print(f'Unsorted : {numbers} count = {len(numbers)}')
mergeSort(numbers, 0, numbers_length - 1)
print(f'Sorted : {numbers} count = {len(numbers)}')