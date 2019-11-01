class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(result, lst, k, range_n):
            if k == 0:
                result.append(lst)
            else:
                for i in range(len(range_n)):
                    dfs(result, lst + [range_n[i]], k - 1, range_n[i+1:])
        
        
        if k > n:
            return False
        result = []
        lst = []
        dfs(result, lst, k, range(1, n + 1, 1))
        return result