def prime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0 and prime(i)==False:
        c+=1
print(c)