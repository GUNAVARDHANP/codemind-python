n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            ans.append(j-i)
            break
    else:
        ans.append(0)
print(*ans)