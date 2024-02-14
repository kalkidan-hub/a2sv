class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs)//2
        for cost in costs:
            cost.append(cost[0] - cost[1])
        costs.sort(key=lambda x:x[2])

        min_cost = 0
        for i in range(len(costs)):
            if i < n:
                min_cost += costs[i][0] 
            else:
                min_cost += costs[i][1] 

        return min_cost