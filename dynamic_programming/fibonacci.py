# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ....


# This version of fibonacci above is Time O(2^n) which is very bad
# but this can be improved with Dynamic Programming


# calculations = 0

def fibonacci(n):
    

    # calculations += 1

    if(n < 2):
        return n
    

    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6)) 

# Notice how the number in index 6 at the top 
# is 8 compared to the return value for fibonacci(6)


# This version of fibonacci has been improved to a
# Time Complexity O(n) from O(2^n) thanks to 
# Dynamic Programming: Memoization/caching and recursion

cache = {}


def fibonacciMaster(n):

    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
    return fib(n)


fasterFib = fibonacciMaster

print(f'DP {fasterFib(10)}')







def fibonacciMaster2(n):

    cache = [0,1]
    for item in range(2, n):
        cache.append(cache[item -2] + cache[item -1])

    return cache.pop()

print(fibonacciMaster2(5))

# fibonacci_cache = {}

# def fibonacci_dp(n):
    

#     # calculations += 1

#     def fibonacci_equation(n):

#         return fibonacci(n-1) + fibonacci(n-2)

    

#     fibonacci_cache[n] = fibonacci_equation

#     if(n < 2):
#         return n
#     elif(n in fibonacci_cache.keys()):
#         print(f'pulled from cache!')
#         return fibonacci_cache[n]
#     else:
#         new_num = fibonacci_equation(n)
#         fibonacci_cache[n] = new_num
#         return fibonacci_dp(n)
    
#     # fibonacci_cache[n] = fibonacci_equation

#     # fibonacci_equation = fibonacci(n-1) + fibonacci(n-2)

#     # return fibonacci_equation

# print(fibonacci_dp(6)) 
# print(fibonacci_dp(4))
# print(fibonacci_dp(6))
