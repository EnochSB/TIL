# 세 수
import heapq
heap = list(map(lambda x: -int(x), input().split()))
heapq.heapify(heap)
heapq.heappop(heap)
print(-heapq.heappop(heap))