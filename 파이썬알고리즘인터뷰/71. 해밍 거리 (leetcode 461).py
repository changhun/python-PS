class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = bin(x ^ y).count('1')
        return ans