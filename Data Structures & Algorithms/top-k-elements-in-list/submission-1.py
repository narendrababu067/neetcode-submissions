from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   # count frequency
        
        # sort numbers based on frequency (highest first)
        sorted_nums = sorted(count, key=count.get, reverse=True)
        
        return sorted_nums[:k]