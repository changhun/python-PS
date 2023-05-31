class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_ret = x ^ y
        return bin(xor_ret).count('1')
