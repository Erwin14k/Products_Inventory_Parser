from Lexical_Analyzer import token_handler
from Lexical_Analyzer import error_handler

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
        self.beggining()
        print()
    #Función que le da inicio a la gramática
    def beggining(self):
        self.instructions_list()


    #Se define la lista de instrucciones
    def instructions_list(self):
        #print(self.tokens_list)
        if self.tokens_list[self.i].type == 'Register' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'CLAVES' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'max' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'min' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'data' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'print' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'println' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'count' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'average' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'count_if' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'sum' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'report' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        else:
            line = self.tokens_list[self.i].line
            column = self.tokens_list[self.i].column
            error_handler.new_error('Se esperaba un tipo de instrucción, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)


    #Función recursiva de instrucciones
    def instructions_list_2(self):
        if self.tokens_list[self.i].type == 'Register' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'CLAVES' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'max' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'min' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'data' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'print' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'println' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'count' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'average' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'count_if' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'sum' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'report' :
            #print(self.tokens_list[self.i].type)
            self.instruction()
            self.instructions_list_2()
        elif self.tokens_list[self.i].type == 'EOF' :
            print(self.tokens_list[self.i].type)
            print('analisis sintactico exitoso')
        else:
            line = self.tokens_list[self.i].line
            column = self.tokens_list[self.i].column
            error_handler.new_error('Se esperaba un tipo de instrucción, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)

    #Función que valida que instrucción viene en camino
    def instruction(self):
        if self.tokens_list[self.i].type == 'Register' :
            #print(self.tokens_list[self.i].type)
            self.registers_ins()
        elif self.tokens_list[self.i].type == 'CLAVES' :
            #print(self.tokens_list[self.i].type)
            self.keys_ins()
        elif self.tokens_list[self.i].type == 'max' :
            #print(self.tokens_list[self.i].type)
            self.max_ins()
        elif self.tokens_list[self.i].type == 'min' :
            #print(self.tokens_list[self.i].type)
            self.min_ins()
        elif self.tokens_list[self.i].type == 'data' :
            #print(self.tokens_list[self.i].type)
            self.data_ins()
        elif self.tokens_list[self.i].type == 'print' :
            #print(self.tokens_list[self.i].type)
            self.print_ins()
        elif self.tokens_list[self.i].type == 'println' :
            #print(self.tokens_list[self.i].type)
            self.println_ins()
        elif self.tokens_list[self.i].type == 'count' :
            #print(self.tokens_list[self.i].type)
            self.count_ins()
        elif self.tokens_list[self.i].type == 'average' :
            #print(self.tokens_list[self.i].type)
            self.average_ins()
        elif self.tokens_list[self.i].type == 'count_if' :
            #print(self.tokens_list[self.i].type)
            self.count_if_ins()
        elif self.tokens_list[self.i].type == 'sum' :
            #print(self.tokens_list[self.i].type)
            self.sum_ins()
        elif self.tokens_list[self.i].type == 'report' :
            #print(self.tokens_list[self.i].type)
            self.export_ins()


    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #====================================================================================================
    #Todo lo relacionado a la instrucción registros
    def registers_ins(self):
        if self.tokens_list[self.i].type == 'Register' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'equals' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'open_square_bracket' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    self.registers_list()
                    if self.tokens_list[self.i].type == 'closed_square_bracket' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
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
        self.register()
        self.registers_list_2()
    def registers_list_2(self):
        if self.tokens_list[self.i].type == 'closed_square_bracket' :
            pass
        else:
            self.register()
            self.registers_list_2()
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
        if self.tokens_list[self.i].type == 'string_value' :
            print(self.tokens_list[self.i].type)
            self.i+= 1
        elif self.tokens_list[self.i].type == 'int_value' :
            print(self.tokens_list[self.i].type)
            self.i += 1
        elif self.tokens_list[self.i].type == 'float_value' :
            print(self.tokens_list[self.i].type)
            self.i += 1
        elif self.tokens_list[self.i].type == 'double_quotation_mark' :
            print(self.tokens_list[self.i].type)
            self.i += 1
            if self.tokens_list[self.i].type == 'string_value':
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark':
                    print(self.tokens_list[self.i].type)
                    self.i += 1
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
                    if self.tokens_list[self.i].type == 'parameter' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'parameter' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    self.keys_list()
                    if self.tokens_list[self.i].type == 'closed_square_bracket' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
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

    def keys_list(self):
        if self.tokens_list[self.i].type == 'double_quotation_mark' :
            self.i += 1
            if self.tokens_list[self.i].type == 'Clave' :
                print(self.tokens_list[self.i].type)
                self.i += 1
                if self.tokens_list[self.i].type == 'double_quotation_mark' :
                    print(self.tokens_list[self.i].type)
                    self.i += 1
                    self.keys_list_2()
    def keys_list_2(self):
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
                            self.keys_list_2()
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
                error_handler.new_error('Se esperaba una coma, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'message' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un message, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'message' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un message, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'parameter' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'parameter' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'comma' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'int_parameter' or self.tokens_list[self.i].type == 'float_parameter' or self.tokens_list[self.i].type == 'string_parameter':
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
                                    if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                        print(self.tokens_list[self.i].type)
                                        self.i += 1
                                        if self.tokens_list[self.i].type == 'semicolon' :
                                            print(self.tokens_list[self.i].type)
                                            self.i += 1
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
                                    error_handler.new_error('Se esperaba un string|float|int parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                        error_handler.new_error('Se esperaba un parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'parameter' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un parameter, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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
                    if self.tokens_list[self.i].type == 'title' :
                        print(self.tokens_list[self.i].type)
                        self.i += 1
                        if self.tokens_list[self.i].type == 'double_quotation_mark' :
                            print(self.tokens_list[self.i].type)
                            self.i += 1
                            if self.tokens_list[self.i].type == 'parenthesis_that_closes' :
                                print(self.tokens_list[self.i].type)
                                self.i += 1
                                if self.tokens_list[self.i].type == 'semicolon' :
                                    print(self.tokens_list[self.i].type)
                                    self.i += 1
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
                        error_handler.new_error('Se esperaba un tittle, en su lugar se obtuvo: '+self.tokens_list[self.i].type,'sintactico', line, column)
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