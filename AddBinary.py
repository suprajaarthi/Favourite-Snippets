# https://ide.geeksforgeeks.org/UaRrBfT12v

def addBinary(a,b):
    a_num = int(a,2)
    b_num = int(b,2)
    total = a_num + b_num
    x = bin(total).replace('0b',"")
    return x
# 1010
# 1011
#10101

print(addBinary("1010", "1011"))
