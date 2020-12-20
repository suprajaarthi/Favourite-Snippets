a=input().strip()
b=input().strip()
afreq=[0]*26
bfreq=[0]*26
c=0
for i in a:
    afreq[ord(i)-ord('a')]+=1
for j in b:
    bfreq[ord(j)-ord('a')]+=1
for i in range(26):
    c+=min(afreq[i],bfreq[i])
   
print(afreq)
print(bfreq)
print(c)

