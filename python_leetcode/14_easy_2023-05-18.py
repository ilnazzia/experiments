strs = [""]
def longestCommonPrefix(strs):
    result = ""
    for num, letter in enumerate(strs[0]):
        for wrd in strs:
            if wrd[:num + 1] != result + letter: 
                return result
        result += letter
    return result

print(longestCommonPrefix(strs))

print(sorted(['free', 'freme', 'or']))