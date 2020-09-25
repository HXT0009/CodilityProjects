
def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    min = 1
    for a in A:
        if a > min:
            return min
        if a > 0:
            min = a+1
    
    return min
    pass
