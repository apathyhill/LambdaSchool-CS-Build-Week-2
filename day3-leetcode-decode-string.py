# Problem:
# Decode String

# URL: 
# https://leetcode.com/problems/decode-string/

# Solution:
class Solution:
    def decodeString(self, s: str) -> str:
        final_str = ""
        number = ""
        repeat_list = []
        for char in s:
            if char in "1234567890":
                number += char
            elif char == "[":
                repeat_list.append([int(number), ""])
                number = ""
            elif char == "]":
                temp_list = repeat_list.pop(-1)
                temp_str = temp_list[0] * temp_list[1]
                if len(repeat_list) > 0:
                    repeat_list[-1][1] += temp_str
                else:
                    final_str += temp_str
            else:
                if len(repeat_list) > 0:
                    repeat_list[-1][1] += char
                else:
                    final_str += char
        return final_str