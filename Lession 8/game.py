import pygame

pygame.init()
screen = pygame.display.set_mode([576,576])

done = False
game_finish = False

COLOR_GREEN = [0,200,0]

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def calc_next(self,dx,dy):
        return [self.x + dx, self.y + dy]

class Box():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def calc_next_position(self,dx,dy):
        return [self.x + dx, self.y + dy]

class Gate():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Map():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.player = Player(1,3)
        self.box = Box(3,2)
        self.gate = Gate(2,4)

    def check_inside(self,x,y):
        if 0<= x < self.width and 0 <= y < self.height:
            return True
        return False

    def move_object(self,dx,dy):
        [next_player_x, next_player_y] = self.player.calc_next(dx,dy)
        [next_box_x, next_box_y] = self.box.calc_next_position(dx,dy)
        if not self.check_inside(next_player_x, next_player_y):
            None
        else:
            if next_player_x == self.box.x and next_player_y == self.box.y:
                if self.check_inside(next_box_x, next_box_y):
                    self.player.move(dx,dy)
                    self.box.move(dx,dy)
            else:
                self.player.move(dx,dy)

    def win(self):
        if self.box.x == self.gate.x and self.box.y == self.gate.y:
            return True
        return False

map = Map(18,18)
SQUARE_SIZE = 32

image = pygame.image.load('mario.png')
square = pygame.image.load('square.png')
image_box = pygame.image.load('box.jpg')
image_gate = pygame.image.load('gate.png')
image_win = pygame.image.load('win.jpg')

while not done:
    dx=0
    dy=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
            else:
                dx, dy = 0, 0

    if dx !=0 or dy !=0:
        map.move_object(dx,dy)
        if map.win():
            game_finish = True

    screen.fill(COLOR_GREEN)

    for y in range(map.height):
        for x in range(map.width):
            screen.blit(square,(x * SQUARE_SIZE, y * SQUARE_SIZE ))

    screen.blit(image_gate, (map.gate.x * SQUARE_SIZE, map.gate.y * SQUARE_SIZE))
    screen.blit(image_box, (map.box.x * SQUARE_SIZE, map.box.y * SQUARE_SIZE))
    screen.blit(image, (map.player.x * SQUARE_SIZE, map.player.y * SQUARE_SIZE))

    if game_finish == True:
        screen.blit(image_win,(0,0))

    pygame.display.flip()