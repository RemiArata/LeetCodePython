

def two_sum(nums, target) -> list[int]:
    for num in nums:
        if target - num in nums:
            if target - num == num:
                if nums.count(num) > 1:
                    first = nums.index(num)
                    nums.pop(first)
                    second = nums.index(num)
                    return [first, second + 1]
                else:
                    continue
            else:
                return [nums.index(num), nums.index(target - num)]
    return None

n = [2,7,11,15]
t = 9
print(two_sum(n, t))

n = [3,2,4] 
t = 6
print(two_sum(n, t))

n = [3,3]
t = 6
print(two_sum(n, t))