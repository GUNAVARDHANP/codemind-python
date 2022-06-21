def selfd(n):
    if n<10:
        return True
    else:
        c=0
        pc=0
        temp=n
        while temp:
            d=temp%10
            if d==0:
                return False
            elif n%d!=0:
                return False
            else:
                c+=1
            pc+=1
            temp//=10
        if c==pc:
            return True
        else:
            return False
n=int(input())
m=int(input())
while n<=m:
    if selfd(n):
        print(n,end=' ')
    n+=1