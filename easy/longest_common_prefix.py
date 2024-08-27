def longest_common_prefix(strs) -> str:
    prefixs = [""]
    p = ""
    for ltr in strs[0]:
        p += ltr
        prefixs.append(p)
    for i in range(1, len(prefixs)):
        for s in strs:
            if prefixs[i] not in s[:i]:
                return prefixs[i - 1]
    return prefixs[-1]


            




strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

strs = ["dog","racecar","car"]
print(longest_common_prefix(strs))

strs = ["c","acc","ccc"]
print(longest_common_prefix(strs))