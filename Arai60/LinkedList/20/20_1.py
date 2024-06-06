"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
なんとなく解いた記憶が有る
"""
# 1回目 7:29
# 1度目は右かっこが余った場合でエラーを出してしまい、修正し、ついでに各分岐に説明のコメントをつけた。修正に1分くらいかけた.


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        brackets_stack = []
        for char in s:
            # 左かっこの場合はスタックに貯める
            if char in bracket_pairs.keys():
                brackets_stack.append(char)
            # 入力の制限からそれ以外は右かっこ.
            else:
                # 右かっこが余った場合
                if len(brackets_stack) == 0:
                    return False

                bracket_to_close = brackets_stack.pop()
                # 最後に登場した左かっこと、今登場した右かっこが適合する場合
                if bracket_pairs[bracket_to_close] == char:
                    continue
                else:
                    return False

        # 左かっこが全て閉じられた
        if len(brackets_stack) == 0:
            return True
        # 左かっこが余った
        else:
            return False
