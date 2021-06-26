class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        #declare last element as max
        current_max = arr[-1]
        #replace last as -1
        arr[-1] = -1
        n = len(arr)
        for i in range(n-2,-1,-1):
            temp = arr[i];
            arr[i] = current_max
            if temp > current_max:
                current_max = temp
                
                
        return arr
