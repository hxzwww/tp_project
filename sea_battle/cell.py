class cell:                                                         
    def __init__(self, status = 'empty'):                           
        self.__cell_status = status                                   
                                                                    
    def set_cell_status(self, new_status):                         
        self.__cell_status = new_status

    def set_cell_status(self):
        return self.__cell_status
