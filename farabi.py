from math import sqrt

def sigma(start, stop, func):
    out = 0
    for x in range(start, stop):
        out += func
    return out

def mean(nums):
    return sum(nums)/len(nums)

def median(nums):
    nums = sorted(nums)
    l = len(nums)
    if l%2 != 0:
        return nums[int(l/2)]
    i = int(l/2)
    return (nums[i-1]+nums[i])/2

def variance(nums):
    aver = mean(nums)
    out = 0
    for x in nums:
        out+=(x-aver)**2
    return out/len(nums)

def variance_s(nums):
    aver = mean(nums)
    out = 0
    for x in nums:
        out+=(x-aver)**2
    return out/(len(nums)-1)

def stdev(nums):
    return sqrt(variance(nums))

def stdev_s(nums):
    return sqrt(variance_s(nums))
