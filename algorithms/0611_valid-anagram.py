"""
パターン1: 手書きでのアナグラム判定
- 時間計算量: O(n) = O(1) + O(n) + O(k) ※k は最大で n
- 空間計算量: O(k)
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

"""
パターン2: PythonのCounter()を使ったアナグラム判定
- 時間計算量: O(n)
- 空間計算量: O(k)
- カウンターの使い方: Counter({'a': 3, 'b': 2, 'c': 1})
- パフォーマンスが最もよく、簡潔で読みやすい。
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

"""
パターン3: ソートを使ったアナグラム判定
- 時間計算量: O(n log n)
- 空間計算量: O(n)

sorted(s) → O(n log n)
sorted(t) → O(n log n)
リスト比較 → O(n)
総計算量 = O(n log n) + O(n log n) + O(n) = O(n log n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)