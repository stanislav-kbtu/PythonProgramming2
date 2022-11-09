import numpy as np

dict = {0 : [i for i in range(3)],
        1 : [i for i in range(3, 6)],
        2 : [i for i in range(6, 9)]}
class Sudoku():

    def __init__(self, s):
        self.s = s
        self.board = np.array([list(s[i*9:(i+1)*9]) for i in range(9)])

    def get_row(self, N):
        return self.board[N]

    def get_col(self, N):
        return self.board.transpose()[N]
        
    def get_sqr(self, lis):
        res = ""
        if len(lis) == 1:
            n = lis[0] 
            cols = n%3 # 0 - [0, 1, 2]: 0 column => rows*9 + cols
            rows = int((n)/ 3) # 0 - [0, 1, 2]:
            for i in dict[rows]:

                for j in dict[cols]:

                    res += self.s[i*9 + j]
            return np.array(list(res))
        elif len(lis) == 2:

            rows = int(lis[1] / 3) 
            cols = lis[0] % 3
            for i in dict[rows]:

                for j in dict[cols]:

                    res += self.s[i*9 + j]
            return np.array(list(res))


game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
print(game.board)
print(game.get_row(8))
print(game.get_col(8))
print(game.get_sqr([1]))
print(game.get_sqr([1, 8]))