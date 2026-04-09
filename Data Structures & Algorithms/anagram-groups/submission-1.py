class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for string in strs:
            char_cnt=[0]*26
            for ch in string:
                char_cnt[ord(ch)-ord('a')]+=1
            groups.setdefault(tuple(char_cnt),[]).append(string)
        return list(groups.values())
