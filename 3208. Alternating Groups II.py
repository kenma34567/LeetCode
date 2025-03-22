class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        '''
            double end queue
            -> keep track of start & end, loop until start reaches the last element of the list

            -> first initilize the sub list to be size k, from colors[0] -> colors[k-1]
            -> if there are consecutive blocks that have the same color, set start to the latter one
            -> when a valid group is found, keep shifting the sub list by popping the start and append a new block, if the original pop = the newly added block, then it is also valid

        '''

        q = deque([])
        result = 0
        start, count = 0, 0

        while len(q) < k and start < len(colors):
            current = count % len(colors)
            if q and colors[current] == q[-1]:
                # invalid, set start to count
                q = deque([])
                start = count
            q.append(colors[current])

            # print("outside", start, count)

            if len(q) == k:
                # print("?", q)
                result += 1
                q.popleft()
                start += 1

            count += 1

        return result
