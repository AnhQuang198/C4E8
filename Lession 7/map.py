from player import Player
from box import Box
from gate import Gate
class Map:
    def __init__(self, width, height):
        self.player = Player(0,0)
        self.box = Box(3,1)
        self.gate = Gate(2,3)
        self.width = width
        self.height = height

    def print(self):
        for y in  range(self.height):
            for x in range(self.width):
                if x == self.player.x and y == self.player.y:
                    print("P ", end="")
                elif x == self.box.x and y == self.box.y:
                    print("B ",end="")
                elif x == self.gate.x and y == self.gate.y:
                    print("G ",end="")
                else:
                    print("_ ",end="")
            print()

    def move_player(self, dx, dy):
        self.player.move(dx,dy)

    def move_box(self, dx, dy):
        self.box.move(dx,dy)

    def in_map(self, x, y, width, height):
        if x < 0 or y < 0 or x > width - 1 or y > height - 1:
            return False
        return True

    def win(self):
        if self.box.x == self.gate.x and self.box.y == self.gate.y:
            return True

    def process_input(self, move):
        direction = move.upper()
        if  direction=="W":
            dx, dy = 0, -1
        elif direction=="S":
            dx , dy = 0, 1
        elif direction=="A":
            dx , dy = -1, 0
        elif direction=="D":
            dx , dy = 1, 0
        else:
            dx, dy = 0 , 0


        [next_px,next_py] = self.player.calc_next(dx,dy)

        if not self.in_map(next_px,next_py,self.width,self.height):
            print("Go away!!!")
        else:
            if next_px == self.box.x and next_py == self.box.y:
                [next_bx, next_by]=self.box.calc_next(dx,dy)
                if self.in_map(next_bx,next_by,self.width,self.height):
                    self.move_player(dx,dy)
                    self.move_box(dx,dy)
            else:
                self.move_player(dx,dy)

    def loop(self):
        while True:
            move = input("What your move? (A, D, W, S)")
            self.process_input(move)
            self.print()
            if self.win():
                print("YOU WIN!!!")
                break

map = Map(5,5)
map.print()
map.loop()
