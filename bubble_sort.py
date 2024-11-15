# This only creates a random list
import random

nums = []
for i in range(10) :
    nums.append(random.randrange(0, 100))
print(nums)
# The functions to sort
# 
# index for checking list position
# and for rechecking if the sort has done
def index(i=0):
    if i < len(nums):
        index2(i)
        bubble_sort(i)
    return nums

# index for checking list position
def index2(i=0):
    if i < len(nums):
        bubble_sort(i)
    return nums

# Bubble Sort algorithm
def bubble_sort(i):
    if i < len(nums)-1:
        #print(i)
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        i += 1
        index(i)
    return nums

print(index(0))