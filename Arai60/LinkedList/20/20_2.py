"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
なんとなく解いた記憶が有る
"""
# 2回目 綺麗にする
# 特に変更しなかった、コメントを追加した.


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        brackets_stack = []
        for char in s:
            # 左かっこの場合はスタックに貯める.
            if char in bracket_pairs.keys():
                brackets_stack.append(char)
            # 入力の制限からそれ以外は右かっこ.
            else:
                # 右かっこが余った場合、不適切.
                if len(brackets_stack) == 0:
                    return False

                bracket_to_close = brackets_stack.pop()
                # 最後に登場した左かっこと、今登場した右かっこが適合する場合、正しい右かっこということになる.
                if bracket_pairs[bracket_to_close] == char:
                    continue
                # 適合しない右かっこが登場した場合、不適切.
                else:
                    return False

        # 左かっこが全て閉じられたということは、全てのかっこがマッチしていた
        if len(brackets_stack) == 0:
            return True
        # 左かっこが余った場合、不適切.
        else:
            return False
