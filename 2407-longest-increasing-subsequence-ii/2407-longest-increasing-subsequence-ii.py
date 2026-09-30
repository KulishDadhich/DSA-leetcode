class Solution:
    def lengthOfLIS(self, nums, k):

        mx = max(nums)
        tree = [0] * (4 * (mx + 1))

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return 0

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            return max(
                query(2 * node, l, mid, ql, qr),
                query(2 * node + 1, mid + 1, r, ql, qr)
            )

        def update(node, l, r, pos, val):
            if l == r:
                tree[node] = max(tree[node], val)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(2 * node, l, mid, pos, val)
            else:
                update(2 * node + 1, mid + 1, r, pos, val)

            tree[node] = max(
                tree[2 * node],
                tree[2 * node + 1]
            )

        ans = 0

        for x in nums:

            left = max(1, x - k)
            right = x - 1

            best = query(1, 1, mx, left, right)

            current = best + 1

            update(1, 1, mx, x, current)

            ans = max(ans, current)

        return ans