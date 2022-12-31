# Time Complexity: O(n)  Here n=sr*sc
# Space Complexity: O(1)
# Question Link: https://leetcode.com/problems/flood-fill/

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc]==color:
            return image
        p_c=image[sr][sc]
        def fillcolor(image,sr,sc,color):
            if sc<0 or sr<0 or sc>len(image[0])-1 or sr>len(image)-1 or image[sr][sc]==color or image[sr][sc]!=p_c :
                return image
            image[sr][sc]=color
            fillcolor(image,sr-1,sc,color)
            fillcolor(image,sr,sc+1,color)
            fillcolor(image,sr+1,sc,color)
            fillcolor(image,sr,sc-1,color)
            return image

        return fillcolor(image,sr,sc,color)
        


