https://ide.geeksforgeeks.org/7BtcuLUsxq

a=input().strip()
b='aeiouAEIOU'
s,d=[],''
# let a= 'environment'
for i in range(len(a)):
	if a[i] in b:
  #  Get index of str bfr & after vowels 
#  		nvrnmn  => [1,2,4,6,7,9]
	    s.append(i-1)
	    s.append (i+1)
print(s)      
# If str not in vowel list print str
# print chars in 0,3,5,8 pos
for i in range(len(a)):
	if i not in s:
		d+=a[i]

print(d)

# environment => eioet
 
  
  
