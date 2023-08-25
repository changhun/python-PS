class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ret = 0
        while xor:
            ret += (xor & 1)
            xor >>= 1

        return ret