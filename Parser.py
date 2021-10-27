
from Instructions import *
from Lexical_Analyzer import error_handler
from Expressions import *


class Parser:
    
    def __init__(self):
        self.errors_list = []
        self.tokens_list = []
        self.i = 0


    #Función que ejecuta el analizador sintáctico
    def analyze(self, tokens_list):
        print()
        self.i = 0
        self.tokens_list = tokens_list
        tree=self.beggining()
        tree.do_it({})
        print()
        tree.get_nodes()
    #Función que le da inicio a la gramática
    def beggining(self):
        list=self.instructions_list()
        return Beggining_Instruction(list)
    #Función para epsilon
    def epsilon(self):
        return Epsilon_Instruction()


    #Se define la lista de instrucciones
    def instructions_list(self):
        instruction=self.instruction()
        list=self.instructions_list_2()
        return Instructions_List(instruction,list)
        


    #Función recursiva de instrucciones
    def instructions_list_2(self):
        if self.tokens_list[self.i].type == 'EOF':
            print('Analisis sintactico exitoso')
            print('RETORNANDO EPSILON')
            instruction = self.epsilon()
            return Instructions_List_2(instruction, [])
        else:
            instruction = self.instruction()
            list = self.instructions_list_2()
            return Instructions_List_2(instruction, list)

    #Función que valida que instrucción viene en camino
    def instruction(self):
        #print("hello")
        if self.tokens_list[self.i].type == 'Register' :
            #print(self.tokens_list[self.i].type)
            instruction=self.registers_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'CLAVES' :
            #print(self.tokens_list[self.i].type)
            instruction=self.keys_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'max' :
            #print(self.tokens_list[self.i].type)
            instruction=self.max_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'min' :
            #print(self.tokens_list[self.i].type)
            instruction=self.min_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'data' :
            #print(self.tokens_list[self.i].type)
            instruction=self.data_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'print' :
            #print(self.tokens_list[self.i].type)
            instruction=self.print_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'println' :
            #print(self.tokens_list[self.i].type)
            instruction=self.println_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'count' :
            #print(self.tokens_list[self.i].type)
            instruction=self.count_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'average' :
            #print(self.tokens_list[self.i].type)
            instruction=self.average_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'count_if' :
            #print(self.tokens_list[self.i].type)
            instruction=self.count_if_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'sum' :
            #print(self.tokens_list[self.i].type)
            instruction=self.sum_ins()
            return Instruction_Instruction(instruction)
        elif self.tokens_list[self.i].type == 'report' :
            #print(self.tokens_list[self.i].type)
            instruction=self.export_ins()
            return Instruction_Instruction(instruction)


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción registros
    def registers_ins(self):
        print("hello")
        if self.tokens_list[self.i].type == 'Register' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'equals' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'open_square_bracket' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    list=self.registers_list()
                    if self.tokens_list[self.i].type == 'closed_square_bracket' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        return Register_Instruction(list)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un closed_square_bracket, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un open_square_bracket, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un equals, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    def registers_list(self):
        instruction=self.register()
        list=self.registers_list_2()
        return Register_List(instruction, list)
    def registers_list_2(self):
        if self.tokens_list[self.i].type == 'closed_square_bracket' :
            pass
        else:
            instruction=self.register()
            list=self.registers_list_2()
            return Register_List_2(instruction, list)
    def register(self):
        if self.tokens_list[self.i].type == 'open_key' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            self.attributes_list()
            if self.tokens_list[self.i].type == 'closed_key' :
                print(self.tokens_list[self.i].type)
                self.i += 1
    def attributes_list(self):
        self.attribute()
        self.attributes_list_2()
    def attributes_list_2(self):
        if self.tokens_list[self.i].type == 'closed_key' :
            pass
        elif self.tokens_list[self.i].type == 'comma' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            self.attribute()
            self.attributes_list_2()
    def attribute(self):
        if self.tokens_list[self.i].type == 'double_quotation_mark' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'string_value':
                print(self.tokens_list[self.i].type)
                lexem=self.tokens_list[self.i].lexem
                lexem=lexem.replace("\\","")
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark':
                    print(self.tokens_list[self.i].type)
                    expression= Literal_Expression("string_value",lexem)
                    self.i += 1
                    return expression
        elif self.tokens_list[self.i].type == 'int_value' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            expression= Literal_Expression("int_value",lexem)
            self.i+= 1
            return expression
        elif self.tokens_list[self.i].type == 'float_value' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            expression= Literal_Expression("float_value",lexem)
            self.i+= 1
            return expression
        elif self.tokens_list[self.i].type == 'parameter' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            expression= Literal_Expression("parameter",lexem)
            self.i+= 1
            return expression
        elif self.tokens_list[self.i].type == 'int_parameter' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            expression= Literal_Expression("int_parameter",lexem)
            self.i+= 1
            return expression
        elif self.tokens_list[self.i].type == 'message' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            lexem=lexem.replace("\\","")
            expression= Literal_Expression("message",lexem)
            self.i+= 1
            return expression
        elif self.tokens_list[self.i].type == 'title' :
            print(self.tokens_list[self.i].type)
            lexem=self.tokens_list[self.i].lexem
            lexem=lexem.replace("\\","")
            expression= Literal_Expression("title",lexem)
            self.i+= 1
            return expression
        else:
            line = self.tokens_list[self.i].line
            column = self.tokens_list[self.i].column
            error_handler.new_error('Se esperaba un valor: String|float|int, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            pass
        #else:
        #print("no encontró nada") 
        #pass
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================







    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción max
    def max_ins(self):
        if self.tokens_list[self.i].type == 'max' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Max_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opnes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        
                        
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================




    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción min
    def min_ins(self):
        if self.tokens_list[self.i].type == 'min' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Min_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opnes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================



    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción datos
    def data_ins(self):
        if self.tokens_list[self.i].type == 'data' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    if self.tokens_list[self.i].type == 'semicolon' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        return Data_Instruction()
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción claves
    def keys_ins(self):
        if self.tokens_list[self.i].type == 'CLAVES' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'equals' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'open_square_bracket' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    list=self.keys_list()
                    if self.tokens_list[self.i].type == 'closed_square_bracket' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        print("se terminaron las claves!")
                        return Keys_Instruction(list)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un closed_square_bracket, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un open_square_bracket, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un equals, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    '''def key(self):
        #if self.tokens_list[self.i].type == 'double_quotation_mark' :
            #self.i += 1
        if self.tokens_list[self.i].type == 'Clave' :
            print(self.tokens_list[self.i].type)
            type=lexem=self.tokens_list[self.i].lexem
            lexem=self.tokens_list[self.i].lexem
            self.i += 1
            if self.tokens_list[self.i].type == 'double_quotation_mark' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                list=self.keys_list_2()
                #expression=Key_Expression(type,lexem)
                return Keys_Instruction(list)'''
    def key(self):
        if self.tokens_list[self.i].type == 'double_quotation_mark' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'Clave' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1

    def keys_list(self):
        key = self.key()
        list = self.keys_list_2()
        return Keys_List(key, list)


    def keys_list_2(self):
        if self.tokens_list[self.i].type == 'closed_square_bracket' :
            pass
        else:
            if self.tokens_list[self.i].type == 'comma' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                key=self.key()
                list=self.keys_list_2()
                return Keys_List_2(key, list)
    '''def keys_list_2(self):
        if self.tokens_list[self.i].type == 'closed_square_bracket' :
            pass
        else:
            if self.tokens_list[self.i].type == 'comma' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    if self.tokens_list[self.i].type == 'Clave' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            list=self.keys_list_2()
                            return Keys_List_2("Clave",list)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba una Clave, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba una coma, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)'''
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================



    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción imprimir
    def print_ins(self):
        if self.tokens_list[self.i].type == 'print' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Print_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================




    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción imprimirln
    def println_ins(self):
        if self.tokens_list[self.i].type == 'println' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Println_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción conteo
    def count_ins(self):
        if self.tokens_list[self.i].type == 'count' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    if self.tokens_list[self.i].type == 'semicolon' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        return Count_Instruction()
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================



    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción promedio
    def average_ins(self):
        if self.tokens_list[self.i].type == 'average' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Average_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción contarsi
    def count_if_ins(self):
        if self.tokens_list[self.i].type == 'count_if' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'comma' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            expression2=self.attribute()
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
                                    return Countif_Instruction(expression,expression2)
                                else:
                                    line = self.tokens_list[self.i].line
                                    column = self.tokens_list[self.i].column
                                    error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba una comma, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================



    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción sumar
    def sum_ins(self):
        if self.tokens_list[self.i].type == 'sum' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Sum_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                                
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción exportar
    def export_ins(self):
        if self.tokens_list[self.i].type == 'report' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'parenthesis_that_opens' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    expression=self.attribute()
                    if self.tokens_list[self.i].type == 'double_quotation_mark' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'semicolon' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                return Export_Instruction(expression)
                            else:
                                line = self.tokens_list[self.i].line
                                column = self.tokens_list[self.i].column
                                error_handler.new_error('Se esperaba un semicolon, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                        else:
                            line = self.tokens_list[self.i].line
                            column = self.tokens_list[self.i].column
                            error_handler.new_error('Se esperaba un parenthesis_that_closes, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                    else:
                        line = self.tokens_list[self.i].line
                        column = self.tokens_list[self.i].column
                        error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
                else:
                    line = self.tokens_list[self.i].line
                    column = self.tokens_list[self.i].column
                    error_handler.new_error('Se esperaba un double_quotation_mark, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
            else:
                line = self.tokens_list[self.i].line
                column = self.tokens_list[self.i].column
                error_handler.new_error('Se esperaba un parenthesis_that_opens, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================





    



    '''def impErrores(self):
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                i.imprimirData()'''