class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        subset = []
        
        def get_subset(i: int):
            if i>=len(nums):
                r.append(subset.copy())
                return
            subset.append(nums[i])
            get_subset(i+1)
            subset.pop()
            get_subset(i+1)
        
        get_subset(0)
        return r
