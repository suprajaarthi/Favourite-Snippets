#eliminate adjacent vowels in a string
a=input().strip()
b='aeiouAEIOU'
s,d=[],''
for i in range(len(a)):
	if a[i] in b:
	    s.append(i-1)
	    s.append (i+1)
for i in range(len(a)):
	if i not in s:
		d+=a[i]

print(d)