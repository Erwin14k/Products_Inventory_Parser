from Instruction import Instruction
class Instruction_DAO:
    def __init__(self):
        self.instructions_list = []


    #Función para crear nuevos Errores
    def new_instruction(self,what_should_I_do):
        new = Instruction(what_should_I_do)
        self.instructions_list.append(new)
        return True

    def print_instructions(self):
        for instruction in self.instructions_list:
            print(instruction.what_should_I_do)

