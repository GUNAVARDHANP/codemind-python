a=input()
m=a.split()
for i in range(len(m)):
    m[i]=(m[i][::-1])
    print(m[i],end=' ')