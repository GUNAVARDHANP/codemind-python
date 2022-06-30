string=input()
l=[]
res=[]
vowels=set("aeiouAEIOU")
for i in range(0,len(string)):
    if string[i] in vowels:
       l.append(string[i])
res = []
for i in l:
    if i not in res:
        res.append(i)
print(*res)