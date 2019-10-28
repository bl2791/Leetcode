class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combine(digits, idx, string, result):
            if digits == "":
                return
            if idx == len(digits):
                result.append(string)
            else:
                for j in range(len(letter[int(digits[idx]) - 1])):
                    combine(digits, idx + 1, string + letter[int(digits[idx]) - 1][j], result)
        
        letter = ['', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        global letter
        result = []
        string = ''
        combine(digits, 0, string, result)
        return result
