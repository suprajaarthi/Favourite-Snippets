def vow(a):
    c=0
    for i in a:
        if i in 'aeiou':
            c+=1
    return c

l=list(map(str,input().split()))    
s=sorted(l,key=lambda x:vow(x))
print(*s)


