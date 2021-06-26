class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letter_counts = {}
        
        for let in s:
            if let in letter_counts:
                letter_counts[let] += 1
            else:
                letter_counts[let] = 1
                
        for index, let in enumerate(s):
            if letter_counts[let] == 1:
                return index
            
            
        return -1
