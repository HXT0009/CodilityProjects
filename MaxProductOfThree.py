def solution(A):
    # write your code in Python 3.6
    SortedA = sorted(A)
    NumberA = len(A)
    
    CombinA = SortedA[NumberA-3:NumberA]
    CombinB = SortedA[0:3]
    CombinC1 = SortedA[NumberA-1]
    CombinC2 = SortedA[0:2]
    
    Value1= 1
    Value2 = 1
    Value4 = 1
    
    for i in CombinA:
        Value1=Value1*i
    for i in CombinB:
        Value2=Value2*i
    for i in CombinC2:
        Value4 = Value4*i
    
    Value4 = Value4*CombinC1
    
    
    Store = []
   
    Store.append(Value1)
    Store.append(Value2)
    Store.append(Value4)
    if(0 in A):
        Store.append(0)
    
    return max(Store)
    pass