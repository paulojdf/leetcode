"""
Problem:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
    
        def check_palindrome(check_string: str) -> bool:
        # This function checks if a string is a palindrome, comparing the first half of the string with the reversed remain.
        # Returns True is the string is a palindrome and False if it doesn't.
    
            if len(check_string) % 2 == 0 and check_string[:len(check_string)//2] == check_string[(len(check_string)//2):][::-1]:
                return True
            elif len(check_string) % 2 !=0 and check_string[:len(check_string)//2] == check_string[(len(check_string)//2+1):][::-1]:
                return True
            else:
                return False

        i = 0
        j = len(s) - 1
        while i < j:
            
            if check_palindrome(s[i:j+1]):
                return True
            
            elif s[i] != s[j]:
                   
                if check_palindrome(s[i+1:j+1]):
                    return True
                elif check_palindrome(s[i:j]):
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1
    
# NOTE - Solution purposed by Leetcode:
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True
"""