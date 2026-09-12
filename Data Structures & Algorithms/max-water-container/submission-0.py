class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        i = 0
        j = len(heights) - 1

        while(i < j):
            volume = (j - i) * min(heights[i] , heights[j]) # base * altura
            
            if volume > output:
                output = volume
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        return output