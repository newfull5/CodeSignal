def kthLargestElement(nums, k):
    nums.sort()
    return nums[-k]
    
