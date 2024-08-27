def search_insert(nums: list[int], target: int) -> int:
    lower, upper = 0, len(nums)

    if target in nums:
        return nums.index(target)
    
    while upper - lower > 1:
        mid = (upper + lower) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            upper = mid
        else:
            lower = mid
    if nums[lower] > target:
        return lower
    return upper

n = [1, 3, 5, 6]
t = 5
print(search_insert(n, t)) # 2


n = [1, 3, 5, 6]
t = 2
print(search_insert(n, t)) # 1

n = [1, 3, 5, 6]
t = 7
print(search_insert(n, t)) # 4

n = [1]
t = 1
print(search_insert(n, t)) # 0

n = [1, 3, 5, 6] 
t = 0
print(search_insert(n, t)) # 0