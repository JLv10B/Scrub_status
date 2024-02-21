"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

ex
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

req:
- find how many of each element in the array
- return the top k elements

- sort in place then return the first 

element_count = {}
result = []
"""
def find_k_elements(nums, k):
    element_count = {}

    for n in nums:
        if n in element_count:
            element_count[n] += 1
        else:
            element_count[n] = 1
    
    freq = [[] for i in nums]
    print(freq)

    for val, count in element_count.items():
        freq[count].append(val)
    
    ans = []
    for index in range(len(freq)-1, 0, -1):
        for n in freq[index]:
            ans.append(n)
            if len(ans) == k:
                return ans

# Testing
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(find_k_elements(nums, k))


