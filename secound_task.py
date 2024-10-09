import pygame
import time

# написання кольрів у стилі RGB тобто по цифрам
# колір брався з color picker ось ссилка: https://www.google.com/search?q=Color+Picker&sca_esv=4fc2b25e9d5170f8&biw=1536&bih=730&sxsrf=ADLYWIK7e6CXOGAGDrkVX6zYWH2HqdWm8A%3A1728304510353&ei=ftUDZ4ySFaSCxc8Pv4HvgQE&ved=0ahUKEwiMyZyDpPyIAxUkQfEDHb_AOxAQ4dUDCA8&oq=Color+Picker&gs_lp=Egxnd3Mtd2l6LXNlcnAiDENvbG9yIFBpY2tlcjIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzIKEAAYsAMY1gQYRzINEAAYgAQYsAMYQxiKBTINEAAYgAQYsAMYQxiKBUjSD1AAWABwAXgBkAEAmAEAoAEAqgEAuAEMyAEAmAIBoAIHmAMAiAYBkAYKkgcBMaAHAA&sclient=gws-wiz-serp
WHITE = (255, 255, 255) # білий
BLACK = (0, 0, 0) # чорний
GREEN = (0, 255, 0) # зелений
RED = (255, 0, 0) # червоний
GREY = (99, 99, 99) # сірий

GRID_WIDTH = 20 # кількість клітинок по ширині
GRID_HEIGHT = 10  # кількість клітинок по висоті
CELL_SIZE = 35  # розмір клітинок у пікселях

# ініціалізація pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Лабіринт")

# матриця лабіринту
maze = [
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

player_pos = [0, 0] # тут координати спавну комп'ютер
exit_pos = [9, 19]  # тут координати фінішу

# Функція для малювання лабіринту
def draw_maze():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # ці 2 рядка нижче візуалізують сам лабіринт тут використовуються параметри лабіринту 13-15 рядки, чорний кольор
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # оконтовка клітинок лабіринт тут використовується те саме що і у рядку вище тільки колір сірий для оконтовки
            pygame.draw.rect(screen, GREY, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    # відображення клітинки-вихід тут використовується параметри лабіринту 13-15 рядки, зелений кольор 8 рядка і позиція яка написана на 35 рядка
    pygame.draw.rect(screen, GREEN, pygame.Rect(exit_pos[1] * CELL_SIZE, exit_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Функція для малювання комп'ютер
def draw_player():
    pygame.draw.rect(screen, RED, pygame.Rect(player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Функція для відстеження (backtracking) та знаходження виходу
def backtrack(x, y):
    # Перевірка, чи досягли виходу
    if [x, y] == exit_pos:
        return True

    # Помічаємо клітинку як відвідану (1)
    maze[x][y] = 2  # Використовуємо 2 для позначення відвіданих шляхів

    # Можливі рухи: вгору, вниз, вліво, вправо
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # Перевірка, чи нова позиція в межах лабіринту і не була відвідана
        if 0 <= nx < GRID_HEIGHT and 0 <= ny < GRID_WIDTH and maze[nx][ny] == 0:
            # Оновлюємо позицію комп'ютер
            global player_pos
            player_pos = [nx, ny]
            # малюємо комп'ютер
            draw_player()
            # оновлюємо картинку тобто дісплей
            pygame.display.update()
            time.sleep(0.2)  # Затримка для візуалізації руху

            if backtrack(nx, ny):
                return True
    return False

# Основний цикл
running = True
while running:
    screen.fill(WHITE)
    draw_maze()  # буквально малюємо або ж відображаємо лабіринт
    draw_player()  # буквально малюємо або ж відображаємо комп'ютер

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # перевірка, чи пройшов комп'ютер до виходу
    if player_pos == [0, 0]:  
        if backtrack(player_pos[0], player_pos[1]):
            # якщо гравець досяг кінцевої точки тобто вихід 
            # виводимо Вітаємо, комп'ютер знайшов вихід з лабіринту! і завершуємо гру
            print("Вітаємо, комп'ютер знайшов вихід з лабіринту!")
        else:
            # якщо комп'ютер не досяг кінцевої точки
            # виводимо що Комп'ютер не зміг знайти вихід :( і завершуємо гру
            print("Комп'ютер не зміг знайти вихід :(")
        running = False  # завершуємо гру

    pygame.display.update()  # оновлюємо кадр у грі, він треба щоб показати куди здвинувся гравець

# Завершення гри
pygame.quit()