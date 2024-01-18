

class Solution:
    def changeMoney(self, money):
        divs = [500, 100, 50, 10]
        ans = 0
        for div in divs:
            #quotient, remainder = money//div, money%div
            quotient, remainder = divmod(money, div)
            ans += quotient
            money = remainder
            #print(div, quotient)
        return ans

money = 2370
ans = Solution().changeMoney(money)
print(ans)