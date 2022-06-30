n=input()
x=set("AQWSZXDERFCVGTYHBNJUIKMLOP")
c=0
for i in n:
    if i in x:
        c+=1
print(c)