class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        temp = sorted(set(nums))   # fix ordering

        maxi = 1
        curr = 1

        for i in range(1, len(temp)):
            if temp[i] == temp[i-1] + 1:
                curr += 1
            else:
                curr = 1
            maxi = max(maxi, curr)

        return maxi


