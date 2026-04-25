class Solution:
    def hasDuplicate(self, nums):
        dic = {}

        for num in nums:
            if num in dic:
                return True
            dic[num] = 1

        return False