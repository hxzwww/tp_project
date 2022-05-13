import os
from field import field
import math
from interface import interface


class player:                                                               
    def __init__(self):
        self.win = False
        self.score = 0                                                      
        self.field = field()
        self.interface = interface()

    def create_fleet(self):
        for i in range(1, 5, 1):
            for j in range(5 - i, 0, -1):
                self.field.show()
                coordinates = self.interface.get_coordinates(i) 
                self.field.add_ship(coordinates)
    
    def shoot(self, enemy):
        hit = True
        while hit:
            coordinates = self.interface.print_situation(self.field.get(),
                    enemy.field.get(True))
            result = enemy.field.result_of_shoot(coordinates)
            if result == 'destruction':
                self.score += 1
                if self.score == 10:
                    self.win = True
                    return
            if result == 'no hit':
                hit = False

