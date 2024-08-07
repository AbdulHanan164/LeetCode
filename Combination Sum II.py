class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # Sort candidates to handle duplicates
        result = []
        
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(current_combination[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # No need to check further, candidates are sorted
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)
                current_combination.pop()
        
        backtrack(0, target, [])
        return result
