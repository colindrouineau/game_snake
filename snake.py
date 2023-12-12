import pygame

WHITE = (150, 150, 150)
BLACK = (100, 100, 100)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
CLOCK_FREQUENCY = 5
TIME_LIMIT = 10 # s
LENGHT_TILES = 20
STARTING_POSITION = (10, 5) # en tiles
SNAKE_COLOR = (100, 200, 50)
DIRECTION = {'u': (-1,0), 'd': (1,0), 'l': (0,-1), 'r': (0,1)}

class snake_class:
    def __init__(self):
        self.position = [(10, 7), (10, 6), (10, 5)]
        self.direction = 'r'
    
    def afficher(self):
        for i, j in self.position:
            rect = pygame.Rect(j*20, i*20, LENGHT_TILES, LENGHT_TILES)
            pygame.draw.rect(screen, SNAKE_COLOR, rect)

    def avancer(self):
        for i in range(2, len(self.position)+1):
            self.position[-i+1] = self.position[-i]
        self.position[0] = (self.position[0][0] + DIRECTION[self.direction][0], self.position[0][1] + DIRECTION[self.direction][1])
        

pygame.init()
pygame.display.set_caption("snake.io")

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
clock = pygame.time.Clock()

def starting_screen():
    screen.fill( WHITE )
    for i in range(SCREEN_HEIGHT // LENGHT_TILES):
        for j in range(SCREEN_WIDTH //LENGHT_TILES):
            if (i + j) % 2 == 1:
                rect = pygame.Rect(20*j, 20*i, LENGHT_TILES, LENGHT_TILES)
                pygame.draw.rect(screen, BLACK, rect)

starting_screen()

rect = pygame.Rect(STARTING_POSITION[1]*20, STARTING_POSITION[0]*20, 3*LENGHT_TILES, LENGHT_TILES)
pygame.draw.rect(screen, SNAKE_COLOR, rect)

snake = snake_class()

while True :
    clock.tick(CLOCK_FREQUENCY)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'd':
                snake.direction = 'u'
            if event.key == pygame.K_DOWN and snake.direction != 'u':
                snake.direction = 'd'
            if event.key == pygame.K_LEFT and snake.direction != 'r':
                snake.direction = 'l'
            if event.key == pygame.K_RIGHT and snake.direction != 'l':
                snake.direction = 'r'

            if event.key == pygame.K_q:
                pygame.quit()
    
    snake.avancer()

    starting_screen()
    snake.afficher()
    pygame.display.update()