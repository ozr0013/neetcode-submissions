
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        maps = {}
        mapp = {}
        for i in range(len(s)):
            maps[s[i]] = maps.get(s[i], 0) + 1
            mapp[t[i]] = mapp.get(t[i], 0) + 1
        return maps == mapp