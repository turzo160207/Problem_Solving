from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
def group_anagrams(strs):
    result = defaultdict(list)

    for s in strs:
        count = [0]*26

        for c in s:
            count[ord(c)-ord("a")] += 1

        result[tuple(count)].append(s)

    return list(result.values())

print(group_anagrams(strs))

    




