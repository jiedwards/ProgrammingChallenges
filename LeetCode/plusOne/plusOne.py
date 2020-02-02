class Solution(object):
    def plusOne(self, digits):
            # Edge case to ensure a value
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            # The 9 will be removed and a zero is added in it's place
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits