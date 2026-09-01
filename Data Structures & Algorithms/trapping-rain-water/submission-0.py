class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax = [0]* n
        rightmax = [0]* n
        maxi=0
        for i in range(1,len(height)):
            maxi=max(maxi,height[i-1])
            leftmax[i]=maxi
        maxi=0
        for i in range(len(height)-2,-1,-1):
            maxi=max(maxi,height[i+1])
            rightmax[i]=maxi
        res=0
        for i in range(0,len(height)):
            area=min(leftmax[i],rightmax[i]) - height[i]
            if area > 0:
                res+= area
        return res


