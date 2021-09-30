from Error import  Error
class Error_DAO:
    def __init__(self):
        self.errors_list = []


    #Función para crear nuevos Errores
    def new_error(self,description, type, line, column):
        new = Error(description, type, line, column)
        self.errors_list.append(new)
        return True

    def print_error(self):
        for error in self.errors_list:
            print(error.description,error.type,str(error.line),str(error.column))