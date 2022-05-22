def prime(i):
    if i==0 or i==1:
        return False
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        else:
            return True
def palindrome(i):
    temp=i
    rev=0
    while temp>0:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==i:
        return True
    else:
        return False
n=int(input())
for i in range(n+1,(20*n)+1):
    if prime(i) and palindrome(i):
        print(i)
        break