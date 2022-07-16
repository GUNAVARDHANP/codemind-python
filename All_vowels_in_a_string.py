a=input()
l=[]
for i in a:
    if i in 'aeiouAEIOU' and i not in l:
        l.append(i)
l=sorted(l)
if 'aeiou' in ''.join(l) or 'AEIOU' in ''.join(l):
    print(True)
else:
    print(False)