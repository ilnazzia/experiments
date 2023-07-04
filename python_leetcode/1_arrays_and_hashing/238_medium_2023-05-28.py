def productExceptSelf(nums):
    l = len(nums)
    output = [0] * l

    # prefix
    prev = 1
    for i, num in enumerate([1] + nums[:-1]):
        output[i] = num * prev
        prev = num * prev

    # postfix
    prev = 1
    for i, num in enumerate((nums[1:] + [1])[::-1]):
        output[l - i - 1] *= num * prev
        prev = num * prev
    
    return output


nums = [1,2,3,4]
print(productExceptSelf(nums))
