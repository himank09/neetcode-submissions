class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap_heap = list(zip(capital, profits))
        heapq.heapify(min_cap_heap)
        max_profit_heap = []

        for _ in range(k):
            while min_cap_heap and min_cap_heap[0][0] <= w:
                c, p = heapq.heappop(min_cap_heap)
                heapq.heappush(max_profit_heap, -p)
       

            if not max_profit_heap:
                break

            w += -heapq.heappop(max_profit_heap)

        return w 