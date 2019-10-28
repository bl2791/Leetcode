class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        def Sum(result, candidates, lst, target):
            if target == 0:
                result.append(lst)
            elif target > 0:
                for i in range(len(candidates)):
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    if i < len(candidates) - 1:
                            Sum(result, candidates[i + 1:], lst + [candidates[i]], target - candidates[i])
                    else:
                        if candidates[i] == target:
                            result.append(lst + [candidates[i]])
        
        result = []
        lst = []
        Sum(result, candidates, lst, target)
        return result
