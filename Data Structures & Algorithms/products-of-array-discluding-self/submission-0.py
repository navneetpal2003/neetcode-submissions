import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero=0
        ans=[]
        for num in nums:
            if num==0:
                zero+=1
            else:
                prod*=num
        if(zero>1):
            return [0]*len(nums)
        elif(zero == 1):
            for num in nums:
                if num!=0:
                    ans.append(0)
                else:
                    ans.append(prod)
            return ans
        else:
            for num in nums:
                ans.append(prod//num)
            return ans
