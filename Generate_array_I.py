n=int(input())
l=list(map(int,input().split()))
ll=[]
for i in range(0,len(l),2):
    for j in range(l[i+1]):
        ll.append(l[i])
print(*ll)