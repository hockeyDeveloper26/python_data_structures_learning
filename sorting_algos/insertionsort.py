# Insertion Sort : Time Complexity O(n^2) = Bad, Space Complexity O(1) - Great

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertionsort(numbers):

    numbers_length = len(numbers)   # Length of List

    if numbers_length <= 1:  #Edge Case if list is length of 1, already sorted
        return
   
    for num in range(1, numbers_length):    # Iterate over the array starting from the second element
        key = numbers[num]  # Store the current element as the key to be inserted in the right position
        num2 = num - 1
        while num2 >= 0 and key < numbers[num2]:    # Move elements greater than key one position ahead
            numbers[num2+1] = numbers[num2]     # Shift elements to the right
            num2 -= 1
        numbers[num2+1] = key   # Insert the key in the correct position

    return numbers

print(f'Unsorted : {numbers} count = {len(numbers)}')
print(f'Sorted : {insertionsort(numbers)} count = {len(numbers)}')