class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        final = int(s) +1
        new_list = list(str(final))

        for j in range(len(new_list)):
            number = int(new_list[j])
            new_list[j] = number
        return new_list
            
