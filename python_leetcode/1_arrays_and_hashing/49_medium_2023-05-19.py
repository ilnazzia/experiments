def groupAnagrams(strs):
    # sorted_strs = [''.join(sorted(x)) for x in strs]
    result = {}

    for i in range(len(sorted_strs)):
        if sorted_strs[i] not in hashM:
            hashM[sorted_strs[i]] = [i]
        else:
            hashM[sorted_strs[i]] += [i]
    
    result = []
    for k in hashM:
        temp = []
        for i in hashM[k]:
            temp.append(strs[i])
        result.append(temp)

    return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))