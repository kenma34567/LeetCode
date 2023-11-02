class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValidNum(numSet: set, num: int) -> bool:
            if not num.isnumeric():
                return True
            num = int(num)
            if num in numSet or num < 1 or num > 9:
                return False
            numSet.add(num)
            return True

        def checkRow(i: int) -> bool:
            numSet = set()
            for j, num in enumerate(board[i]):
                if not isValidNum(numSet, num):
                    return False
            return True

        def checkColumn(j: int) -> bool:
            numSet = set()
            for i in range(len(board)):
                num = board[i][j]
                # print("check col", num)
                if not isValidNum(numSet, num):
                    return False
            return True

        def checkBoxValid(boxNum: int) -> bool:

            '''
                0: 0, 0
                1: 0, 3
                2: 0, 6

                3: 3, 0
                4: 3, 3
                5: 3, 6

                6: 6, 0
                7: 6, 3
                8: 6, 6
            '''
            numSet = set()
            iStart = 3 * (boxNum // 3)
            jStart = 3 * (boxNum % 3)
            for i in range(iStart, iStart + 3):
                for j in range(jStart, jStart + 3):
                    num = board[i][j]
                    if not isValidNum(numSet, num):
                        return False
            return True

        for i in range(len(board)):
            if not checkRow(i):
                print("not valid row!", i)
                return False

        for j in range(len(board[0])):
            if not checkColumn(j):
                print("not valid col!", j)
                return False

        for boxNum in range(9):
            if not checkBoxValid(boxNum):
                print("not valid box!", boxNum)
                return False

        return True
