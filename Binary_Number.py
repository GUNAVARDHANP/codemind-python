n=int(input())
for i in range(2**n):
    b=len("{:b}".format(i))
    if b<n:
        for j in range(n-b):
            print(0,end='')
        print("{:b}".format(i))
    else:
        print("{:b}".format(i))