from mrinal import Player57
import time

self = Player57()

old_move = (0,7)
board = [['o', 'o', 'o', 'o', '-', '-', 'x', 'o', '-'], ['-', '-', '-', 'o', '-', 'x', 'o', 'x', 'x'], ['-', 'o', 'x', 'o', 'x', 'x', 'x', 'x', 'o'], ['o', '-', 'x', 'x', 'x', 'x', 'x', 'o', 'o'], ['-', '-', 'x', '-', 'o', '-', 'x', 'o', 'o'], ['o', '-', 'x', 'o', '-', '-', 'o', '-', 'x'], ['x', '-', 'x', '-', 'x', '-', 'o', 'o', 'o'], ['o', 'x', '-', '-', 'x', '-', '-', '-', '-'], ['-', 'o', 'x', '-', 'x', 'o', '-', '-', '-']]
block = ['o', 'o', '-', 'x', 'x', 'o', 'x', 'x', 'o']
flag = 'x'
t =time.time()
move = self.move(board,block,old_move,flag)
print move
print time.time() - t
