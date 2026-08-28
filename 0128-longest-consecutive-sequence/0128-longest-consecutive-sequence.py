class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        sorted_nums = sorted(list(set_nums))
        consecutives = []
        lenth = 1
        for i in range(len(sorted_nums)-1):
            num = sorted_nums[i]
            next_num =  sorted_nums[i+1]
            if num == next_num -1:
                lenth += 1
            else:
                if lenth > 1:
                    consecutives.append(lenth) 
                    lenth = 1
        consecutives.append(lenth)
        logest_consecutive = max(consecutives) if consecutives else None
        return logest_consecutive       