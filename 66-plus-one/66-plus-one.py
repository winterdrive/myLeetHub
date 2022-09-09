class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index=-1
        if digits[index]!=9:
            digits[index]=digits[index]+1
            return digits
        else:
            while digits[index]==9:
                digits[index]=0
                if digits[0]==digits[index]:
                    digits.insert(0,1)
                    return digits
                index=index-1
            digits[index]=digits[index]+1
            return digits