"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
def pow(x,n):
    """
    This function calculates x to the power of n.

    Approach:
    - n can be >0, ==0, <0
    - if n == 0 then return 1
    - To handle n >0, or n<0:
        - Brute force approach would to be to perform a loop to multiply x by itself n times but that would be inefficient
            - eg. x^6 == (x^2)*(x^2)*(x^2) == (x^2)^3
        - We can perform this recursively to find end_product
        - After the end_product is found then return end_product if n>0 or 1/end_product if n<0
    """
    
    result = power_recursive(x,abs(n)) # n<0 is handled by else statement below
    if n >= 0:
        return result
    else:
        return 1/result

def power_recursive(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_recursive(x*x, n//2)
    else:
        return power_recursive(x*x, (n-1)//2) * x

