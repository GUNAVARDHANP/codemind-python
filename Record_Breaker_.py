for j in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    if l[0]>l[1]:
        c+=1
    if max(l)==l[-1] and l.count(l[-1])==1:
        c+=1
    for i in range(1,n-1):
        if l[i]>l[i+1]:
            if max(l[0:i+1])==l[i] and l[0:i+1].count(l[i])==1:
                c+=1
    print('Case #'+str(j+1)+':',c)