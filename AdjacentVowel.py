a=input().strip()
b='aeiouAEIOU'
s,d=[],''
for i in range(len(a)):
	if a[i] in b:
  #  Get index of str bfr & after vowels 
	    s.append(i-1)
	    s.append (i+1)
      
# If str not in vowel list print str
for i in range(len(a)):
	if i not in s:
		d+=a[i]

print(d)


# environment => eioet
 
  
  
