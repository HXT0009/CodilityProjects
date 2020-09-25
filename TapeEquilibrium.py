def solution(A):
    # write your code in Python 3.6
    LeftSum = 0
    RightSum = sum(A)
    Diff = float('inf')
    for i in A:
        LeftSum = LeftSum + i
        RightSum = RightSum-i
        
        diff = abs(LeftSum - RightSum)
        if(diff<Diff):
            Diff=diff
    return Diff
    pass
