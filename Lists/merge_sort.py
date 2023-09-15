import heapq


# def merge_sort(arr):
#     if len(arr) > 1:
#         left_arr = arr[:len(arr) // 2]
#         right_arr = arr[len(arr) // 2 : ]

#         # recursion
#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         # merge
#         numLeftIndex = 0
#         numRightIndex = 0
#         numMergedIndex = 0

#         while numLeftIndex < len(left_arr) and numRightIndex < len(right_arr):
#             if left_arr[numLeftIndex] < right_arr[numRightIndex]:
#                 arr[numMergedIndex] = left_arr[numLeftIndex]

#                 numLeftIndex += 1
                
            
#             else:
#                 arr[numMergedIndex] = right_arr[numRightIndex]
#                 numRightIndex += 1
                

#             numMergedIndex += 1

#         while numLeftIndex < len(left_arr):
#             left_arr[numLeftIndex] = left_arr[numLeftIndex]   
#             numLeftIndex += 1
#             numMergedIndex += 1

#         while numRightIndex < len(right_arr):
#             arr[numMergedIndex] = right_arr[numRightIndex]
#             numRightIndex += 1
#             numMergedIndex += 1



# arr_test = [2,3,5,1,7,4,4,4,2,6,0]

# print(arr_test)

# merge_sort(arr_test)

# print(arr_test)

def merge_sort(array):

    if(len(array) == 1):
        return array

    print(array.count(4))
    print(array.count(2))

    arrayLeft = [array[0: len(array) // 2]]
    arrayRight = [array[len(array) // 2 : ]]

    print(arrayLeft, arrayRight)

    def merge(arrayLeft, arrayRight):

        merged = []
        
        leftIndex = 0
        rightIndex = 0

        # print(heapq.heapify(arrayLeft))



        while(leftIndex < len(arrayLeft) and rightIndex < len(arrayRight)):
            

            # print(arrayLeft.count)

            if(arrayLeft[leftIndex] < arrayRight[rightIndex]):
                merged.append(arrayLeft[leftIndex])
                leftIndex+=1
            
            else:
                merged.append(arrayRight[rightIndex])
                rightIndex+=1

        # merged.append(arrayLeft)
        # merged.append(arrayRight)

        return merged

    return merge(arrayLeft, arrayRight)


arr_test = [2,3,5,1,7,4,4,4,2,6,0]

print(merge_sort(arr_test))