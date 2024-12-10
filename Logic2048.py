# 2048 project
import random
class Logic2048:
    def __init__(self):
        self._row = 4
        self._col = 4
        self._board = []
        for i in range(self._row):
            row = []
            for j in range(self._col):
                row.append(0)
            self._board.append(row)

    def get_board(self) -> list[list[int]]:
        return self._board
    
    def print_board(self) -> None:
        print('--'+ ('----' * self._col) + '--')
        for i in range(self._row):
            print('| ', end = '')
            for j in range(self._col):
                print(f'{self._board[i][j]:>4}', end = '')
            print(' |')
        print('--'+ ('----' * self._col) + '--')
    
    def set_board(self, board: list[list[int]]) -> None:
        self._board = list(board)

    def get_empty(self) -> list[tuple[int,int]]:
        out = []
        for i in range(self._row):
            for j in range(self._col):
                if self._board[i][j] == 0:
                    out.append((i,j))
        return out
    
    def spawn(self) -> bool:
        starting_nums = [2,2,2,2,4]
        
        spots = self.get_empty()
        if len(spots) == 0:
            return False
        choice = random.choice(spots)
        self._board[choice[0]][choice[1]] = random.choice(starting_nums)

    def shift(self, nums :list[int]) -> list[int]:
        col = nums
        for i in range(len(col)-1,-1,-1):
            temp = i
            if col[temp] != 0:
                for j in range(i,len(col)):
                    if col[j] == 0:
                        col[j] = col[temp]
                        col[temp] = 0
                        temp = j
        return col
    
    def match(self, nums :list[int]) -> list[int]:
        col = nums
        for i in range(len(col)-2,-1,-1):
            if col[i] != 0 and col[i+1] == col[i]:
                col[i+1] *= 2
                col[i] = 0
        return col
    
    def process(self, nums :list[int]) -> list[int]:
        temp = self.shift(nums)
        temp = self.match(temp)
        temp = self.shift(temp)
        return temp 
    
    def down(self) -> None:
        pass

    def up(self) -> None:
        pass

    def right(self) -> None:
        for i in self._board:
            i = self.process(i)

    def left(self) -> None:
        pass

        