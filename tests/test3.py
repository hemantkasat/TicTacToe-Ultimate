from team30 import Player30

v = Player30()

board = [['x','x','x','-','-','-','x','x','x'],['x','x','x','-','-','-','x','x','x'],['x','x','x','-','-','-','x','x','x'],['-', '-', '-', '-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-', '-', '-', '-'],['-', '-', '-', '-', '-', '-', '-', '-', '-']] 
block = ['x','-','x','-','-','-','-','-','-']

flag = 'o'
allowed_moves = v.get_moves(board,block,(3,4),flag)
move = v.heuristic_func(board,block,allowed_moves,flag)
print move

