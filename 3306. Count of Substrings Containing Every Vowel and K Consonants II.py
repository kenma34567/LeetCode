class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        '''
            ---------------------------->
                                k===-----
                                    k+1--
                                result of k - result of (k+1)
        '''

        def findAtLeastTargetCon(target):
            count = 0
            left = 0
            vowels = {'a', 'e', 'i', 'o', 'u'}
            vowels_count = defaultdict(int)
            consonants_count = 0

            for right, right_char in enumerate(word):
                if right_char in vowels:
                    vowels_count[right_char] += 1
                else:
                    consonants_count += 1

                while len(vowels_count) == 5 and consonants_count >= target:
                    '''
                        if a substring is good, adding char after it is also good
                        aeiouqqq, k = 1
                        --> aeiouq
                        --> aeiouqq
                        --> aeiouqqq
                    '''
                    count += len(word) - right

                    left_char = word[left]
                    if left_char in vowels:
                        vowels_count[left_char] -= 1
                    else:
                        consonants_count -= 1
                    if vowels_count[left_char] == 0:
                        vowels_count.pop(left_char)

                    left += 1

            return count

        return findAtLeastTargetCon(k) - findAtLeastTargetCon(k + 1)
