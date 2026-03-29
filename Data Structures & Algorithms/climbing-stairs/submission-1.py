class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        for i in range(1, n+1):
            if i == 1:
                res.append(1)
            elif i ==2:
                res.append(2)
            else:
                print(res)
                res.append(res[i-2] + res[i-3])
        return res[len(res)-1]

