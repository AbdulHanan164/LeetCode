class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Sort candidates to ensure ascending order
        
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(current_combination[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break  # No need to check further, candidates are sorted
                current_combination.append(candidates[i])
                backtrack(i, target - candidates[i], current_combination)
                current_combination.pop()
        
        result = []
        backtrack(0, target, [])
        return result
