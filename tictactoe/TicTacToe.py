# MODULES
import pygame, sys

import math
from random import choice
import time

# initializes pygame
pygame.init()

# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 5
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 100
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 5
CROSS_WIDTH = 10
SPACE = 25

SPACE_AROUND = 150
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (255, 255, 255)
CROSS_COLOR = (255, 255, 255)


human_result = 0
ai_result = 0

#font = pygame.font.Font('arcade.ttf', 50)
#human_result_text = font.render(str(human_result) , True, (255, 255, 255))

#ai_result_text = font.render(str(ai_result) , True, (255, 255, 255))

#human_text = font.render('YOU' , True, (255, 255, 255))

#ai_text = font.render('AI' , True, (255, 255, 255))

# ------
# SCREEN
# ------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BG_COLOR )


board = [ ['', '', ''],
          ['', '', ''],
          ['', '', ''] ]

players = ['x', 'o']
player = players[0]

def draw_lines():
    
    #scores
    #pygame.draw.line( screen, (255, 0, 0), (100, 50), (WIDTH-100, 50), LINE_WIDTH )
    
    #pygame.draw.line( screen, (255, 0, 0), (WIDTH // 2, 0), (WIDTH // 2, 50), LINE_WIDTH )
    
    
    # 1 horizontal
    pygame.draw.line( screen, LINE_COLOR, (150, 250), (WIDTH - 150, 250), LINE_WIDTH )
    # 2 horizontal
    pygame.draw.line( screen, LINE_COLOR, (150, 2 * 100 + 150), (WIDTH - 150, 2 * 100 + 150), LINE_WIDTH )

    # 3 horizontal
    pygame.draw.line( screen, LINE_COLOR, (150, 150), (WIDTH - 150, 150), LINE_WIDTH )
    # 4 horizontal
    pygame.draw.line( screen, LINE_COLOR, (150, 3 * 100 + 150), (WIDTH - 150, 3 * 100 + 150), LINE_WIDTH )

    # 1 vertical
    pygame.draw.line( screen, LINE_COLOR, (250, 150), (250, HEIGHT - 150), LINE_WIDTH )
    # 2 vertical
    pygame.draw.line( screen, LINE_COLOR, (2 * 100 + 150, 150), (2 * 100 + 150, HEIGHT - 150), LINE_WIDTH )

    # 3 vertical
    pygame.draw.line( screen, LINE_COLOR, (150, 150), (150, HEIGHT - 150), LINE_WIDTH )
    # 4 vertical
    pygame.draw.line( screen, LINE_COLOR, (3 * 100 + 150, 150), (3 * 100 + 150, HEIGHT - 150), LINE_WIDTH )

    #pygame.draw.aaline(screen, (0, 0, 255), (600, 0), (0, 479), 20)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'o':
                pygame.draw.circle( screen, CIRCLE_COLOR, ( int( col * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE//2 ) ), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 'x':
                pygame.draw.aaline( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE_AROUND + SPACE, row * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE_AROUND + SPACE), CROSS_WIDTH )    
                pygame.draw.aaline( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE_AROUND + SPACE, row * SQUARE_SIZE + SPACE_AROUND + SPACE), (col * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE_AROUND + SQUARE_SIZE - SPACE), CROSS_WIDTH )
                


def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == ''

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                return False

    return True


def is_board_empty():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != '':
                return False

    return True



def equals3(a, b, c):
    return a == b and b == c and a != ''



def check_win():
    
    winner = None;

  # Horizontal
    for i in range(0,3):
        if (equals3(board[i][0], board[i][1], board[i][2])):
            winner = board[i][0]

  # Vertical
    for i in range(0,3):
        if (equals3(board[0][i], board[1][i], board[2][i])):
            winner = board[0][i]

  # Diagonal
    if (equals3(board[0][0], board[1][1], board[2][2])):
        winner = board[0][0]
  
    if (equals3(board[2][0], board[1][1], board[0][2])):
        winner = board[2][0]

    openSpots = 0
    
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == ''):
                openSpots = openSpots + 1

    if (winner == None and openSpots == 0):
        return 'tie'
    else:
        return winner




scores = {'x': 1, 'o': -1, 'tie': 0}

def minimax(board, depth, is_max):

    result = check_win()
    if result is not None:
        score = scores[result]
        return score

    if is_max:
        best_score = -math.inf
        for y in range(0,3):
            for x in range(0,3):
                if board[x][y] == '':
                    board[x][y] = 'x'
                    score = minimax(board, depth + 1, False)
                    board[x][y] = ''

                    best_score = max(score, best_score)
        return best_score

    else:            
        best_score = math.inf
        for y in range(0,3):
            for x in range(0,3):
                if board[x][y] == '':
                    board[x][y] = 'o'
                    score = minimax(board, depth + 1, True)
                    board[x][y] = ''

                    best_score = min(score, best_score)
        return best_score


def ai_move():
        
        best_score = -math.inf
        move = (0, 0)
        
        global player, board, ai_result
        
        if is_board_empty():
            arr_3 = [0, 1, 2]
            i = choice(arr_3)
            j = choice(arr_3)
            
            mark_square( i, j, player)
            draw_figures()
            player = players[1]
            aiTurn = False
            
        else:    
            for i in range(0,3):
                for j in range(0,3):
                    if board[i][j] == '':
    
                        board[i][j] = 'x'
                        score = minimax(board, 0, False)
                        
                        board[i][j] = ''
                        
                        if(score > best_score):
                            best_score = score
                            move = (i, j)
                        
            mark_square( move[0], move[1], player)
            winner = check_win()
            
            if winner != None:
                ai_result = ai_result + 1
                game_over = True
            
            draw_figures()
            player = players[1]
            aiTurn = False
        
                        
        

def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''
    
    

draw_lines()

aiTurn = True
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if(aiTurn):
            ai_move()
            aiTurn = False
            

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and not aiTurn:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            player = players[1]
            
            
            if( (mouseX > 150 and mouseY > 150) and (mouseX < 450 and mouseY < 450)):
                    mx = int ((mouseX - 150) // (SQUARE_SIZE))
                    my = int ((mouseY - 150) // (SQUARE_SIZE))

                    if available_square( my, mx ):

                        mark_square( my, mx, player )
                        
                        winner = check_win()
                        if winner != None:
                            human_result = human_result + 1
                            game_over = True
                        
                        player = players[0]

                        draw_figures()
                        aiTurn = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = players[0]
                game_over = False
                aiTurn = True
        
        
    
    #human_result_text = font.render(str(human_result) , True, (255, 255, 255))
    #screen.blit(human_result_text, (260, 3))
    
    #ai_result_text = font.render(str(ai_result) , True, (255, 255, 255))
    #screen.blit(ai_result_text, (320, 3))
    
    #screen.blit(human_text, (10, 3))
    #screen.blit(ai_text, (520, 3))
    pygame.display.update()
    
