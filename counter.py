from collections import Counter
from string import punctuation # one-trick pony

count = Counter()

for line in open('hamlet.txt'):
    line = ''.join([char for char in line.lower()
                if char not in punctuation])
    count.update(line.split())
    
print(count.most_common(10))
