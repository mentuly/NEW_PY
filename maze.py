# це той же лабіринт але тут людина сама вибирає куди йти (двигатися стрілочками), просто коли я писав цей код я не до кінця зрозумів що таке backtrack і ось так вийшло
import pygame

# НАписання кольрів у стилі RGB тобто по цифрам
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
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

player_pos = [0, 0] # тут координати спавну комп'ютер
exit_pos = [9, 19]  # тут координати фінішу

# функція що відображає лабіринт
def draw_maze():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GREY, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    
    # відображення клітинки-вихід
    pygame.draw.rect(screen, GREEN, pygame.Rect(exit_pos[1] * CELL_SIZE, exit_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# функція що відображає гравця
def draw_player():
    pygame.draw.rect(screen, RED, pygame.Rect(player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# основний цик, можна було і не вписувати до основного циклу 56 строку але я її сюди поставив тільки тому що game_won використовується тільки тут і ставити його десь вище, мені задлося, що буде недоречним
game_won = False
running = True
while running:
    screen.fill(WHITE)
    draw_maze()  # буквально малюємо або ж відображаємо лабіринт
    draw_player()  # буквально малюємо або ж відображаємо гравця
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # якщо гра не виграна, обробляємо рухи гравця
        # тут ще використовуються K_LEFT, K_RIGHT і тд то вони якби і створюють сам цей рух у коді
        if event.type == pygame.KEYDOWN and not game_won:
            x, y = player_pos[0], player_pos[1]
            
            if event.key == pygame.K_LEFT:
                y -= 1  # рух вліво
            if event.key == pygame.K_RIGHT:
                y += 1  # рух вправо
            if event.key == pygame.K_UP:
                x -= 1  # рух вгору
            if event.key == pygame.K_DOWN:
                x += 1  # рух вниз

            # перевірка чи можна рухатися в на нову клітинку, щоб наш гравець не проходив крізь стіни
            if 0 <= x < GRID_HEIGHT and 0 <= y < GRID_WIDTH and maze[x][y] == 0:
                player_pos = [x, y]

            # якщо гравець досяг кінцевої точки тобто вихід, то game_won робимо True, виводимо що користувач пройшов лабіринт і завершуємо гру
            if player_pos == exit_pos:
                game_won = True
                print("Вітаємо, ви знайшли вихід з лабіринту!")
                running = False  # завершуємо гру

    pygame.display.update()  # оновлюємо кадр у грі, він треба щоб показати куди здвинувся гравець

# завершення гри
pygame.quit()