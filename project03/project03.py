''' Module project03.py'''
import random
import string

def new_board():
    # creates a empty list
    board = []

    # going through and adding random letters to the board
    for i in range(0, 4):
        inner_board = []
        for j in range(0, 4):
            char = random.choice(string.ascii_letters)
            inner_board.append(char.upper())
        board.append(inner_board)

    # returns the list board with random letters filled in it
    return board

def board_to_string(board):
    # creates an emptry string
    result = ""

    # variable that takes care of adding newlines at the right point
    count = 0

    for i in range(len(board)):

        # variable that takes care of adding spaces at the right point
        space_count = 0

        for j in range(len(board[i])):
            result += "["
            result += board[i][j]
            result += "]"
            space_count += 1

            if space_count < 4:
                result += " "
        count += 1
        if count < 4:
            result += "\n"

    # returns the string result with all the content of the board in it
    return result

def board_has_word(board, word, used_cells=None):
    if used_cells is None:
        # grabbing the first letter in the word, and finding all the cells
        # that have it
        starting_cells = cells_with_letter(board, word[0])

        # if no cells are found that means the word does not exist which
        # means return False
        if not starting_cells:
            return False

        # if we do find some starting points then we can work out the base case
        # base case
        # if the wod is a single character means we have found the word and
        # game is over
        if len(word) == 1 and len(starting_cells) > 0:
            return True

        # recursive case
        if len(word) > 1:
        # we start at each possible statying point to see if the remainder
        # of the word can be found there
            for cell in starting_cells:
                # the recursive case needs to know what starting cell has been
                # chosen
                # so it is passed as the only element of a new list in the
                # used_cells
                return board_has_word(board, word[1:], [cell])
    if used_cells is not None:
        # storing the last item in the used_cells as the current cell
        current_cell = used_cells[-1]

        # storing all of the possible neighbors of the current cell
        neighbors = adjacent_cells(current_cell)

        # removing all the used_cells from the neighbors
        neighbors = [cell for cell in neighbors if not cell in used_cells]

        # removing all neighbors that dont contain the letter that
        # is being looked for
        neighbors = [c for c in neighbors if word[0] == board[c[0]][c[1]]]

        # checking if there are any possibilities remaining
        #if not, cannot go any further, return False
        if not neighbors:
            return False

        # it can be assumed that there are possible paths remaining
        # recursion can be used again
        # Base case:
        if len(word) == 1:
            #this is the last character in the word
            return True

        # Recusrive case:
        if len(word) > 1:
            # now it can be seen if the remainder of the word can
            # be found from here
            for neighbor in neighbors:
                # each recusrive call needs to know what neighbor it is
                # starting from so we append the neighbors to the used cells
                return board_has_word(board, word[1:], used_cells + [neighbor])

def adjacent_cells(current_cell):
    # list of tuples representing the coordinates of adjacent cells
    adjacent_cells = []

    # storing  the x and y values of the current cell in the variables
    x = current_cell[0]
    y = current_cell[1]

    # checking for cells above
    if y > 0:
        adjacent_cells.append((x, y - 1))

    # checking for cells below
    if y < 3:
        adjacent_cells.append((x, y + 1))

    # checking for cells to the left
    if x > 0:
        adjacent_cells.append((x + 1, y))

    # checking for cells to the right
    if x < 3:
        adjacent_cells.append((x - 1, y))

    # checking for top left diagonal
    if x > 0 and y > 0:
        adjacent_cells.append((x-1, y-1))

    # checking for top right diagonal
    if x < 3 and y > 0:
        adjacent_cells.append((x+1, y-1))

    # checking for bottom left diagonal
    if y < 3 and x > 0:
        adjacent_cells.append((x-1, y+1))

    # checking for bottom right diagonal
    if y < 3 and x < 3:
        adjacent_cells.append((x+1, y+1))

    # returns the list adjacent cells with the location as tuples
    return adjacent_cells

def cells_with_letter(board, letter):
    # creating a new list to store the location as tuples
    letters = []

    # iterating through the list to get the location of the letter
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == letter:

                # adding the location of the letter to the list
                letters.append((j, i))

    # returns nothing if the letter does not exist
    if not letters:
        return None

    # returns the list letters that cotains the locations of all
    # instances of the letter on the board
    return letters
