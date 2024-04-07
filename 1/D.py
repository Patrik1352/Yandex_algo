plait = []
for _ in range(8):
    plait.append(input().strip())



# Ввод состояния шахматной доски
board_input = plait

# Инициализация матрицы доски, где 0 - пустая клетка, 1 - слон, 2 - ладья, -1 - битая клетка
board = [[0 for _ in range(8)] for _ in range(8)]

# Размещение фигур на доске
for i in range(8):
    for j in range(8):
        if board_input[i][j] == 'B':
            board[i][j] = 1
        elif board_input[i][j] == 'R':
            board[i][j] = 2

# Функция для отметки битых клеток слоном
def mark_bishop_attacks(x, y):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d in directions:
        cx, cy = x, y
        while 0 <= cx + d[0] < 8 and 0 <= cy + d[1] < 8:
            cx += d[0]
            cy += d[1]
            if board[cx][cy] not in (0,-1):  # Встреча с другой фигурой
                break
            board[cx][cy] = -1

# Функция для отметки битых клеток ладьёй
def mark_rook_attacks(x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in directions:
        cx, cy = x, y
        while 0 <= cx + d[0] < 8 and 0 <= cy + d[1] < 8:
            cx += d[0]
            cy += d[1]
            if board[cx][cy] not in (0,-1):  # Встреча с другой фигурой
                break
            board[cx][cy] = -1

# Проходим по доске и отмечаем битые клетки
for i in range(8):
    for j in range(8):
        if board[i][j] == 1:  # Слон
            mark_bishop_attacks(i, j)
        elif board[i][j] == 2:  # Ладья
            mark_rook_attacks(i, j)

# Считаем количество небитых пустых клеток
safe_cells = sum(row.count(0) for row in board)
print(safe_cells)
