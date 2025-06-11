# OpenGL Tic Tac Toe

A simple 2-player Tic Tac Toe game implemented purely in OpenGL and GLUT (no Pygame).

## Features
- Pure OpenGL rendering (no external game engines)
- Mouse-click input handling
- Win/draw detection
- Text rendering using GLUT fonts
- Clean 2D orthographic projection

## How It Works
1. **Rendering**:
   - Uses OpenGL's immediate mode (`glBegin/glEnd`) for drawing
   - Grid lines drawn with `GL_LINES`
   - X's and O's rendered with primitives

2. **Game Logic**:
   - Tracks moves in a 3x3 array
   - Alternates players between X and O
   - Checks for wins/draws after each move

3. **Input**:
   - GLUT mouse callback converts clicks to grid positions
   - Only allows valid moves (empty squares)

## Requirements
- Python 3.x
- PyOpenGL (`pip install PyOpenGL PyOpenGL_accelerate`)

## How to Run
```bash
python tictactoe_opengl.py
