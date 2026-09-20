class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def solve(i, current, total):

            # We reached the target
            if total == target:
                ans.append(current.copy())
                return

            # We went too far
            if total > target or i == len(candidates):
                return

            # 1. Take the current number
            current.append(candidates[i])
            solve(i, current, total + candidates[i])
            current.pop()

            # 2. Skip the current number
            solve(i + 1, current, total)

        solve(0, [], 0)

        return ans