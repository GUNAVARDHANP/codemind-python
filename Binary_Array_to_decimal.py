n=int(input())
l=list(map(int,input().split()))
s=''
for i in l:
    s+=str(i)
s=int(s)
su=0
i=0
while s:
    su+=(s%10)*(2**i)
    i+=1
    s//=10
print(su)