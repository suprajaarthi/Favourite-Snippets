# https://ide.geeksforgeeks.org/a2m9B6kghb

def triangles(b):
	n=len(b)
	b.sort()
	c=0
	for i in range(0,n-2):
		k=i+2
		for j in range(i+1,n):
			while k<n and b[i]+b[j]>b[k]:
				k+=1
			if k>j:
				c+=k-j-1
	return c

# a=int(input()) 
l=list(map(int,input().split()))
print(triangles(l))


# arr = [ 10, 21, 22, 100, 101, 200, 300 ] 
