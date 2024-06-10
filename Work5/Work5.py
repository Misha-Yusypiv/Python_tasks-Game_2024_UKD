import tkinter as tk  # Імпортуємо модуль для створення візуального інтерфейсу
from tkinter import messagebox  # Імпортуємо модуль для сповіщень у вікні

def check_winner(board, player):
    """Перевіряємо, чи є переможець у грі."""
    # Перевірка по горизонталі
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Перевірка по вертикалі
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Перевірка по діагоналі
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def on_click(row, col):
    """Викликається при кліку на кнопку. Обробляє хід гравця та перевіряє переможця."""
    global current_player, moves_left
    # Перевірка, чи клітинка вільна
    if board[row][col] != " ":
        messagebox.showerror("Невірний хід", "Клітинка вже зайнята. Спробуйте ще раз.")
        return

    # Збереження ходу та зміна гравця
    board[row][col] = players[current_player]
    buttons[row][col].config(text=players[current_player], state=tk.DISABLED)
    moves_left -= 1

    # Перевірка переможця або нічиєї
    if check_winner(board, players[current_player]):
        messagebox.showinfo("Переможець", f"Гравець {players[current_player]} виграв!")
        reset_game()
    elif moves_left == 0:
        messagebox.showinfo("Нічия", "Гра закінчилась у нічию!")
        reset_game()
    else:
        current_player = (current_player + 1) % 2

def reset_game():
    """Скидає гру до початкового стану."""
    global board, current_player, moves_left
    board = [[" " for _ in range(3)] for _ in range(3)]
    moves_left = 9
    current_player = 0
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state=tk.NORMAL)

root = tk.Tk()  # Створюємо вікно для гри
root.title("Хрестики-нолики")  # Встановлюємо заголовок вікна

board = [[" " for _ in range(3)] for _ in range(3)]  # Ініціалізуємо дошку
players = ["X", "O"]  # Встановлюємо гравців
current_player = 0  # Починаємо з першого гравця
moves_left = 9  # Лічильник доступних ходів

buttons = []  # Список кнопок для клітинок на дошці
# Створюємо кнопки та розміщуємо їх на вікні
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                            command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)  # Розміщуємо кнопку на вікні
        button_row.append(button)  # Додаємо кнопку до рядка
    buttons.append(button_row)  # Додаємо рядок кнопок до списку

root.mainloop()  # Запускаємо головний цикл для роботи вікна
