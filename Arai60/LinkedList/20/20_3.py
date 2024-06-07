# 3回目 3回書き直し

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        bracket_stack = []

        for c in s:
            # 左かっこはスタックに貯めておく
            if c in bracket_pairs.keys():
                bracket_stack.append(c)
                # 終わりなので次へ
                continue
            # 右かっこは、まだ閉じてない左かっこのうち最後に開かれたものとマッチする必要がある
            # stackが空な場合は右かっこが余っている。popもできない.
            if not bracket_stack:
                return False

            # これを閉じられるか確認する
            bracket_to_close = bracket_stack.pop()
            if bracket_pairs[bracket_to_close] == c:
                continue
            else:
                return False
        return not bracket_stack
