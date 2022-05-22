def prime(psum):
    if psum==0 or psum==1:
        return False
    else:
        for i in range(2,int(psum**0.5)+1):
            if psum%i==0:
                return False
        else:
            return True
a=int(input())
b=int(input())
sum=a+b
psum=sum+1
while (1):
    if prime(psum):
        print(psum-sum)
        break
    else:
        psum=psum+1