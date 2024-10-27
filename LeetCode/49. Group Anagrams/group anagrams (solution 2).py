from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]
def group_anagrams(strs):
   result = defaultdict(list)

   for s in strs:
      sorted_word = "".join(sorted(s))

      result[sorted_word].append(s)

   return list(result.values())


print(group_anagrams(strs))

    




