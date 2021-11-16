import tkinter as Tk

h = 500
w = 500
canvas = Tk.Canvas(width = w, height = h)
canvas.pack()

size = 50
rows = h / size
cols = h / size

players = {
    1 : "x",
    -1 : "o"
}
current_p = 1

board = []

def drawGame():
    x, y = 0, -50
    for i in range(int(cols)):
        x = 0
        y += 50
        for j in range(int(rows)):
            canvas.create_rectangle(x, y, x + size, y + size)
            x += 50

def createGameDb():
    global board
    row = []

    for i in range(int(rows + 1)):
        if row: board.append(row)
        row = []
        for j in range(int(cols)):
            row.append(None)

def drawPlayer(x, y, player):
    if player == "x":
        canvas.create_line(x, y, x + size, y + size)
        canvas.create_line(x, y + size, x + size, y)
    elif player == "o":
        canvas.create_oval(x, y, x + size, y + size)

def showWinMsg(winner):
    txt = winner.upper()
    canvas.create_text(w//2, h//2, text=f"Výťazom je {txt}")

def checkWinner(x, y):
    try:
        if board[x][y] == board[x-1][y] and board[x][y] == board[x-2][y]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x-1][y-1] and board[x][y] == board[x-2][y-2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x][y-1] and board[x][y] == board[x][y-2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x+1][y-1] and board[x][y] == board[x+2][y-2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x+1][y] and board[x][y] == board[x+2][y]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])            
        elif board[x][y] == board[x+1][y+1] and board[x][y] == board[x+2][y+2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x][y+1] and board[x][y] == board[x][y+2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == board[x-1][y+1] and board[x][y] == board[x-2][y+2]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == [x+1][y] and board[x][y] == board[x-1][y]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == [x][y-1] and board[x][y] == board[x][y+1]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == [x+1][x-1] and board[x][y] == board[x-1][y+1]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
        elif board[x][y] == [x-1][y-1] and board[x][y] == board[x+1][y+1]:
            print(f"Winner is: {board[x][y]}")
            showWinMsg(board[x][y])
    except IndexError:
        pass

def click(e):
    global current_p
    global board

    row = e.x//size
    col = e.y//size

    if board[col][row] == None:
        board[col][row] = players[current_p]
        drawPlayer(row * size, col * size , players[current_p])
    else: 
        print("Pole zabraté!!!")
    current_p *= -1

    print(f"Clicked row is {row}")
    print(f"Clicked col is {col}")
    checkWinner(col, row)

    for row in board:
        print(row)
    print("------------------------------------")
    

drawGame()
createGameDb()



canvas.bind("<Button-1>", click)

canvas.mainloop()


