class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for str in strs:
            curr=''.join(sorted(str))
            mp[curr].append(str)
        return list(mp.values())