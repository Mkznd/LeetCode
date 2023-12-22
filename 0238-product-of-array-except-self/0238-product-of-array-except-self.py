class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        post = [1]*len(nums)
        
        pref[0] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i-1]*nums[i-1]
            
        a = list(reversed(nums))
        post[0] = 1
        for i in range(1, len(a)):
            post[i] = post[i-1]*a[i-1]
            
        post = list(reversed(post))
        
        return [pref[i]*post[i] for i in range(len(pref))]