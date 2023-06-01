from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_header_valid(byte_data):
            byte_data &= 0xFF
            if (byte_data >> 7) == 0:
                return True
            elif (byte_data >> 5) == 0b110:
                return True
            elif (byte_data >> 4) == 0b1110:
                return True
            elif (byte_data >> 3) == 0b11110:
                return True

            return False

        def get_char_length(byte_data: int):
            byte_data &= 0xFF;
            if (byte_data >> 7) == 0:
                return 1
            elif (byte_data >> 5) == 0b110:
                return 2
            elif (byte_data >> 4) == 0b1110:
                return 3
            elif (byte_data >> 3) == 0b11110:
                return 4

            return 0

        i = 0
        while i < len(data):
            val = data[i]
            val &= 0xFF
            if not is_header_valid(val):
                return False
            char_length = get_char_length(val)
            if i + char_length > len(data):
                return False
            for j in range(1, char_length):
                if (data[i+j] >> 6) != 0b10:
                    return False
            i += char_length

        return True


data = [197,130,1]
data = [235,140,4]
ret = Solution().validUtf8(data)
print(ret)