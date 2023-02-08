# 절댓값 힙
import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (num, num) if num > 0 else (-num, num))