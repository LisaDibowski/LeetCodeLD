class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashsetduplicate = set()
        for n in nums:
            if n in hashsetduplicate:
                return True
            hashsetduplicate.add(n)
        return False 
