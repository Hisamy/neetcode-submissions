class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for f in freq.values() if f == max_freq)
        
        # Calculate minimum intervals based on the most frequent task
        min_intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Return the maximum of calculated intervals or total tasks
        return max(min_intervals, len(tasks))

        