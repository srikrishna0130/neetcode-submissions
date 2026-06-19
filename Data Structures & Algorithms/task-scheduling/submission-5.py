class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_map = Counter(tasks)
        maxheap = [ [-tasks_map[key], key] for key in tasks_map ]
        heapq.heapify(maxheap)

        taskq = deque()
        step = 0
        steps = []
        cooldown = n

        while maxheap or taskq:
            if taskq and taskq[0]:
                next_step, next_count, task = taskq[0]
                if step + 1 >= next_step:
                    heapq.heappush(maxheap, [-next_count, task])
                    taskq.popleft()
            
            if maxheap:
                count, task = heapq.heappop(maxheap)
                step += 1
                steps.append(task)
    
                if count*-1 != 1:
                    # next_step, next_count, task
                    taskq.append([step + cooldown + 1, -count - 1, task])
            else:
                step += 1
                steps.append("idle")
        
        return step

