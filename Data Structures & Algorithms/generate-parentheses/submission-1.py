class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        comb = []

        def backtrack(open_count, close_count):
            if close_count == open_count == n:
                res.append("".join(comb))
                return

            if close_count < open_count:
                comb.append(")")
                backtrack(open_count, close_count + 1)
                comb.pop()

            if open_count < n:
                comb.append("(")
                backtrack(open_count + 1, close_count)
                comb.pop()

        backtrack(0, 0)

        return res
        