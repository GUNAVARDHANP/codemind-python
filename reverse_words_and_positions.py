a=input()
m=a.split()
for i in range(len(m)):
    m[i]=(m[i][::-1])
for i in range(len(m)-1,-1,-1):
    print(m[i],end=' ')