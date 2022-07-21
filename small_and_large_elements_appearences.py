l=[]
for i in input():
    if i.isalnum():
        l.append(ord(i))
print(chr(min(l)),l.count(min(l)),chr(max(l)),l.count(max(l)))