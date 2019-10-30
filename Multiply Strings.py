class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0 for i in range(len(num1))]
        for i in range(len(num1) - 1, -1, -1):
            n = 0
            res = 0
            for j in range(len(num2) - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                if j == 0:
                    result[len(num1) - 1 - i] += (multi + res) * pow(10, n) 
                else:
                    result[len(num1) - 1 - i] += (multi % 10 + res) * pow(10, n) 
                    res = multi // 10
                    n += 1
        output = 0
        for i in range(len(result)):
            output += result[i] * pow(10, i)
        return str(output)