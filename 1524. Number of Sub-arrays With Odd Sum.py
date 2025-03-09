class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
                '''
            brute force: n^2 to find all sub arrays, calculate one by one

            prefix sum
            [1, 4, 9]
            -> loop through prefix sum, if current is odd, +1, and check before this element, how many even prefix sum, becoz odd - even = odd
            -> if current is even, just check before this element, how many odd prefix sum, becoz even - odd = odd
        '''

        MODULO = pow(10, 9) + 7

        prefix_sum = [arr[0]]
        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[-1] + arr[i])
        #print("prefix_sum", prefix_sum)

        odd_count, even_count = 0, 0
        result = 0

        for n in prefix_sum:
            if n % 2 != 0:  #odd
                result = (result + even_count + 1) % MODULO
                odd_count += 1
            else:           #even
                result = (result + odd_count) % MODULO
                even_count += 1

        return result
