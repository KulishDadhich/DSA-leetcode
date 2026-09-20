class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(current.copy())
                return

            # Don't take nums[i]
            backtrack(i + 1, current)

            # Take nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)

            # Remove it for the next possibility
            current.pop()

        backtrack(0, [])
        return result