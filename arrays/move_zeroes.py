class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        writeInd = 0
        n = len(nums)
        readInd = 0
        while readInd < n:
            if nums[readInd] != 0:
                nums[writeInd] = nums[readInd]
                writeInd += 1
            readInd += 1
			
        while writeInd < n:
            nums[writeInd] = 0
            writeInd += 1
		
	return nums
