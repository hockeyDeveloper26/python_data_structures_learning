# Selection Sort : Time Complexity O(n^2) = Bad, Space Complexity O(1) - Great

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionsort(numbers):

    numbers_length = len(numbers)

    for num in range(numbers_length):
        min_num_index = num

        for num2 in range(num+1, numbers_length):

            # select the minimum element in every iteration
            if numbers[num2] < numbers[min_num_index]:
                min_num_index = num2

        # swapping the elements to sort the array
        (numbers[num], numbers[min_num_index]) = (numbers[min_num_index], numbers[num])

    return numbers

print(f'Unsorted : {numbers} count = {len(numbers)}')
print(f'Sorted : {selectionsort(numbers)} count = {len(numbers)}')
