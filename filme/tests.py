from django.test import TestCase

# Create your tests here.
nums = [1,2,3,4,5]

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(find_max(nums))