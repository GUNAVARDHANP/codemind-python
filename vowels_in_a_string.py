s=input()
x=input()
vowel=set("aeiouAEIOU")
for i in range(0,len(s)):
    if s[i] in vowel:
        if s[i]==x:
            print(True)
            print(i)
            break
            
else:
    print(False)