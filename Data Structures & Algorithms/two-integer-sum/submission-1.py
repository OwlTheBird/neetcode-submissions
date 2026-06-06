class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        is_target = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                is_target = nums[i] + nums[j]
                if is_target == target:
                    result.append(int(i))
                    result.append(int(j))
                    return result