class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        ans = 0
        for shift in range(32):
            a_bit = (a >> shift) & 1
            b_bit = (b >> shift) & 1
            sum_bit = a_bit ^ b_bit ^ c
            c = a_bit & b_bit | c & a_bit | c & b_bit
            ans |= (sum_bit << shift)
        return ans


a = -12
b = -8
ret = Solution().getSum(a, b)
print(bin(ret))