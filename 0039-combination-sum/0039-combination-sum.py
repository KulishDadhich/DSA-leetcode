class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(i, current, total):
            if total == target:
                result.append(current.copy())
                return

            if i == len(candidates) or total > target:
                return

            # Take candidates[i]
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            current.pop()

            # Don't take candidates[i]
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)

        return result