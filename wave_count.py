n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l),2):
    if i<=len(l)-3:
        if l[i]<l[i+1] and l[i+1]>l[i+2]:
            c+=1
        else:
            print(-1)
            break
else:
    print(c)