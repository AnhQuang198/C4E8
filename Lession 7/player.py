class Player:
    def __init__(self, x, y): #khoitao constructor
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def move_to(self,x ,y ):
        self.x = x
        self.y = y
    def calc_next(self, dx, dy):
        # self.next_x = dx + self.x
        # self.next_y = dy + self.y
        return [self.x + dx, self.y + dy]