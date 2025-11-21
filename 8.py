class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        PN = 1
        ans = 0
        if not s:
            return 0

        MAX = 2**31 - 1
        MIN = -2**31

        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            PN = -1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            ans = ans * 10 + digit

            if PN * ans <= MIN:
                return MIN
            if PN * ans >= MAX:
                return MAX
            
            i += 1

        return ans * PN
        