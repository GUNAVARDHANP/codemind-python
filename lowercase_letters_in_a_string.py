n=input()
c=0
x=set("aqwsedzxcfrtgvbhyujnmkiolp")
for i in n:
    if i in x:
        c+=1
print(c)