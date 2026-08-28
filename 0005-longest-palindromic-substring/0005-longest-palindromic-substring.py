class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1:
            return s
        lis_s=list(s)
        palindromes = {}
        for i in range(len(s)):
            j = len(s) -1
            while j > i: 
                if lis_s[i] == lis_s[j]:
                    temp = s[i:j+1]
                    if temp == temp[::-1]:
                        palindromes[len(temp)] = temp
                j -= 1
                
        max_len = max(palindromes.keys()) if palindromes else None
        largest_palindrome = palindromes[max_len] if max_len else s[:1]
        return largest_palindrome