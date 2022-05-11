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
        self.super_shoot = 0

    def create_fleet(self):
        for i in range(1, 5, 1):
            for j in range(5 - i, 0, -1):
                self.field.show()
                coordinates = self.interface.get_coordinates(i) 
                self.field.add_ship(coordinates)
    
    def shoot(self, enemy):
        hit = True
        shoot_counter = 0
        while hit:
            if shoot_counter >= 3:
                self.interface.print_situation(self.field.get(),
                    enemy.field.get(True), 0)
                coordinates = self.interface.ask_for_superpower()
                if coordinates != '-1':
                    if coordinates.isupper():
                        for i in range(10):
                            enemy.field.result_of_shoot(coordinates + str(i))
                    else:
                        for i in range(10):
                            enemy.field.result_of_shoot(('A' + i) + coordinates)
                    hit = False
                    continue

            coordinates = self.interface.print_situation(self.field.get(),
                    enemy.field.get(True))
            result = enemy.field.result_of_shoot(coordinates)
            if result == 'hit':
                shoot_counter += 1
            if result == 'destruction':
                shoot_counter += 1
                self.score += 1
                if self.score == 10:
                    self.win = True
                    return
            if result == 'no hit':
                hit = False

