a=input()
b=input()
l=list(a)
for i in range(len(l)):
    if l[i]==b:
        print(True)
        print(i)
        break
else:
    print(False)