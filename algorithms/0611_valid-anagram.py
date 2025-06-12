"""
パターン1: 手書きでのアナグラム判定
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step.1 長さをチェック
        if len(s) != len(t):
            return False
        
        # Step.2 どの文字が何個あるかをチェック
        countS, countT = {}, {}
        for i in range(len(s)):
            ## 文字が初出であれば1からカウントアップ
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # Step.3 すべてのキーを順番に取り出し、個数が一致しているかチェック
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True