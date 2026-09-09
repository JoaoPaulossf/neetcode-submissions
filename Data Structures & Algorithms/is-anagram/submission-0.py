class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        table = {}
        for char in s:
            table[char] = table.get(char, 0) + 1
        
        for char in t:
            if char not in table:
                return False
            table[char] -= 1
            if table[char] < 0:
                return False

        return True