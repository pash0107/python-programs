#counter
from collections import Counter

counter = [1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,2,2,2,2,2,4,4,4,4,5,5,5,5,5]
string = 'The quick brown fox jumps over the head of a lazy dog.'
word = string.split()
index = Counter(word)
print(index.most_common()[:-3-1:-1])
index += Counter()
# print(Counter(word))
# print(sum(index.values()))

# lister = list(index)
# print(lister)

# print(set(index))
print(index)