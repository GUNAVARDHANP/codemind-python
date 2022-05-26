n=int(input())
for i in range(n):
    b=int(input())
    a=input()
    for j in a:
        c=0
        for k in a:
            if j==k and j.isdigit()==False and k.isdigit()==False:
                c+=1
        if c==1:
            print(j)
            break
    else:
        print(-1)