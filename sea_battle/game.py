import os
from player import player


class game:                                                                     
                                                                                
    def __init__(self):    
        os.system('clear')
        self.__first_player = player()                                            
        self.__second_player = player()                                           
                                                                                
    def __start_fighting(self):
        while True:
            self.__first_player.shoot(self.__second_player)
            if self.__first_player.win:
                print('first player is a winner!')
                return
            self.__second_player.shoot(self.__first_player)
            if self.__second_player.win:
                print('second player is a winner!')
                return


    def start_game(self):
        input('first player are you ready? (enter "yes") ')
        self.__first_player.create_fleet()
        input(f'{self.__first_player.field.show()}(enter "yes")')
        os.system('clear')
        input('second player are you ready? (enter "yes") ')
        self.__second_player.create_fleet()
        input(f'{self.__second_player.field.show()}(enter "yes")')
        self.__start_fighting()

