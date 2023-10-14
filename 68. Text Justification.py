class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        """
            @param temp     -> A list to store several lists (sList), each element in temp represents words at the same line
            @param sList    -> A list to store strings, every word inside the sList stays at the same line
            @param ans      -> Answer to return, a list to store strings

            Appraoch:
            1) Loop through words, to distinguish which line should the word belongs to (store to temp)
                a) Uses width to keep track on remaining width
                b) If width >= len(word), try to add the word into sList with:
                    i)  If it is the 1st word to be added, simply add it
                    ii) Else, add a space before the word, as each word should at least be separated by 1 space
                c) If width < len(word), append sList into temp and open a new sList to represent a new line

                Special 1:  Consider for lines having more than 1 word, even if remaining width = len(word),
                            as we need to pack in an extra space,
                            we have to move the word to the new line
                Special 2:  Consider for len(word) = maxWidth, we need a new line without any space to store the word

            2) Loop through temp, try to
                a) Fully Justify for lines that are not the last line
                b) Left Justify for the last line

                For a:  i)      We try to put sList into a justifiedStr and add to ans
                        ii)     We uses len(sList) to calculate the number of "intervals" between words
                        iii)    Then, we calculate remaining width after packing the word, thus we know number of spaces needed
                        iv)     Total number of spaces needed // number of intervals = number of spaces in each interval
                        v)      If iii) has remainder, as the intervals on left needs to have more spaces then intervals on right,
                                we add extra space starting from the left and deduct remainder by 1, until remainder = 0

                For b:  i)      Just add all the words to justifiedStr by "".join(sList) and pack the remaining width with spaces

        """

        def justify(sList: List[str], fully: bool, maxWidth: int) -> str:

            intervals = len(sList) - 1  # space interval between words
            lengthOfWords = 0
            for s in sList:
                lengthOfWords += len(s)
            diff = remaining = maxWidth - lengthOfWords

            if intervals == 0 or not fully:
                return "".join(sList) + " " * diff

            justifiedStr = sList[0]
            expectedSpaces = diff // intervals
            remainder = diff % intervals

            print("diff", sList, diff, intervals, expectedSpaces, remainder)

            for i in range(1, len(sList)):
                actualSpaces = expectedSpaces
                if remainder > 0:
                    actualSpaces += 1
                    remainder -= 1
                if remaining == 0:
                    actualSpaces = 0

                s = sList[i]
                justifiedStr += " " * actualSpaces + s
                remaining -= actualSpaces
                print("appending", actualSpaces, s)

            print("result length", len(justifiedStr))
            return justifiedStr

        temp = []
        ans = []
        sList = []
        width = maxWidth
        for word in words:

            if width < maxWidth and width <= len(word):
                temp.append(sList)
                sList = [word]
                width = maxWidth - len(word)
                continue

            if width >= len(word):
                wordLength = len(word)
                if len(sList) > 0:
                    wordLength += 1
                    word = " " + word
                width -= wordLength
                sList.append(word)

        if sList:
            temp.append(sList)

        print("temp", temp)

        for i in range(len(temp)):
            ans.append(justify(temp[i], i != len(temp) - 1, maxWidth))

        print("ans", ans)

        return ans
