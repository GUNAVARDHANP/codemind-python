a=input().split()
for i in range(0,len(a),2):
    a[i]=a[i][::-1]
print(' '.join(a))