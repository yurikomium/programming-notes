"""
Brute Force

考え方：「有効な括弧列なら、隣り合う一致ペア (), {}, [] を消していくと最後に空文字になる」
* 条件として、開きかっこと閉じかっこがペアで登場することが問題に書かれているため。

Time Complexity: O(n^2) - 文字列の長さを n とすると、最悪で n/2 回の置換を行い、各置換で文字列全体を走査するため
Space Complexity: O(n) - 置換操作により新しい文字列が生成されるため

"""

class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''