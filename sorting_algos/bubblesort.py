# Bubble Sort Time : Complexity O(n^2) - Bad, Space Complexity O(1) - Great

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubblesort(numbers):

    numbers_length = len(numbers)

    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process

    swapped = False

    # Traverse through all array elements

    for num1 in range(numbers_length-1):    #O(n)

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place

        for num2 in range(0, numbers_length-num1-1):    # O(n)

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element

            if numbers[num2] > numbers[num2 + 1]:
                swapped = True
                numbers[num2], numbers[num2 + 1] = numbers[num2 + 1], numbers[num2]

        if not swapped:

            # if we haven't needed to make a single swap, we
            # can just exit the main loop.

            return

    return numbers


print(f'Unsorted : {numbers} count = {len(numbers)}')
print(f'Sorted : {bubblesort(numbers)} count = {len(numbers)}')


# Bubble Sort : Time Complexity O(n^2) - Bad, Space Complexity O(1) - Great

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubblesort2(numbers):

    numbers_length_cap = len(numbers)-1


    index = 0

    count = 0

    while count < numbers_length_cap: # O(n)
        if numbers[index] > numbers[index+1]: #O(1)
            numbers[index], numbers[index+1] = numbers[index+1], numbers[index]
        index += 1

        if index == numbers_length_cap: #O(n)
            count +=1
            index = 0

    return numbers

print(f'Unsorted : {numbers} count = {len(numbers)}')
print(f'Sorted : {bubblesort2(numbers)} count = {len(numbers)}')
        