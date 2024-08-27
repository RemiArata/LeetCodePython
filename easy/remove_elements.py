
def remove_elements(nums: list[int], val) -> int:
    not_val = 0
    for x in nums:
        if x != val:
            nums[not_val] = x
            not_val += 1
    return not_val