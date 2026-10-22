class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        result = {}
        for s in strs:
            ss = str(sorted(s))
            if ss not in result:
                result[ss] = [s]
            else:
                result[ss].append(s)
        return list(result.values())