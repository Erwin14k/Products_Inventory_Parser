class Register_DAO:
    def __init__(self):
        self.registers_list = []


    #Función para crear nuevos Errores
    def new_register(self,attributes):
        new = attributes
        self.registers_list.append(new)
        return True

    def print_registers(self):
        for register in self.registers_list:
            print(register)