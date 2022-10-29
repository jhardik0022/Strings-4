# Time complexity : O(n) --> n = 10 digits
# Space complexity : O(1)
# Leetcode : Solved and submitted

class Solution:
    def myAtoi(self, s: str) -> int:
        # remove the leading spaces
        s = s.lstrip(' ')
        
        # check for null case
        if s == None or len(s) == 0:
            return 0
        
        # check for the first char in the string after trimming spaces
        res = 0
        first = s[0]
        sign = '+'
        
        # calculate the int min and max values
        max_val = pow(2,31) - 1
        min_val = -pow(2,31)
        
        # change the sign is '-'
        if first == '-':
            sign = '-'
        
        # if we find any other character then return 0
        if (first != '-' and first != '+') and not first.isdigit():
            return 0
        
        # max num we can go is int max / 10
        max_num = max_val//10
        
        # traverse over the string s
        for i in range(len(s)):
            ch = s[i]
            # fetch the digit
            digit = ord(ch) - ord('0')
            if ch.isdigit():
                # if the digit is num and res so far has gone above the limit which is max_num, then return the max or min val according to the sign
                if res > max_num:
                    if sign == '+':
                        return max_val
                    else:
                        return min_val
                # if the num found so far is same as max_val, then we'll update the value according to the next value
                elif res == max_num:
                    # for positive sign, if any number above 6, return max_val
                    if sign == '+':
                        if digit >= 7:
                            return max_val
                    else:
                        # for negative sign, if any number above 7, return max_val
                        if digit >= 8:
                            return min_val
                # keep forming the res with each didit we find
                res = res * 10 + digit
            
            # if at any point, we find a non-numeric character, then break and return the res
            if i > 0 and not ch.isdigit():
                break
        
        # return res according to the sign
        if sign == '-':
            return -res
        return res
