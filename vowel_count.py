s=input()
c=0
vowel=set("aeiouAEIOU")
for i in range(0,len(s)):
    if s[i] in vowel:
        c+=1
print(c)
    
       