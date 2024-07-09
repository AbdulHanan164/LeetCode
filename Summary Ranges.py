class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        result = []
        start_range = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                end_range = nums[i-1]
                if start_range == end_range:
                    result.append(str(start_range))
                else:
                    result.append("{}->{}".format(start_range, end_range))
                start_range = nums[i]
        
        # Add the last range
        if start_range == nums[-1]:
            result.append(str(start_range))
        else:
            result.append("{}->{}".format(start_range, nums[-1]))
        
        return result
