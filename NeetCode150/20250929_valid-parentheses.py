"""
Stack

考え方：開き括弧が来たらスタックに積み、閉じ括弧が来たらスタックの一番上の開き括弧とペアになるか確認する

Time Complexity: O(n) - 文字列の長さを n とすると、各文字を一度ずつ処理するため
Space Complexity: O(n) - 最悪の場合、すべての文字が開き括弧である場合、スタックに n 個の文字が積まれるため

"""

class Solution:
    def isValid(self, s: str) -> bool:
        ## 「まだ閉じられていない括弧」が上（末尾）になるように積まれたスタック
        stack = [] ### 実質はリストだが、末尾に追加・削除する使い方によってスタックとして機能させる
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } ## 閉じ括弧から、「直前が何ならOKか」を判定 ## 辞書型 dict[key: str, value: str]
        ### 例: closeToOpen[")"] -> "("を参照できる

        for c in s:
            ## 閉じ括弧の場合
            if c in closeToOpen: ## keyが存在しないとcloseToOpen[c]でエラーになる
                ## stack[-1]は一番内側の開き括弧。現在の閉じ括弧がペアならpop、そうでなければ不正
                if stack and stack[-1] == closeToOpen[c]: ## 空のスタックだとエラーになる + 閉じ括弧を読んだときにstackが空だと対応する開き括弧がないので不正
                    ## ペアならstackから取り除く
                    stack.pop()
                else:
                    return False
            else: ## 開き括弧ならスタックに追加
                stack.append(c)
        ## スタックが空なら有効な括弧列と判断
        return True if not stack else False
        

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