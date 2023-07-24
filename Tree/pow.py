

class Solution:

    def assistPow(self,x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = self.assistPow(x, n // 2)
        result = result * result
        if n % 2:
            return result * x
        else:
            return result

    def myPow(self, x: float, n: int) -> float:


        if n >= 0: return self.assistPow(x, n)
        elif n < 0:
            return 1/ self.assistPow(x, abs(n))



if __name__ == '__main__':
    s1 = Solution()
    print(s1.myPow(2.00000, 10))
    print(s1.myPow(2.10000, 3))