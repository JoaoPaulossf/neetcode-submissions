class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tabela = {}
        for num in nums:
            if num in tabela:
                return True
            tabela[num] = num
        return False