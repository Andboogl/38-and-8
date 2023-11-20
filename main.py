import os


BOARD_WIDTH = 15
BOARD_HEIGHT = 15


class Empty:
    empty = '.'


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
my_hero = Hero(0, 0)
point_hero1 = Point(7, 7)
point_hero2 = Point(5, 1)
point_hero3 = Point(8, 9)
point_hero4 = Point(11, 1)
point_hero5 = Point(12, 12)
point_hero6 = Point(14, 7)
point_hero7 = Point(14, 8)
point_hero8 = Point(14, 9)
point_hero9 = Point(14, 10)
point_hero10 = Point(9, 7)
obstacle1 = Obstacle(3, 4)
obstacle2 = Obstacle(2, 4)
obstacle3 = Obstacle(1, 4)
obstacle4 = Obstacle(0, 7)
obstacle5 = Obstacle(6, 3)
obstacle6 = Obstacle(5, 6)
obstacle7 = Obstacle(2, 5)
obstacle8 = Obstacle(5, 7)
obstacle9 = Obstacle(5, 2)
obstacle10 = Obstacle(10, 4)
obstacle11 = Obstacle(14, 4)
obstacle12 = Obstacle(12, 8)
obstacle13 = Obstacle(0, 1)
obstacle14 = Obstacle(6, 3)
obstacle15 = Obstacle(7, 2)
obstacle16 = Obstacle(8, 4)
obstacle17 = Obstacle(9, 9)
obstacle18 = Obstacle(3, 5)

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

        else:
            print('Uknown command')

    except ValueError:
        pass

    os.system('clear')
    print(board)

    if board.is_win():
        print('You won!')
        break
