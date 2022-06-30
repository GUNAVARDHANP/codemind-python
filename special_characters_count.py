n=input()
l=[]
c=0
x=set("!@#$%^&*()_+~`=-<>?''/.,;\|[]{}")
for i in n:
    if i in x:
        c+=1
print(c)