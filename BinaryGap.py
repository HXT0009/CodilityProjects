def solution(N):
    # write your code in Python 3.6
    list = []
    listTemp = []
    if(N>=1 and N<=2147483647):
        BinN = bin(N).replace('0b', '')
        count = 0
        for i in BinN:
            count = count+1
            if(i == '1'):
                list.append(count)
        if(len(list)==1):
            return 0
        if(len(list)>1):
            for j in range(1, len(list)):
                listTemp.append(list[j]-list[j-1]-1);
            return max(listTemp)
    else:
        return 0
    pass