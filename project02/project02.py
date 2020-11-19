'''Module Project02'''
import random
'''Function that takes two arguements
x and y an returns a board of those
dimensions filled with Falses'''
def new_board(x, y):
	board = []
	for i in range(y):
		row = []
		for j in range(x):
			row.append(False)
		board.append(row)
	return board
'''Function that takes a board and randomizes
its contents and returns it'''
def randomize_board(board_arr):
	for i in range(len(board_arr)):
		for j in range(len(board_arr[0])):
			rand = random.random()
			if rand > 0.5:
				board_arr[i][j] = True
			else:
				board_arr[i][j] = False
	return board_arr
'''Function that converts the board to a string that is
shown on the console'''
def board_to_string(board_arr):
	string = ""
	for i in range(len(board_arr)):
		count = 0
		for j in range(len(board_arr[0])):
			if count > 0:
				string += " "
			if board_arr[i][j] == True:
				string += "X"
				count += 1
			else:
				string += "O"
				count += 1
		string += "\n"
	return string
''' Function that flips a cell to show either x or y 
depending on its value'''
def flip_cell(board_arr, x, y):
	if board_arr[x][y] == True:
		board_arr[x][y] = False
	else:
		board_arr[x][y] = True
	if x <= len(board_arr):
		if board_arr[x+1][y] == True:
			board_arr[x+1][y] = False
		else:
			board_arr[x+1][y] = True
	if x > 0:
		if board_arr[x-1][y] == True:
			board_arr[x-1][y] = False
		else:
			board_arr[x-1][y] = True
	if y <= len(board_arr[0]):
		if board_arr[x][y+1] == True:
			board_arr[x][y+1] = False
		else:
			board_arr[x][y+1] = True
	if y > 0:
		if board_arr[x][y-1] == True:
			board_arr[x][y-1] = False
		else:
			board_arr[x][y-1] = True
	return board_arr
'''Function that checks to see if the player has 
won the game or not'''
def is_winning(board_arr):
	arr_size = len(board_arr)*len(board_arr[0])
	x_count = 0
	o_count = 0
	for i in range(len(board_arr)):
		for j in range(len(board_arr[0])):
			if board_arr[i][j] == True:
				x_count += 1
			if board_arr[i][j] == False:
				o_count += 1
	return x_count == arr_size or o_count == arr_size

#var that checks to see if the game is over
game_over = False
#getting user input for dimensions of the board
x_coord,y_coord = input("Enter X and Y dimensions of you board: ").split(",")
x_coord = int(x_coord)
y_coord = int(y_coord)
#creating a new board and randomizing it
game_board = new_board(x_coord,y_coord)
game_board = randomize_board(game_board)
#running the game until it is over
while not game_over:
	#prints the board to the console
	print(board_to_string(game_board))
	#gets user input for what cell to slip
	x_flip, y_flip = input("Enter cordinates to flip cell: ").split(",")
	x_flip = int(x_flip)
	y_flip = int(y_flip)
	#flips the cell
	game_board = flip_cell(game_board,x_flip,y_flip)
	#checks to see if the game is over
	if is_winning(game_board):
		print("Game over! You win!")
		game_over = True


	
