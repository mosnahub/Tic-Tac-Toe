xo = []
coord_input = []
turn = 1


def write_cell():
    index = 0
    for i in range(3):
        xo.append([])
        for j in range(3):
            xo[i].append(" ")
            index += 1


def print_table():
    print("---------")
    for i in range(3):
        print(f"| {xo[i][0]} {xo[i][1]} {xo[i][2]} |")
    print("---------")


def get_coord():
    global coord_input, turn

    while True:
        coord_input = [i for i in input("Enter the coordinates: ").split()]

        for i in coord_input:
            if not i.isnumeric():
                print("You should enter numbers!")
                break
        else:
            coord_ = [int(j) for j in coord_input]
            x = 3 - coord_[1]
            y = coord_[0] - 1

            if coord_[0] < 1 or coord_[0] > 3 or coord_[1] < 1 or coord_[1] > 3:
                print("Coordinates should be from 1 to 3!")
            elif not is_empty(x, y):
                print("This cell is occupied! Choose another one!")
            else:
                if turn % 2 == 1:
                    xo[x][y] = 'X'
                    turn += 1
                    break
                elif turn % 2 == 0:
                    xo[x][y] = 'O'
                    turn += 1
                    break


def is_empty(x, y):
    if xo[x][y] == ' ':
        return True
    return False


def check(xo):
    no_spaces = 0

    if xo[0][0] == xo[0][1] == xo[0][2] and xo[0][0] != ' ':  # top
        return f"{xo[0][0]} wins"
    elif xo[1][0] == xo[1][1] == xo[1][2] and xo[1][0] != ' ':  # middle
        return f"{xo[1][0]} wins"
    elif xo[2][0] == xo[2][1] == xo[2][2] and xo[2][0] != ' ':  # bottom
        return f"{xo[2][0]} wins"
    elif xo[0][0] == xo[1][0] == xo[2][0] and xo[0][0] != ' ':  # left
        return f"{xo[0][0]} wins"
    elif xo[0][1] == xo[1][1] == xo[2][1] and xo[0][1] != ' ':  # center
        return f"{xo[0][1]} wins"
    elif xo[0][2] == xo[1][2] == xo[2][2] and xo[0][2] != ' ':  # right
        return f"{xo[0][2]} wins"
    elif xo[0][0] == xo[1][1] == xo[2][2] and xo[0][0] != ' ':  # diagonal left to right
        return f"{xo[0][0]} wins"
    elif xo[0][2] == xo[1][1] == xo[2][0] and xo[0][2] != ' ':  # diagonal right to left
        return f"{xo[0][2]} wins"
    for i in xo:
        if ' ' in i:
            pass
        else:
            no_spaces += 1
    if no_spaces == 3:
        return "Draw"


write_cell()

while True:
    print_table()
    get_coord()
    if check(xo) is not None:
        print_table()
        print(check(xo))
        break


