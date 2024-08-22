def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
            return -1
    window = len(needle)
    for idx in range(0, len(haystack)):
        if haystack[idx:idx + window] == needle:
            return idx
    return 0

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))