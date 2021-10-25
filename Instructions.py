from Expressions import *


class Print_Instruction() :
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        value = self.expression.get_value(environment)
        print(value)
class Println_Instruction() :
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        value = self.expression.get_value(environment)
        print(value)

class Instruction_Instruction() :
    def __init__(self, instruction) :
        self.instruction = instruction

    def do_it(self, environment):
        self.instruction.do_it(environment)

class Instructions_List_2() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        if self.instruction:
            self.instruction.do_it(environment)
            if self.list:
                self.list.do_it(environment)

class Instructions_List() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        if self.instruction:
            self.instruction.do_it(environment)
            if self.list:
                self.list.do_it(environment)

class Beggining_Instruction() :
    def __init__(self,list) :
        self.list = list

    def do_it(self, environment):
        self.list.do_it(environment)