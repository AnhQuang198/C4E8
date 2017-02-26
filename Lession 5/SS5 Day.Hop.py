px = 2
py = 3
bx = 2
by = 2
ax = 1
ay = 2
zx = 1
zy = 3

screen_width = 5
screen_height = 5

def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def move(x, y, dx, dy):
    return [x + dx,y + dy]

def win(ax, ay, bx, by):
    if (ax == bx and ay == by):
        print("YOU WIN!!!")
        return True
    return False

def box(bx , by, px, py):
    if (bx == px and by == py):
        return True
    return False

while not (win(ax, ay, bx, by)):
    for y in range(screen_height):
        for x in range(screen_width):
            if (x == px and y == py):
                print("P", end=" ")
            elif (x == bx and y == by):
                print("B", end=" ")
            elif (x == ax and y == ay):
                print("*", end=" ")
            else:
                print("-", end=" ")
        print()

    choice = input("What do you want?(W-A-S-D)").upper()
    dx = 0
    dy = 0
    if choice == "W":
        dy = -1
    elif choice == "S":
        dy = 1
    elif choice == "A":
        dx = -1
    elif choice == "D":
        dx = 1

    [next_px, next_py] = move(px, py, dx, dy)
    if box(bx, by, next_px, next_py):
        [next_bx, next_by] = move(bx, by, dx, dy)
        if not in_map(next_bx, next_by, screen_width, screen_height):
            print("Come Back!!!")
        else:
            py = next_py
            px = next_px
            bx = next_bx
            by = next_by
    else:
        if not in_map(next_px, next_py, screen_width, screen_height):
            print("Go away!!!")
        else:
            px = next_px
            py = next_py

    if ( px == bx and py == by ):
        if ( choice == "W"):
            next_py = py - 1
            by = by - 1
        elif ( choice == "A"):
            next_px = px - 1
            bx = bx - 1
        elif ( choice == "S"):
            next_py = py + 1
            by = by + 1
        elif ( choice == "D"):
            next_px = px + 1
            bx = bx + 1

    if ( bx == 0 and by == 0 ):
        print("YOU LOSE!!!")
        break
    elif ( bx == screen_width - 1 and by == 0 ):
        print("YOU LOSE!!!")
        break
    elif ( bx == 0 and by == screen_height - 1 ):
        print("YOU LOSE!!!")
        break
    elif ( bx == screen_height - 1 and by == screen_width - 1 ):
        print("YOU LOSE!!!")
        break
