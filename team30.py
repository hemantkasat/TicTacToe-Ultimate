import random
import copy
import time
inf = 1000000000000

class Player30:

	def move(self,board,block,old_move,flag):
		global depth_allowed,t2

		t2 =time.time()
		depth_allowed = 0
		if block.count('-') <= 4:
			depth_allowed = 10 - block.count('-')
		if(old_move[0] == -1 and old_move[1] == -1):
                        return (3,3)
		allowed_moves = self.get_moves(board,block,old_move,flag)
		if len(allowed_moves) > 18 and depth_allowed > 4:
			depth_allowed = 4
		if len(allowed_moves) == 1:
			return (allowed_moves[0],allowed_moves[1])

		move = self.heuristic_func(board,block,allowed_moves,flag)
		#print time.time() - t2
		return move


	def heuristic_func(self,board,block,allowed_moves,flag):
		#global t2
		#t2 =time.time()
		return self.alpha_beta(board,block,allowed_moves,flag)
		#return allowed_moves[random.randrange(len(allowed_moves))]
	def alpha_beta(self,board,block,allowed_moves,flag):
		x,ans = self.max_value(board,block,allowed_moves,flag,-1*inf,inf,0,11.8/1.0)
		return ans

	def eval(self,board,block,flag):
		return self.winningposs(board,block,flag)

	def max_value(self,board,block,allowed_moves,flag,a,b,depth,rtime):
		t = 0.000025
		#if rtime <= 2*t:
		random.shuffle(allowed_moves)
		global depth_allowed,t2
		#depth_allowed = 0
		if (depth > depth_allowed and depth_allowed !=0) or (rtime <=2*t and depth_allowed == 0):
			a = 1
			if depth % 2:
				a = -1
			return a*self.eval(board,block,flag),allowed_moves[0]
		v = -1*inf
		ans = allowed_moves[0]
		#print rtime/float((len(allowed_moves)))
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			if len(next_moves) == 0:
				x = (10**6)*self.win(temp_block,flag)
			else:
				x,qq = self.min_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1,rtime/float(len(allowed_moves)+0.1))
			if v < x:
				v = x
				ans = move
			if v >= b:
				return v,ans
			if time.time() - t2 >= 11.9:
				return v,ans
			a = max(a,v)
		return v,ans

	def min_value(self,board,block,allowed_moves,flag,a,b,depth,rtime):
		t = 0.000025
		random.shuffle(allowed_moves)
#		if rtime <= 2*t:
		global depth_allowed,t2
		#depth_allowed = 0
		if (depth > depth_allowed and depth_allowed !=0) or (rtime <=2*t and depth_allowed == 0):
			a = 1
			if depth % 2:
				a = -1
			return a*self.eval(board,block,flag),allowed_moves[0]
		#"""
		#if depth > 4:
		#	return -1*self.eval(board,block,flag),allowed_moves[0]

		v = inf
		ans = allowed_moves[0]
		#print rtime/float((len(allowed_moves)))
		for move in allowed_moves:
			temp_board,temp_block = self.apply_move(board,block,move,flag)
			temp_flag = 'x'
			if flag =='x':
				temp_flag = 'o'
			next_moves = self.get_moves(temp_board,temp_block,move,temp_flag)
			if len(next_moves) == 0:
				x = (10**6)*self.win(temp_block,flag)
			else:
				x,qq = self.max_value(temp_board,temp_block,next_moves,temp_flag,a,b,depth+1,rtime/float(len(allowed_moves)+0.1))
			if v > x:
				v = x
				ans = move
			if v <= a:
				return v,ans
			if time.time() - t2 >= 11.9:
				return v,ans
			b = min(b,v)
		return v,ans

	def check(self,block,flag):
		inline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		for i in range(8):
			count = 0
			for j in range(3):
				if block[inline[i][j]] == flag:
					count+=1
			if count == 3:
				return True
		return False

	def win(self,block,flag):
		a = self.check(block,flag)
		if a:
			return 1
		nflag = 'x'
		if(flag == 'x'):
			nflag = 'o'
		a = self.check(block,nflag)
		if a:
			return -1
		return 0

	def evalwp(self,board,inline,flag):
		if '-' not in board:
			return [0,0]
		pc = 0
		pc2 = 0
		oc2 = 0
		oc = 0
		oflag = 'x'
		if flag == 'x':
			oflag = 'o'
		for seq in inline:
			fil_seq = [board[i] for i in seq if board[i] != '-']
			if flag in fil_seq:
				if oflag in fil_seq:
					continue
				if len(fil_seq) > 1:
					pc += 7
					pc2 += 9
				if len(fil_seq) > 2:
					pc += 7
					pc2 += 90
				pc += 1
				pc2 += 1
			elif oflag in fil_seq:
				if len(fil_seq) > 1:
					oc += 7
					oc2 += 9
				if len(fil_seq) > 2:
					oc += 7
					oc2 += 90
				oc += 1
				oc2 += 1
		return [pc - oc,pc2 - oc2]

	def winningposs(self,board,block,flag):
		inline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
		if self.win(block,flag):
			a = self.win(block,flag)
			return 10**6 * a

		if '-' not in block:
			return 0

		lis2 = []
		#ret = 25*self.evalwp(block,inline,flag)[0]
		for i in range(9):
			r = i/3
			c = i%3
			lis = []
			for j in range(3):
				for k in range(3):
					lis.append(board[3*r+j][3*c+k])
			a = self.evalwp(lis,inline,flag)
			#ret += a[0]
			lis2.append(a[1])

		ret = 0
		for i in range(8):
			val = 0
			for j in range(3):
				val += lis2[inline[i][j]]
			val /= 100.0
			if val<=-3:
				ret += ( -3 + (val+3)*90) *2
			elif val>-3 and val<=-2:
				ret += ( -2 + (val+2)*9 )*2
			elif val>-2 and val<=2:
				ret += val*2
			elif val> 2 and val<=3:
				ret += (2 + (val-2)*9)*2
			else:
				ret += (3 + (val-3)*90 )*2
		return ret

	def apply_move(self,board,block,move,flag):
		block2 = copy.deepcopy(block)
		board2 = copy.deepcopy(board)
		board2[move[0]][move[1]] = flag
		block2 = self.update_block(board2,block2,move,flag)
		return board2,block2

	def update_block(self,board,block,move,flag):
		block_r = move[0]/3
		block_c = move[1]/3

		#horizontal direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			if(j>block_r*3+2 or j<block_r*3 ):
				continue
			elif(board[j][move[1]] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#vertical direction
		count = 0
		for i in range(5):
			j = move[1]+i-2
			if(j>block_c*3+2 or j<block_c*3 ):
				continue
			elif(board[move[0]][j] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#diagonal-left direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			k = move[1]+i-2
			if(j>block_r*3+2 or j<block_r*3 or k>block_c*3+2 or k<block_c*3 ):
				continue
			elif(board[j][k] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag
			return block

		#diagonal-right direction
		count = 0
		for i in range(5):
			j = move[0]+i-2
			k = move[1]+2-i
			if(j>block_r*3+2 or j<block_r*3 or k>block_c*3+2 or k<block_c*3 ):
				continue
			elif(board[j][k] == flag):
				count+=1
		if count == 3:
			block[3*block_r+block_c] = flag

		return block


	def get_moves(self,board,block,old_move,flag):

		blocks_allowed = []
		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			blocks_allowed = [1,3]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
			blocks_allowed = [1,5]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
			blocks_allowed = [3,7]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
			blocks_allowed = [5,7]
		elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
			blocks_allowed = [0,2]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
			blocks_allowed = [0,6]
		elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
			blocks_allowed = [6,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
			blocks_allowed = [2,8]
		elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
			blocks_allowed = [4]
		else:
			sys.exit(1)

		#print old_move
		#print blocks_allowed


		for i in blocks_allowed:
			if block[i] != '-':
				blocks_allowed.remove(i)

		for i in blocks_allowed:
			if block[i] != '-':
				blocks_allowed.remove(i)

		#print blocks_allowed

		if blocks_allowed == []:
			for i in range(len(block)):
				if block[i] == '-':
					blocks_allowed.append(i)

		return self.get_empty(board,block,blocks_allowed)

	def get_empty(self,board,block,blocks_allowed):

		cells = []
		for i in range(len(blocks_allowed)):
			r = blocks_allowed[i]/3
			c = blocks_allowed[i]%3
			for j in range(r*3,r*3+3):
				for k in range(c*3,c*3+3):
					if board[j][k] == '-':
						cells.append((j,k))


		if cells == []:
			for i in range(len(block)):
				if block[i] == '-':
					blocks_allowed.append(i)

			for i in range(len(blocks_allowed)):
				r = blocks_allowed[i]/3
				c = blocks_allowed[i]%3
				for j in range(r*3,r*3+3):
					for k in range(c*3,c*3+3):
						if board[j][k] == '-':
							cells.append((j,k))
		return cells
