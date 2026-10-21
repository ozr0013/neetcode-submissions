class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in map:
                map[sortedword].append(word)
            else:
                map[sortedword] = [word]
        return list(map.values())       