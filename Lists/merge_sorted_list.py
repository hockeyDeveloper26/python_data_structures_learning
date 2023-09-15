import logging as log

def mergeSortedArrays(list1, list2):

    # Complex solution

    print(f'List1 {list1} and List2 {list2}before merging')

    for count2 in range(len(list2)):
        for count1 in range(len(list1)):
            if(list2[count2]<list1[count1]):
                list1.insert(count1, list2[count2])
                continue
            else:
                pass

    return print(f'Merged Sorted List For Loops O(n^2) {list1}')

mergeSortedArrays([0,3,4,31], [4,6,30])


def mergeSortedArrays2(list1, list2):

    # Better solution

    try:

        print(f'List1 {list1} and List2 {list2}before merging')

        for item in range(len(list2)):
            list1.append(list2[item])

        list1.sort()

        return print(f'Merged Sorted List For Loops O(n+P) {list1}')
    
    except Exception as e:
        log.error(f'Error, please make sure both values passed to the mergeSortedArrays2 function are Lists \\ Error Message: {e}')

mergeSortedArrays2([0,3,4,31], [4,6,30])
# mergeSortedArrays2('a', 3)
array = [1,2,3,4]

print(array[1])