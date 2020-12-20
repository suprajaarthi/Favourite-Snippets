# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# Compare string by frequency of the smallest character


queries=list(map(str,input().split()))
words=list(map(str,input().split()))
query_freqs = [s.count(min(s)) for s in queries]
word_freqs = [s.count(min(s)) for s in words]
print(query_freqs)
print(word_freqs)
result = [0] * len(query_freqs)
for i,q in enumerate(query_freqs):
    for w in word_freqs:
        if q < w:
            result[i] += 1
print(result)
