class Solution:
    def permute(self, nums):
        def backtrack(current, used):
            # Base case: If current permutation is complete
            if len(current) == len(nums):
                result.append(current[:])  # Make a copy of current
                return
            
            for num in nums:
                if num not in used:
                    # Choose
                    current.append(num)
                    used.add(num)
                    
                    # Explore
                    backtrack(current, used)
                    
                    # Unchoose (backtrack)
                    current.pop()
                    used.remove(num)
        
        result = []
        backtrack([], set())
        return result
