# https://www.hackerrank.com/challenges/word-order/problem


from collections import OrderedDict
words = OrderedDict()
for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    print(words)
    words[word] += 1
   
print(len(words))
print(*words.values())


# https://ide.geeksforgeeks.org/9fLvsfmCtR
