def queen(A, cur=0):
    global queens
    if cur==len(A):
        queens+=1
        print(A)
        print("现在有",queens,"种方法")
        return 0
    for col in range(len(A)):
        A[cur],flag=col,True
        for row in range(cur):
            if A[row]==col or abs(col-A[row])==cur-row:
                flag=False
                break
        if flag:
            queen(A,cur+1)


queens=0
queen([None]*8)

