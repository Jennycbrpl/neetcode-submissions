class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bigotes = set()
        for i in nums:
            if i in bigotes:
                return True
            bigotes.add(i)
        return False