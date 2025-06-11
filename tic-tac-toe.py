from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math  # Add this import for cos and sin functions

# Game constants
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Game state
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 1  # 1 for X, 2 for O
game_over = False
winner = None

def init():
    glClearColor(0.2, 0.3, 0.3, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, HEIGHT, 0)  # 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)

def draw_grid():
    glColor3f(1.0, 1.0, 1.0)  # White lines
    glLineWidth(3.0)
    
    # Vertical lines
    for i in range(1, BOARD_SIZE):
        glBegin(GL_LINES)
        glVertex2f(i * SQUARE_SIZE, 0)
        glVertex2f(i * SQUARE_SIZE, HEIGHT)
        glEnd()
    
    # Horizontal lines
    for i in range(1, BOARD_SIZE):
        glBegin(GL_LINES)
        glVertex2f(0, i * SQUARE_SIZE)
        glVertex2f(WIDTH, i * SQUARE_SIZE)
        glEnd()

def draw_x(x, y):
    glColor3f(1.0, 0.0, 0.0)  # Red X
    glLineWidth(5.0)
    
    center_x = x * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = y * SQUARE_SIZE + SQUARE_SIZE // 2
    offset = SQUARE_SIZE // 3
    
    glBegin(GL_LINES)
    # First diagonal
    glVertex2f(center_x - offset, center_y - offset)
    glVertex2f(center_x + offset, center_y + offset)
    # Second diagonal
    glVertex2f(center_x + offset, center_y - offset)
    glVertex2f(center_x - offset, center_y + offset)
    glEnd()

def draw_o(x, y):
    glColor3f(0.0, 0.0, 1.0)  # Blue O
    glLineWidth(5.0)
    
    center_x = x * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = y * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 3
    
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = i * 3.14159 / 180
        glVertex2f(center_x + radius * math.cos(angle), 
                  center_y + radius * math.sin(angle))
    glEnd()

def draw_game_state():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == 1:
                draw_x(x, y)
            elif board[y][x] == 2:
                draw_o(x, y)

def draw_status():
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(10, 20)
    
    status = ""
    if winner:
        status = f"Player {'X' if winner == 1 else 'O'} wins!"
    elif game_over:
        status = "Game ended in a draw!"
    else:
        status = f"Player {'X' if current_player == 1 else 'O'}'s turn"
    
    for char in status:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def check_win():
    # Check rows
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    
    # Check columns
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def check_draw():
    for row in board:
        if None in row:
            return False
    return True

def mouse_click(button, state, x, y):
    global current_player, game_over, winner
    
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and not game_over:
        col = x // SQUARE_SIZE
        row = y // SQUARE_SIZE
        
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] is None:
            board[row][col] = current_player
            
            winner = check_win()
            if winner:
                game_over = True
            elif check_draw():
                game_over = True
            else:
                current_player = 3 - current_player  # Switch player (1 ↔️ 2)
            
            glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    draw_game_state()
    draw_status()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Tic Tac Toe")
    
    init()
    
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    glutMainLoop()

if __name__ == "__main__":
    main()
