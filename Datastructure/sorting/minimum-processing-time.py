class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        time = 0
        for i in range(3,len(tasks),4):
            t = max(tasks[i-1],tasks[i-2],tasks[i-3],tasks[i])
            time = max(time,t + processorTime[(i//4)])
        return time