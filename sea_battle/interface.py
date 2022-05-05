import os


class interface:
    
    def __init__(self):
        pass

    def print_winner(self, n):
        if n == 1:
            print('first player is a winner!')
        if n == 2:
            print('second player is a winner!')

    def ask_for_ready(self, n):
        if n == 1:
            input('first player are you ready? (enter "yes") ')
        if n == 2:
            input('second player are you ready? (enter "yes") ')

    def show_field(self, field, txt):
        print(field)
        if txt != "":
            input(txt)
            os.system('clear')

    def check_ship_correctness(self, coordinates, len):                         
        x1 = ord(coordinates[0][0]) - ord('A')                                  
        y1 = int(coordinates[0][1])                                             
        x2 = ord(coordinates[1][0]) - ord('A')                                  
        y2 = int(coordinates[1][1])                                             
        if (abs(x1 - x2) + abs(y1 - y2) + 1 != len) or (                        
                abs(x1 - x2) * abs(y1 - y2) != 0):                              
            return False                                                        
        return True 

    def get_coordinates(self, i):
        print(f'Enter your {i}-deck ship coordinates:\n')
        coordinates = []
        if i != 1:
            coordinates.append(input('from: '))
            coordinates.append(input('to: '))
            while not self.check_ship_correctness(coordinates, i):
                print('try again!')
                coordinates = []
                coordinates.append(input('from: '))
                coordinates.append(input('to: '))
        else:
            coordinates.append(input('coordinates: '))
        return coordinates

    def print_situation(self, first, enemy):
        coordinates = input(
            f"""your field:\n\n{first}\nyour enemy's field:\n\n{
            enemy}\nchoose the cell to shoot: """)
        return coordinates
