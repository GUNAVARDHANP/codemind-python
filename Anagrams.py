n=input()
m=input()
n=n.lower()
m=m.lower()
n=sorted(n)
m=sorted(m)
if set(n)==set(m):
    print("True")
else:
    print("False")