class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same sorted characters
        return sorted(s) == sorted(t)
