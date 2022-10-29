# Time complexity : O (m*n log n) --> m - max length of log, n - number of logs
# Space complexity : O (m*n)
# Leetcode : Solved and submitted

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # define a custom sort function
        def get_key(log):
            # split the log into two parts, one is the log id and other is rest of the log
            id_log, rest = log.split(" ", maxsplit=1)
            
            # if the first character of the rest is an alphanumeric, such as "l", then return a tuple
            # with (0, rest, id_log)
            # 0 ensures that this comes first
            # rest is the 2nd parameter when sorting is done, if this is same, then we'll check for log_id
            if rest[0].isalpha():
                return (0, rest, id_log)
            
            # if we encounter a digit, then sorting is not required, just put 1
            return (1, None, None)
        
        # sort the logs array with the above function as the sorting logic
        return sorted(logs, key = get_key)
