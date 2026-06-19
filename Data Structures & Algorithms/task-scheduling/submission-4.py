class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = Counter(tasks).most_common()
        freq_count = task_map[0][1]
        
        m = sum(1 for _, freq in task_map if freq == freq_count)
        
        structural_time = (freq_count - 1) * (n + 1) + m
        return max(len(tasks), structural_time) 