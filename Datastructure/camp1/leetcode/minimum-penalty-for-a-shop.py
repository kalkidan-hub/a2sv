class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # the zero, one problem in real life scenario, ha

        # keep track number of "N"s from the left and number of "Y"s from the right

        totalY = sum([cust == 'Y' for cust in (customers)])
        No = 0
        Yes = 0
        close_hour, min_penality = len(customers), inf

        for j in range(len(customers)):
            
            # calculate my penality had I closed now
            penality = No + (totalY - Yes)
            
            if penality < min_penality:
                close_hour = j
                min_penality = penality

            No += (customers[j] == 'N')
            Yes += (customers[j] == 'Y')
        
        return j + 1 if No + (totalY - Yes) < min_penality else close_hour