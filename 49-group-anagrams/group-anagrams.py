class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1 # a-a=0, z-a=25

            result[tuple(count)].append(str)

        return list(result.values())