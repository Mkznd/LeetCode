class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        numsSorted = sorted(nums)
        while numsSorted[i]+numsSorted[j] != target:
            if numsSorted[i] + numsSorted[j] < target:
                i+=1
            elif numsSorted[i] + numsSorted[j] > target:
                j-=1
        index1 = nums.index(numsSorted[i])
        nums[index1] = -100
        index2 = nums.index(numsSorted[j])
        
        return [index1,index2]