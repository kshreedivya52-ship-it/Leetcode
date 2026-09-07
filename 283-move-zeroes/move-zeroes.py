class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[k] = nums[i]
            if k != i:
                nums[i] =0

            k += 1

        return nums        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        