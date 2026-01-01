# 20920 영단어 암기는 괴로워

import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())

words = []

for _ in range(N):
  word = input().strip()
  if len(word) < M:
    continue
  words.append(word)

counter = Counter(words)

sorted_words = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, freq in sorted_words:
  print(word)