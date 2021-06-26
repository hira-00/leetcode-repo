class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        arr_copy = [arr[i] for i in range(len(arr))]
        arr_copy.sort()
        
        rank_hash = {}
        dup = 0
        for index, elem in enumerate(arr_copy):
            if elem not in rank_hash:
                rank_hash[elem] = (index + 1) - dup
            else:
                dup += 1
        
        for i in range(len(arr)):
            arr[i] = rank_hash[arr[i]]
            
        return arr
