import os
import random


def generate(numbers_list=[], counter=29):
    if 0 < counter:
        number = random.randint(0, BOARD_HEIGHT-1)
        number2 = random.randint(0, BOARD_HEIGHT-1)

        if [number, number2] in numbers_list:
            generate(numbers_list, counter-1)

        else:
            numbers_list.append([number, number2])

        generate(numbers_list, counter-1)

    return numbers_list


BOARD_WIDTH = 15
BOARD_HEIGHT = 15


class Empty:
    empty = '·'


class BaseFigure:
    x: int
    y: int
    code: str
    img: str

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.img


class Point(BaseFigure):
    img = '+'
    code = 'e'

    def get_moves(self, board):
        raise ValueError


class Obstacle(BaseFigure):
    img = '-'
    code = 'o'

    def get_moves(self, board):
        raise ValueError


class Hero(BaseFigure):
    img = '•'
    code = 'h'

    def get_moves(self, board):
        moves = []
        board = board.board

        if self.x > 0:
            if board[self.x - 1][self.y] != Empty.empty:
                if board[self.x - 1][self.y].code != Obstacle.code:
                    moves.append([self.x - 1, self.y])

            else:
                moves.append([self.x - 1, self.y])

        if self.x < BOARD_HEIGHT - 1:
            if board[self.x + 1][self.y] != Empty.empty:
                if board[self.x + 1][self.y].code != Obstacle.code:
                    moves.append([self.x + 1, self.y])

            else:
                moves.append([self.x + 1, self.y])

        if self.y > 0:
            if board[self.x][self.y - 1] != Empty.empty:
                if board[self.x][self.y - 1].code != Obstacle.code:
                    moves.append([self.x, self.y - 1])

            else:
                moves.append([self.x, self.y - 1])

        if self.y < BOARD_WIDTH - 1:
            if board[self.x][self.y + 1] != Empty.empty:
                if board[self.x][self.y + 1].code != Obstacle.code:
                    moves.append([self.x, self.y + 1])

            else:
                moves.append([self.x, self.y + 1])

        return moves


class Board:
    def __init__(self):
        self.board = [[Empty.empty for i in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]

    def is_win(self):
        for i in self.board:
            for y in i:
                if y != Empty.empty:
                    if y.code == Point.code:
                        return False

        return True

    def put_figure(self, figure_obj):
        x = figure_obj.x
        y = figure_obj.y

        if self.board[x][y] != Empty.empty:
            raise ValueError

        self.board[x][y] = figure_obj

    def move(self, figure_obj, new_position):
        old_x = figure_obj.x
        old_y = figure_obj.y

        if new_position in figure_obj.get_moves(self):
            self.board[new_position[0]][new_position[1]] = figure_obj
            self.board[old_x][old_y] = Empty.empty
            figure_obj.x = new_position[0]
            figure_obj.y = new_position[1]

        else:
            raise ValueError('This figure hasn\'t this move!!!')

    def __str__(self):
        board_str = ''

        for i in self.board:
            board_str += '| ' + ' '.join(map(lambda x: x+' |', map(str, i))) + '\n'

        return board_str


board = Board()
x = generate()
my_hero = Hero(x[0][0], x[0][1])
point_hero1 = Point(x[1][0], x[1][1])
point_hero2 = Point(x[2][0], x[2][1])
point_hero3 = Point(x[3][0], x[3][1])
point_hero4 = Point(x[4][0], x[4][1])
point_hero5 = Point(x[5][0], x[5][1])
point_hero6 = Point(x[6][0], x[6][1])
point_hero7 = Point(x[7][0], x[7][1])
point_hero8 = Point(x[8][0], x[8][1])
point_hero9 = Point(x[9][0], x[9][1])
point_hero10 = Point(x[10][0], x[10][1])
obstacle1 = Obstacle(x[11][0], x[11][1])
obstacle2 = Obstacle(x[12][0], x[12][1])
obstacle3 = Obstacle(x[13][0], x[13][1])
obstacle4 = Obstacle(x[14][0], x[14][1])
obstacle5 = Obstacle(x[15][0], x[15][1])
obstacle6 = Obstacle(x[16][0], x[16][1])
obstacle7 = Obstacle(x[17][0], x[17][1])
obstacle8 = Obstacle(x[18][0], x[18][1])
obstacle9 = Obstacle(x[19][0], x[19][1])
obstacle10 = Obstacle(x[20][0], x[20][1])
obstacle11 = Obstacle(x[21][0], x[21][1])
obstacle12 = Obstacle(x[22][0], x[22][1])
obstacle13 = Obstacle(x[23][0], x[23][1])
obstacle14 = Obstacle(x[24][0], x[24][1])
obstacle15 = Obstacle(x[25][0], x[25][1])
obstacle16 = Obstacle(x[26][0], x[26][1])
obstacle17 = Obstacle(x[27][0], x[27][1])
obstacle18 = Obstacle(x[28][0], x[28][1])

board.put_figure(my_hero)
board.put_figure(point_hero1)
board.put_figure(point_hero2)
board.put_figure(point_hero3)
board.put_figure(point_hero4)
board.put_figure(point_hero5)
board.put_figure(point_hero6)
board.put_figure(point_hero7)
board.put_figure(point_hero8)
board.put_figure(point_hero9)
board.put_figure(point_hero10)
board.put_figure(obstacle1)
board.put_figure(obstacle2)
board.put_figure(obstacle3)
board.put_figure(obstacle4)
board.put_figure(obstacle5)
board.put_figure(obstacle6)
board.put_figure(obstacle7)
board.put_figure(obstacle8)
board.put_figure(obstacle9)
board.put_figure(obstacle10)
board.put_figure(obstacle11)
board.put_figure(obstacle12)
board.put_figure(obstacle13)
board.put_figure(obstacle15)
board.put_figure(obstacle16)
board.put_figure(obstacle17)
board.put_figure(obstacle18)
print(board)


while True:
    move = input().lower()

    try:
        if move == 'w':
            board.move(my_hero, [my_hero.x - 1, my_hero.y])

        elif move == 'a':
            board.move(my_hero, [my_hero.x, my_hero.y - 1])

        elif move == 's':
            board.move(my_hero, [my_hero.x + 1, my_hero.y])

        elif move == 'd':
            board.move(my_hero, [my_hero.x, my_hero.y + 1])

    except ValueError:
        pass

    os.system('clear')
    print(board)

    if board.is_win():
        print('You won!')
        break
