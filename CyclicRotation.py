def solution(A, K):
    # write your code in Python 3.6
    if(len(A)>=0 and len(A)<=100 and K>=0 and K<=100):
        Index = 0
        StoreIndex = [];
        StoreNewIndex = [];
        for i in A:
            StoreIndex.append(Index)
            Index=Index+1
        for i in StoreIndex:
            NewIndex = (i+K)%len(A)
            StoreNewIndex.append(NewIndex)
            
        Result = [x for y, x in sorted(zip(StoreNewIndex, A))]
        return Result
    pass