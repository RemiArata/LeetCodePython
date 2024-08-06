def two_sum(nums, target) -> list[int]:
    hash_map = {}

    for idx, val in enumerate(nums):
        res = target - val
        if res in hash_map:
            return [hash_map[res], idx]
        hash_map[val] = idx

n = [2,7,11,15]
t = 9
print(two_sum(n, t))

n = [3,2,4] 
t = 6
print(two_sum(n, t))

n = [3,3]
t = 6
print(two_sum(n, t))