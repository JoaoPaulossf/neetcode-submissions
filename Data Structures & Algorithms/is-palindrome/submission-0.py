class Solution:
    def isPalindrome(self, s: str) -> bool:
        novo = ""

        for caractere in s:
            if caractere.isalnum():
                novo += caractere.lower()
    
        for i in range(len(novo) // 2):
            if novo[i] != novo[len(novo) - i - 1]:
                return False
        
        return True