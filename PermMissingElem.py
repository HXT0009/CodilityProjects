def solution(A):
    # write your code in Python 3.6
    Size = len(A)+1
    SumA = Size * (Size+1)/2
    SumB = sum(A)
    Missing = int(SumA - SumB)
    return Missing
    pass
