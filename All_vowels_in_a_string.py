n=input()
s="aeiou"
l=[]
for i in n:
    if i in s:
        l.append(i)
a=set(l)
if(len(s)==len(a)):
    print("True")
else:
    print("False")


        