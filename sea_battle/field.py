import os
from cell import cell


class field:
    def __init__(self):
        self.__marine_space = [
                [cell() for i in range(10)] for i in range(10)]
        self.__showing_translator = {'empty' : '⸱', 'shooted' : 'o',              
                'ship' : '▣','shooted ship' : '✖'}
        self.__hiding_translator = {'empty' : '⸱', 'shooted' : 'o',
                'ship' : '⸱','shooted ship' : '✖'}

    def show(self, __hiding = False):
        translator = (self.__hiding_translator if __hiding 
                else self.__showing_translator)
        os.system('clear')
        cur_situation = "  A B C D E F G H I J\n"
        for i in range(10):
            cur_situation += str(i) + ' '
            for j in range(10):
                cur_situation += translator[
                        self.__marine_space[i][j].cell_status] + ' '
            cur_situation += '\n'
        return cur_situation

    def add_ship(self, coordinates):
        x1 = ord(coordinates[0][0]) - ord('A')
        y1 = int(coordinates[0][1])
        if len(coordinates) == 1:
            self.__marine_space[y1][x1].set_cell_status('ship')
            return
        x2 = ord(coordinates[1][0]) - ord('A')
        y2 = int(coordinates[1][1])

        for j in range(min(x1,x2), max(x1, x2) + 1):
            for i in range(min(y1,y2), max(y1, y2) + 1):
                self.__marine_space[i][j].set_cell_status('ship')

    def __check_for_destruction(self, x, y):
        for i in range(x + 1, 10, 1):
            if self.__marine_space[i][y].cell_status == 'ship':
                return 'hit'
            if (self.__marine_space[i][y].cell_status == 'empty'
                    or self.__marine_space[i][y].cell_status == 'shooted'):
                break
        for i in range(x - 1, -1, -1):
            if self.__marine_space[i][y].get_cell_status() == 'ship':
                return 'hit'
            if (self.__marine_space[i][y].get_cell_status() == 'empty'
                    or self.__marine_space[i][y].get_cell_status() == 
                    'shooted'):
                break
        for i in range(y + 1, 10, 1):
            if self.__marine_space[x][i].get_cell_status() == 'ship':
                return 'hit'
            if (self.__marine_space[x][i].get_cell_status() == 'empty'
                    or self.__marine_space[x][i].get_cell_status() == 'shooted'):
                break
        for i in range(y - 1, -1, -1):
            if self.__marine_space[x][i].get_cell_status() == 'ship':
                return 'hit'
            if (self.__marine_space[x][i].get_cell_status() == 'empty'
                    or self.__marine_space[x][i].get_cell_status() == 'shooted'):
                break
        return 'destruction'



    def __shoot(self, x, y):
        if (self.__marine_space[x][y].get_cell_status() == 'empty'):
            self.__marine_space[x][y].set_cell_status('shooted')
            return 'no hit'
        if (self.__marine_space[x][y].get_cell_status() == 'ship'):
            self.__marine_space[x][y].set_cell_status('shooted ship')
            return self.__check_for_destruction(x, y)
        if (self.__marine_space[x][y].get_cell_status().split()[0] == 'shooted'):
            return 'hit'

    def result_of_shoot(self, coordinates):
        y = ord(coordinates[0]) - ord('A')
        x = int(coordinates[1])
        return self.__shoot(x,y)
