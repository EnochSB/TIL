# 단어 정렬
import heapq
words = set()
for _ in range(int(input())):
    word = input()
    words.add(word)
heap = list(words)
heapq.heapify(heap)

print(*heapq.nsmallest(len(heap), heap, key= lambda x: (len(x), x)), sep='\n')