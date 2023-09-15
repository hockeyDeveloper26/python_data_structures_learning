def reverseList(list):

    reverse = []

    list_copy = list.copy()

    length_of_list = (len(list))

    # reverse = list.index(length_of_list, 0)

    for count in range(len(list_copy)):
        if(length_of_list > 0):
            reverse.append(list_copy.pop(-1))
        elif(length_of_list == 1):
            reverse.append(list_copy.pop(0))
        else:
            pass


    print(reverse)


    list.reverse()

    print(list)

    return print(list)

reverseList([1,2,3,4])