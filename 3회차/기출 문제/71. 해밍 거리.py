class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ret = 0
        while xor:
            ret += (xor & 1)
            xor &= xor - 1
            ret += 1
        return ret