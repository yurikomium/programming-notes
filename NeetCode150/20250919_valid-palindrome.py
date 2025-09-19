"""
可読性の高い方法

時間計算量: O(n) - 文字列を一度走査し、新たに文字列を作成するため
空間計算量: O(n) - 文字列を新たに作成するため

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower() ## 小文字に変換
        return newStr == newStr[::-1] ## 逆順にして比較