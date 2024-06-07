"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
なんとなく解いた記憶が有る
"""
# 2回目をもう少し修正 無駄なインデントを避ける.


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        brackets_stack = []
        for c in s:
            # 左かっこの場合はスタックに貯める.
            if c in bracket_pairs.keys():
                brackets_stack.append(c)
                continue
            # 入力の制限からそれ以外は右かっこ.
            # 右かっこが余った場合、不適切.
            if len(brackets_stack) == 0:
                return False

            bracket_to_close = brackets_stack.pop()
            # 最後に登場した左かっこと、今登場した右かっこが適合する場合、正しい右かっこということになる.
            if bracket_pairs[bracket_to_close] == c:
                continue
            # 適合しない右かっこが登場した場合、不適切.
            else:
                return False

        # 左かっこが全て閉じられたということは、全てのかっこがマッチしていた
        return not brackets_stack
