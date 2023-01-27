class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<2:
            return 0
        l=0
        r=len(height)-1
        maxw=(len(height)-1)*min(height[l],height[r])
        while r>l:
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                l+=1
            h=min(height[l],height[r])
            area=(r-l)*h
            maxw=max(maxw,area)
        
        return maxw
            
        