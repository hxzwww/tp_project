import os
from field import field
import math


class player:                                                               
    def __init__(self):
        self.win = False
        self.__score = 0                                                      
        self.field = field()

    def __check_ship_correctness(self, coordinates, len):
        x1 = ord(coordinates[0][0]) - ord('A')
        y1 = int(coordinates[0][1])
        x2 = ord(coordinates[1][0]) - ord('A')
        y2 = int(coordinates[1][1])
        
        if (abs(x1 - x2) + abs(y1 - y2) + 1 != len) or (
                abs(x1 - x2) * abs(y1 - y2) != 0):
            return False
        return True

    def create_fleet(self):
        for i in range(1, 5, 1):
            for j in range(5 - i, 0, -1):
                os.system('clear')
                print(self.field.show())
                print(f'Enter your {i}-deck ship coordinates:\n')
                coordinates = []
                if i != 1:
                    coordinates.append(input('from: '))
                    coordinates.append(input('to: '))
                    while not self.__check_ship_correctness(coordinates, i):
                        print('try again!')
                        coordinates = []
                        coordinates.append(input('from: '))
                        coordinates.append(input('to: '))
                else:
                    coordinates.append(input('coordinates: '))
                    
                self.field.add_ship(coordinates)
    
    def shoot(self, enemy):
        hit = True
        while hit:
            coordinates = input(
                    f"""your field:\n\n{self.field.show()}\nyour enemy's field:\n\n{
                    enemy.field.show(True)}\nchoose the cell to shoot: """)
            result = enemy.field.result_of_shoot(coordinates)
            if result == 'destruction':
                self.__score += 1
                if self.__score == 10:
                    self.win = True
                    return
            if result == 'no hit':
                hit = False

