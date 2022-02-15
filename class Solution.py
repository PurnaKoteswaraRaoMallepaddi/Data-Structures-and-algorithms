class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recur(index,x,y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            else:ß
                if board[x][y] == word[index]:
                    if index == len(word) - 1:
                        return True
                    else:
                        temp = board[x][y]
                        board[x][y]="#"
                        a = recur(index+1,x+1,y)
                        b = recur(index+1,x-1,y)
                        c = recur(index+1,x,y+1)
                        d = recur(index+1,x,y-1)
                        board[x][y] = temp
                        return a or b or c or d
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and recur(0,i,j):
                    return True
        return False
                    
            ß