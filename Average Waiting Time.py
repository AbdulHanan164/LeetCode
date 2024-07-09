class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time in customers:
            current_time = max(current_time, arrival)  # Chef starts the current order at max(current_time, arrival)
            current_time += time  # Chef finishes the current order
            
            waiting_time = current_time - arrival
            total_waiting_time += waiting_time
        
        return float(total_waiting_time) / len(customers)
