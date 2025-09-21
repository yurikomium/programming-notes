"""
可読性の高い方法

時間計算量: O(n) - 文字列を一度走査し、新たに文字列を作成するため
空間計算量: O(n) - 文字列を新たに作成するため

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): ## 英数字かどうかをチェック
                newStr += c.lower() ## 小文字に変換★
        return newStr == newStr[::-1] ## 逆順にして比較

"""

Two Pointers

時間計算量: O(n) - 文字列を一度走査するため
空間計算量: O(1) - 追加の空間を使用しないため

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 ## 左右にポインタを用意

        while l < r: ## 左右の比較すべきペアがまだ残っているか？の判定
            ## 内側のwhileは不要な文字をスキップする
            ### 反復の途中でlとrが交差する可能性があるため、条件にl < rを入れる
            while l < r and not self.alphaNum(s[l]): ## 英数字でない場合、ポインタを進める（英数字以外はスキップする）
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): ## 英数字の場合は左右の英数字を比較。
                return False
            l, r = l + 1, r - 1 ## 一致したら次の比較のために内側にポインタを進める
        return True

    def alphaNum(self, c): ## 英字(A–Z, a–z)と数字(0–9)のみを英数字とみなす。isAlnum()と同じ。
        ## ord()は、文字をUnicode（ユニコード）の数値（コードポイント）に変換する
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))