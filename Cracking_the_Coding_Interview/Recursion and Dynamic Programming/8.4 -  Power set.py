"""
Write a method to return all subsets of a set.

Input: 
Output: [[3,4,5], [7,8,9]]



"""
def stair(cost):
    print(cost)
    last_stair = cost.pop()
    print(last_stair)
    second_last_stair = cost.pop()
    print(second_last_stair)
    print(cost)
    return min(last_stair, second_last_stair)

# Test:

if __name__ == "__main__":
    # cost = [1,100,1,1,1,100,1,1,1]
    cost = [1]
    print(stair(cost))