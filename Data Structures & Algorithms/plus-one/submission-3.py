class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0

        if digits[-1] == 9:
            rem = 1
            for i in range(len(digits)-1, -1, -1):
                if digits[i] + rem == 10:
                    digits[i] = 0
                    rem = 1
                else:
                    digits[i] = digits[i] + rem
                    rem = 0
            if rem == 1:
                digits.insert(0,1)
            return digits
        else:
            digits[-1] += 1
            return digits

