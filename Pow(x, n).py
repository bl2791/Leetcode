class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        arr = []
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n
            
        while True:
            loop = 1
            num = x
            while loop < n:
                num = num * num
                loop = 2 * loop
            if loop == n:
                arr.append(num)
                break
            arr.append(math.sqrt(num))
            n = n - loop/2
        result = 1
        for i in arr:
            result = result * i
        return result


Another solution —— Recursive:
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)