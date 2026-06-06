class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        Freq_counter = []
        real_counter = []
        num_freq = 0

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                get_value = dic.get(nums[i])
                get_value += 1
                dic[nums[i]] = get_value

        sorted_list = sorted(dic, key=dic.get, reverse= True)[0:k]

        return sorted_list
            




        