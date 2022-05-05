import os
from player import player
from interface import interface

class game:                                                                     
                                                                                
    def __init__(self):    
        os.system('clear')
        self.first_player = player()                                            
        self.second_player = player()
        self.interface = interface()
                                                                                
    def start_fighting(self):
        while True:
            self.first_player.shoot(self.second_player)
            if self.first_player.win:
                self.interface.print_winner(1)
                return
            self.second_player.shoot(self.first_player)
            if self.second_player.win:
                self.interface.print_winner(2)
                return


    def start_game(self):
        self.interface.ask_for_ready(1)
        self.first_player.create_fleet()
        self.first_player.field.show('enter "yes"')
        self.interface.ask_for_ready(2)
        self.second_player.create_fleet()
        self.second_player.field.show('enter "yes"')
        self.start_fighting()

