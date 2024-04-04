class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prev_sum=sum(nums[0:k])
        prev_first_element=nums[0]
        max_avg=prev_sum/k
        for i in range(k,len(nums)): 
            next_sum=prev_sum-prev_first_element+nums[i]
            curr_avg=next_sum/k
            if curr_avg>max_avg:
                max_avg=curr_avg
            prev_sum=next_sum
            prev_first_element=nums[i-k+1]
        return max_avg
            