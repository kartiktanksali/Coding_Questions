from collections import Counter

def Solution(A):
    mode = Counter(A)
    m = mode.most_common(1)[0][0]
    count=0
    if m==0:
        rep = 1
    else:
        rep = 0
    for i in range(len(A)):
        if A[i]!=m:
            A[i]=rep
            count+=1
    return count

A = [1,1,0,0,0,0,1,1,0]
res = Solution(A)
print(res)
    