height=[2,5,4,6,4,3,5]
class Solution:
    def trap(self, height) :
        if not height:
            return 0
        
        left_max, right_max = 0,0 #at first left and right put zero and for left we  want to from L-->R  And form right to left vice-versa 
        left, right = 0, len(height) - 1
        water = 0
        
        while left < right:  # doing this till we not getting any pillor longer than left one
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left] # adding all the water till the next one is not met longer and same as in from right max
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        
        return water
    
# we want to  Create an instance of the Solution class
solution = Solution()

#  also Providing a list of heights as input
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# Call the trap method to calculate the trapped water
result = solution.trap(heights)

# Print the result
print(result)

                        

    
        