#!/usr/bin/env Python
# coding=utf-8
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def count_first_ones(byte_data):
            one_count = 0
            for bit in bin(byte_data)[2:10]:
                if bit == '0':
                    return one_count
                one_count += 1
            return one_count

        n = len(data)
        first_byte = True
        count = 0
        for i in range(n):
            if first_byte:
                count = count_first_ones(data[i] & 0xFF)
                if count == 8:
                    return False
                if count == 0:
                    continue
                first_byte = False
                count -= 1
            else:
                if bin(data[i])[2:4] != "10":
                    return False
                count -= 1
                if count == 0:
                    first_byte = True

        if count != 0:
            return False

        return True


data = [197,130,1]
ret = Solution().validUtf8(data)
print(ret)