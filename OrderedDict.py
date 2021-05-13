from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1
   
print(len(words))
print(*words.values())

# ip:
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# op:
# 3
# 2 1 1
