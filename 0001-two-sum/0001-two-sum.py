class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, a in enumerate(nums):
            b = target - a
            if b in m:
                return m[b], i
            m[a] = i