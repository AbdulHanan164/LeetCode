class Solution:
    def insert(self, intervals, newInterval):
        result = []
        start, end = newInterval[0], newInterval[1]
        inserted = False
        
        for interval in intervals:
            if interval[1] < start:
                # No overlap and current interval is before newInterval
                result.append(interval)
            elif interval[0] > end:
                # No overlap and current interval is after newInterval
                if not inserted:
                    result.append([start, end])
                    inserted = True
                result.append(interval)
            else:
                # Overlap, update the newInterval
                start = min(start, interval[0])
                end = max(end, interval[1])
        
        if not inserted:
            result.append([start, end])
        
        return result
