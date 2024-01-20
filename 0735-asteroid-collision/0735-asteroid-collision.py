class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # initialization
        stack=[]
        while asteroids:
            if len(stack)==0: 
                stack.append(asteroids.pop())
            else:
                if stack[-1]>0: 
                    stack.append(asteroids.pop())
                elif asteroids[-1]<0: 
                    stack.append(asteroids.pop())
                elif stack and abs(stack[-1])>asteroids[-1]:
                    asteroids.pop()
                elif stack and abs(stack[-1])<asteroids[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    asteroids.pop()
        return stack[::-1]
            
                