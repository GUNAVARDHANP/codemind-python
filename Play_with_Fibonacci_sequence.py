n=int(input())
f=0
s=1
c=2
print(0,1,end=' ')
while c<n:
    sum=f+s
    print(sum,end=' ')
    f=s
    s=sum
    c+=1