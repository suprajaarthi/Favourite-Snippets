#combination of k elements that equals n 
import itertools
k,n=map(int,input().split())
res=[] 
lst=list(map(list,list(itertools.combinations([x for x in range(1,10)], k)))) 
res=[x for x in lst if sum(x)==n]
print(res)
        