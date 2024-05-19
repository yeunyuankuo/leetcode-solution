class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time: best O(N), worst: O(N * M), N is the legnth of tasks, and M is n,
        # becuase we might have tasks that are all A's, the we need to wait N idle time after each A
        # space: O(26)
        count = Counter(tasks) # count all tasks frequency
        maxHeap = [-cnt for cnt in count.values()] # we need negative count for maxHeap, b/c python doesn't have built in maxHeap
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # [count, idle time needed]
        while queue or maxHeap:
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

            time += 1

        return time
    
    def leastIntervalGreedy(self, tasks: List[str], n: int) -> int:
        # Greedy Approach
        # time: O(N)
        # space: O(26)
        count = Counter(tasks) # count all tasks frequency
        maxCount = max(count.values())

        minTime = (maxCount - 1) * (n + 1)
        for f in count.values():
            if f == maxCount:
                minTime += 1
        
        return max(len(tasks), minTime)