#  Memoization 1

def addTo80(n):
    print('long time')
    return n + 80

cache = {}

def memoizedAddTo80(n):
    if n in cache.keys():
        return cache[n]
    else:
        print('long_time')
        cache[n] = 5 + 80
        return cache[n]

# print(f'1 : {memoizedAddTo80(5)}')
# print(f'2 : {memoizedAddTo80(5)}')


# Memoization 2

def addTo80(n):
    print('long time')
    return n + 80



cache = {}

def closureMemoizedAddTo80(n):

    def process_logic(n):
        print(cache)
        if n in cache.keys():
            return cache[n]
        else:
            print('long_time')
            cache[n] = 5 + 80
            return cache[n]
        
    return  process_logic(n)    # Closures in Python is creating an inner function and calling it

               
memoized = closureMemoizedAddTo80

print(f'1 : {memoized(5)}')
print(f'2 : {memoized(5)}')