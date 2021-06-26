class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        all_nums = [i for i in range(1, len(nums) + 1)]
        hash = {}
        for num in all_nums:
            hash[num] = 0
            
        for num in nums:
            hash[num] = 1

        not_present = []
        
        for num in all_nums:
            if hash[num] == 0:
                not_present.append(num)
                
        return not_present
