class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            vertical and horizontal

            min: max(heights)

            horizontal: add (index, height) into stack
            while h < stack[-1]
                                --> calculate horizontal from current to stack[-1]
                                --> need to store index into stack
                                --> index to be the last stack[-1]'s

            after all, for each remaining element in stack,
                calculate horizontal with the new stack[-1] (original popped)

            [7,1,7,2,2,4]
            i = 0: (0, 7)
            i = 1: (0, 1)
            i = 2: (0, 1), (2, 7)
            i = 3: (0, 1), (2, 2)
            i = 4: (0, 1), (2, 2), (4, 2)
            i = 5: (0, 1), (2, 2), (4, 2), (5, 4)
        '''

        ans = max(heights)
        stack = []  # (start_index, height)

        for i, h in enumerate(heights):
            # vertical
            ans = max(ans, h)

            # horizontal
            start_index = i
            while stack and h < stack[-1][1]:
                popped = stack.pop()
                start_index = popped[0]
                popped_height = popped[1]
                ans = max(ans, (i - start_index) * popped_height)
                # print("udpated ans", ans)

            stack.append((start_index, h))
            # print("ans now", ans)

        # print("stack", stack)

        while stack:
            popped = stack.pop()
            index = popped[0]
            popped_height = popped[1]
            ans = max(ans, (len(heights) - index) * popped_height)

        return ans