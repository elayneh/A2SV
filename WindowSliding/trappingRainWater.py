class Solution:
    def trap(self, height: list[int]) -> int:
        '''
        For each interior column:
            Max. wall to the left begins a container
            Max. wall to the right ends a container; top surface is the minimum of the two.
            Positives under the top surface reduce the water capacity
        '''
        max_l_wall = [0]
        max_ht_so_far = 0                   # Maximum height to the left
        volume = 0
        # For each interior column, l to r:
        for i in range(1, len(height)):
            # record the highest wall to the left of it
            max_ht_so_far = max(height[i - 1], max_ht_so_far)
            max_l_wall.append(max_ht_so_far)
        max_ht_so_far = height[-1]          # Maximum height to the right
        i = len(height) - 2
        # For each interior column, r to l:
        while i > 0:
            # volume += min(highest wall to the right, highest wall to the left) minus column height (or 0)
            max_ht_so_far = max(max_ht_so_far, height[i + 1])
            volume += max(min(max_ht_so_far, max_l_wall[i]) - height[i], 0)
            i -= 1
        return volume


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
