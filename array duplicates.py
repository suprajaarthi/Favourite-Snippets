#Your code below
#Dupliates in an Array using Hashing
def get_dups(array):
    ht = {}
    dups = []
    for x in array:
        if x  in ht:
            dups.append(x)
        else:
            ht[x] = x
    return list(set(dups))
    # return ht

a=[1,2,3,4,2,1,3,5,6,7]
print(get_dups(a))
# print only elements that are repeated
