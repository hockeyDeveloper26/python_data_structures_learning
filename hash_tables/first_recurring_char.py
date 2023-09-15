# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1
# Given an array = [2,3,4,5]
# It should return undefined

test_case1 = [2,5,1,2,3,5,1,2,4]

test_case2 = [2,1,1,2,3,5,1,2,4]

test_case3 = [2,3,4,5]


def recurring_char(chars):   # O(n^2)
    
    index = float('inf')

    for item in range(len(chars)):
        for item2 in range(item+1, len(chars)):
            if(chars[item2]==chars[item]):
                if(item2 < index):
                    index = item2


    if(index != float('inf')):               
        return print(chars[index])
    else:
        return print('No recurring characters found')
    

def recurring_char2(chars):  # O(n)

    chars_count = {}

    for char in range(len(chars)):
        if chars[char] in chars_count:
            return print(chars[char])
        else:
            chars_count[chars[char]] = 0

    return print('No recurring characters')

   

# recurring_char(test_case1)

# recurring_char(test_case2)

# recurring_char(test_case3)

recurring_char2(test_case1)

recurring_char2(test_case2)

recurring_char2(test_case3)