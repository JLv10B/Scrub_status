"""
Datastructures:
Lists
Dictionary
Tuple
Set
Linked List
Tree
"""
# def create_list(array):
#     result_big = [x for x in array if x > 5]
#     print(f'result_big list comprehension  = {result_big}')
#     result_small = [x*2 for x in array if x < 5]
#     print(f'result_small list comprehension = {result_small}')
    
#     for i in result_big:
#         result_big.append(i+1)
#     print(f'result_big append = {result_big}')

#     result_big.extend(result_small)
#     print(f'result_big extend = {result_big}')
#     print(f'result_small= {result_small}')

#     return result_big, result_small


# def create_dict(array1, array2):
#     new_dict = {key:value for (key,value) in zip(array1, array2)}
#     print(f'new dictionary with comprehension = {new_dict}')

#     for key, value in new_dict.items():
#         if key % 2 == 0:
#             del new_dict[key]
def container_function(n):
    memo = {}
    return fibonacci_recursive(n, memo)
    
def fibonacci_recursive(n, memo):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    elif n in memo:
        return memo[n]

    # Recursive case
    else:
        memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
        return memo[n]

        
# Testing:
if __name__ == "__main__":
    # array = [1,2,3,4,5,6,7,8,9,0,12,14,15,16,17,128]
    # create_list(array)
    # create_dict(result_big, result_small)
    container_function(5)