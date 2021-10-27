from enum import IntFlag
from Token_DAO import Token_DAO
from Token import Token
from Error import Error
from Error_DAO import Error_DAO
from Register_DAO import Register_DAO
from Instruction import Instruction
from Instruction_DAO import Instruction_DAO
import re
error_handler=Error_DAO()
token_handler=Token_DAO()
register_handler=Register_DAO()
instruction_handler=Instruction_DAO()

class Lexical_Analyzer:
    def __init__(self):
        self.inventory_data=[]
        self.temporal_register=[]
        self.cols=0
        self.rows=0

#========================================================================================================
#función para la recolección de tokens y erroes léxicos mediante un analizador léxico
    def lexical_analyze_file(self, original_text):
        #inicializar atributos
        line = 1
        column = 1
        buffer = ""
        print_buffer=""
        println_buffer=""
        data_buffer=""
        sentinel = '$'
        count_buffer=""
        average_buffer=""
        max_buffer=""
        min_buffer=""
        export_buffer=""
        count_if_buffer=""
        sum_buffer=""
        state = 0
        original_text += sentinel

        #automata
        i = 0
        while i< len(original_text):
            c = original_text[i]
            #=======================================================================================
            #Estado 0, donde dependiendo lo recolectado ira cambiando de estado
            if state == 0:
                if c == sentinel:
                    buffer+=c
                    token_handler.new_token(buffer, 'EOF', line, column)
                    column+=1
                    buffer=""
                    print('Se aceptó la cadena!')
                    break
                #Si encuentra una letra "C", se irá al estado 1
                elif c=="C":
                    buffer+=c
                    column+=1
                    state = 1
                elif c == 'R':
                    buffer += c
                    column += 1
                    state=5
                elif c == '\n':
                    line += 1
                    column = 1
                elif c == '\t':
                    column += 1
                elif c == ' ':
                    column += 1
                elif c == '\r':
                    pass
                elif c=="#":
                    buffer+=c
                    column+=1
                    state=12
                elif c=="'":
                    buffer+=c
                    column+=1
                    state=15
                elif c=="i":
                    buffer+=c
                    column+=1
                    state=20
                elif c=="c":
                    buffer+=c
                    column+=1
                    state=23
                elif c=="d":
                    buffer+=c
                    column+=1
                    state=24
                elif c=="p":
                    buffer+=c
                    column+=1
                    state=25
                elif c=="e":
                    buffer+=c
                    column+=1
                    state=30
                elif c=="m":
                    buffer+=c
                    column+=1
                    state=27
                elif c=="s":
                    buffer+=c
                    column+=1
                    state=34
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                elif c==")":
                    buffer+=c
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    column+=1
                    buffer=""
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================
            
            
            
            
            #=======================================================================================
            #Estado 1, donde solo acepta letras, por lo tanto si es diferente verifica si se cumple
            # la palabra "Clave" y luego se va al estado 2
            elif state == 1:
                if  c=="l" or c=="a" or c=="v" or c=="e" or c=="s":
                    buffer+=c
                    column += 1
                else:
                    if buffer == 'Claves':
                        token_handler.new_token(buffer, 'CLAVES', line, column)
                    else:
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 2
            #=======================================================================================




            #=======================================================================================
            #Estado 2, donde solo acepta "=" , " " , "["
            elif state == 2:
                if c==" ":
                    buffer += c
                    buffer =""
                    column += 1
                elif c=="=":
                    buffer+=c
                    token_handler.new_token(buffer, 'equals', line, column)
                    column += 1
                    buffer=""
                elif c=="[":
                    buffer+=c
                    token_handler.new_token(buffer, 'open_square_bracket', line, column)
                    column += 1
                    buffer=""
                elif c=="\n":
                    line+=1
                    column=1
                    state=3
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================


            #=======================================================================================
            #Estado 3, solo acepta '"'
            elif state==3:
                if c=='"':
                    buffer += c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    buffer =""
                    state=4
                elif c==" " or c=="\t":
                    column+=1
                elif c=="#":
                    buffer+=c
                    column+=1
                    state=13
                elif c=="'":
                    buffer+=c
                    column+=1
                    state=16
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
                    
            #=======================================================================================


            #=======================================================================================
            #Estado 4, acepta todo lo relacionado a las claves
            elif state==4:
                if re.search('[a-z]', c) or re.search('[A-Z]', c) or c=="_":
                    buffer += c
                    column += 1
                elif c=='"':
                    if len(buffer)>=2:
                        token_handler.new_token(buffer, 'Clave', line, column)
                        self.temporal_register=[*self.temporal_register,buffer]
                        buffer =""
                        column+=1
                        buffer+=c
                        token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                        column+=1
                        buffer=""
                    else:
                        buffer+=c
                        token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                        column+=1
                        buffer=""
                elif c==",":
                    buffer+=c
                    token_handler.new_token(buffer, 'comma', line, column)
                    column+=1
                    buffer=""
                elif c=="\n":
                    line+=1
                    column=1
                elif c=="#":
                    buffer+=c
                    column+=1
                    state=17
                elif c=="'":
                    buffer+=c
                    column+=1
                    state=18
                elif c=="]":
                    buffer+=c
                    token_handler.new_token(buffer, 'closed_square_bracket', line, column)
                    column+=1
                    buffer=""
                    self.cols=len(self.temporal_register)
                    register_handler.new_register(self.temporal_register)
                    self.temporal_register=[]
                    state=0
                elif c==" " or c=="\t":
                    column+=1
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================


            #=======================================================================================
            #Estado 5, acepta la palabra reservada "Registros"
            elif state==5:
                if  c=="e" or c=="g" or c=="i" or c=="s" or c=="t" or c=="r" or c=="o":
                    buffer+=c
                    column += 1
                else:
                    if buffer == 'Registros':
                        #print("si vienen registros")
                        token_handler.new_token(buffer, 'Register', line, column)
                        buffer = ""
                        state = 6
                    else:
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        state = 0
                    
            #=======================================================================================


            #=======================================================================================
            #Estado 6, donde solo acepta "=" , " " , "["
            elif state == 6:
                if c==" ":
                    column += 1
                elif c=="=":
                    buffer+=c
                    token_handler.new_token(buffer, 'equals', line, column)
                    column += 1
                    buffer=""
                elif c=="[":
                    buffer+=c
                    token_handler.new_token(buffer, 'open_square_bracket', line, column)
                    column += 1
                    buffer=""
                    state=7
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================



            #=======================================================================================
            #Estado 7, solo acepta '{'
            elif state==7:
                if c=='{':
                    buffer += c
                    token_handler.new_token(buffer, 'open_key', line, column)
                    column += 1
                    buffer =""
                    state=8
                elif c==" " or c=="\t":
                    column+=1
                elif c=="\n":
                    line+=1
                    column=1
                elif c=="]":
                    buffer+=c
                    token_handler.new_token(buffer,"closed_square_bracket",line,column)
                    column+=1
                    buffer=""
                    state=0
                elif c=="#":
                    buffer+=c
                    column+=1
                    state=14
                elif c=="'":
                    buffer+=c
                    column+=1
                    state=19
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
                    
            #=======================================================================================




            #=======================================================================================
            #Estado 8, acepta todo lo relacionado a los registros
            elif state==8:
                if c=='"':
                    buffer+=c
                    token_handler.new_token(buffer,"double_quotation_mark",line,column)
                    column+=1
                    buffer=""
                    state=9
                elif c==",":
                    buffer+=c
                    token_handler.new_token(buffer, 'comma', line, column)
                    column+=1
                    buffer=""
                elif c=="\n":
                    line+=1
                    column=1
                elif c==" " or c=="\t":
                    column+=1
                elif c=="}":
                    buffer+=c
                    token_handler.new_token(buffer, 'closed_key', line, column)
                    register_handler.new_register(self.temporal_register)
                    buffer=""
                    self.temporal_register=[]
                    state=7
                elif c.isdigit():
                    column+=1
                    buffer+=c
                    state=10
                else:
                    buffer += c
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================



            #=======================================================================================
            #Estado 9, acepta atributo de un registro de tipo string
            elif state==9:
                if c!='"' and c!='\n' and c!="\t":
                    buffer += c
                    column += 1
                elif c=='"':
                    self.temporal_register=[*self.temporal_register,buffer]
                    token_handler.new_token(buffer,"string_value",line,column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer,"double_quotation_mark",line,column)
                    column+=1
                    buffer=""
                    state=8
                elif c=="\n":
                    line+=1
                    column=1
                elif  c=="\t":
                    column+=1
            #=======================================================================================


            #=======================================================================================
            #Estado 10, acepta atributo de un registro de tipo numérico (float/int)
            elif state==10:
                if c.isdigit():
                    buffer += c
                    column += 1
                elif c==".":
                    buffer += c
                    column+=1
                    state=11
                elif c=="," or c==" " :
                    self.temporal_register=[*self.temporal_register,int(buffer)]
                    token_handler.new_token(buffer,"int_value",line,column)
                    buffer=""
                    column+=1
                    buffer+=c
                    token_handler.new_token(buffer,"comma",line,column)
                    buffer=""
                    state=8
                elif c=="}":
                    self.temporal_register=[*self.temporal_register,int(buffer)]
                    token_handler.new_token(buffer,"int_value",line,column)
                    buffer=""
                    column+=1
                    buffer+=c
                    token_handler.new_token(buffer,"closed_key",line,column)
                    buffer=""
                    column+=1
                    register_handler.new_register(self.temporal_register)
                    #print(self.temporal_register)
                    self.temporal_register=[]
                    state=7
                else:
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================


            #=======================================================================================
            #Estado 11, viene de recibir un punto, quiere decir que esperamos un float, por lo que
            #se verifica que lo que venga a continuación sea un digito
            elif state==11:
                if c.isdigit():
                    buffer += c
                    column += 1
                else:
                    if c=="," or c==" ":
                        self.temporal_register=[*self.temporal_register,float(buffer)]
                        token_handler.new_token(buffer,"float_value",line,column)
                        buffer=""
                        column+=1
                        buffer+=c
                        token_handler.new_token(buffer,"comma",line,column)
                        buffer=""
                        state=8
            #=======================================================================================

            #=======================================================================================
            #Estado 12, Este estado recibe comentarios simples, viene de un "#" del estado 0
            elif state==12:
                if c!="\n":
                    buffer += c
                    column += 1
                else:
                    #token_handler.new_token(buffer,"simple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=0
            #=======================================================================================


            #=======================================================================================
            #Estado 13, Este estado recibe comentarios simples, viene de un "#" del estado 3
            elif state==13:
                if c!="\n":
                    buffer += c
                    column += 1
                else:
                    #token_handler.new_token(buffer,"simple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=3
            #=======================================================================================


            #=======================================================================================
            #Estado 14, Este estado recibe comentarios simples, viene de un "#" del estado 7
            elif state==14:
                if c!="\n":
                    buffer += c
                    column += 1
                else:
                    #token_handler.new_token(buffer,"simple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=7
            #=======================================================================================

            #=======================================================================================
            #Estado 15, Este estado recibe comentarios multilinea, viene de un "'" del estado 0
            elif state==15:
                if buffer.count("'")!=6:
                    if c=="'":
                        buffer += c
                        column+=1
                    else:
                        if c!="'" :
                            buffer+=c
                            column+=1
                            if  c=="\n":
                                column=1
                                line+=1
                else:
                    #token_handler.new_token(buffer,"multiple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=0

            #=======================================================================================


            #=======================================================================================
            #Estado 16, Este estado recibe comentarios multilinea, viene de un "'" del estado 3
            elif state==16:
                if buffer.count("'")!=6:
                    if c=="'":
                        buffer += c
                        column+=1
                    else:
                        if c!="'" :
                            buffer+=c
                            column+=1
                            if  c=="\n":
                                column=1
                                line+=1
                else:
                    #token_handler.new_token(buffer,"multiple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=3

            #=======================================================================================


            #=======================================================================================
            #Estado 17, Este estado recibe comentarios multilinea, viene de un "#" del estado 4
            elif state==17:
                if c!="\n":
                    buffer += c
                    column += 1
                else:
                    #token_handler.new_token(buffer,"simple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=4

            #=======================================================================================



            #=======================================================================================
            #Estado 18, Este estado recibe comentarios multilinea, viene de un "'" del estado 4
            elif state==18:
                if buffer.count("'")!=6:
                    if c=="'":
                        buffer += c
                        column+=1
                    else:
                        if c!="'" :
                            buffer+=c
                            column+=1
                            if  c=="\n":
                                column=1
                                line+=1
                else:
                    #token_handler.new_token(buffer,"multiple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=4
            #=======================================================================================

            #=======================================================================================
            #Estado 19, Este estado recibe comentarios multilinea, viene de un "'" del estado 7
            elif state==19:
                if buffer.count("'")!=6:
                    if c=="'":
                        buffer += c
                        column+=1
                    else:
                        if c!="'" :
                            buffer+=c
                            column+=1
                            if  c=="\n":
                                column=1
                                line+=1
                else:
                    #token_handler.new_token(buffer,"multiple_comment",line,column)
                    buffer=""
                    column=1
                    line+=1
                    state=7

            #=======================================================================================

            #=======================================================================================
            #Estado 20, donde solo acepta letras, por lo tanto si es diferente verifica si se cumple
            # un imprimir o un imprimirln
            elif state == 20:
                if  c=="i" or c=="m" or c=="p" or c=="r" or c=="l" or c=="n":
                    buffer+=c
                    column += 1
                else:
                    if buffer == "imprimir" and c=="(":
                        token_handler.new_token(buffer, 'print', line, column)
                        print_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        print_buffer+=c
                        buffer=""
                        state=21
                    elif buffer=="imprimirln":
                        token_handler.new_token(buffer, 'println', line, column)
                        println_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        println_buffer+=c
                        buffer=""
                        state=22
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 21, viene de recibir un imprimir, en este caso se recolecta, que se desea
            #imprimir
            elif state == 21:
                if  c=='"' :
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    print_buffer+=c
                    buffer=""
                    state=36
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    #state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 22, viene de recibir un imprimirln, en este caso se recolecta, que se desea
            #imprimir
            elif state == 22:
                if  c=='"' :
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    println_buffer+=c
                    buffer=""
                    state=37
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    #state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 23, viene de recibir una "c" minúscula en estado 0, por lo que puede indicar la
            # función conteo() o contarsi(parametro,cantidad) en este caso se recolecta y se verifica
            elif state == 23:
                if  c=="o" or c=="n" or c=="t" or c=="e" or c=="c" or c=="a" or c=="r" or c=="s" or c=="i":
                    buffer+=c
                    column += 1
                else:
                    if buffer == "conteo" and c=="(":
                        token_handler.new_token(buffer, 'count', line, column)
                        count_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        count_buffer+=c
                        buffer=""
                        state=32
                    elif buffer=="contarsi" and c=="(":
                        token_handler.new_token(buffer, 'count_if', line, column)
                        count_if_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        count_if_buffer+=c
                        buffer=""
                        state=33
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 24, viene de recibir una "d" minúscula en estado 0, por lo que puede indicar la
            # función datos(), en este caso se recolecta y se verifica
            elif state == 24:
                if  c=="a" or c=="o" or c=="t" or c=="s":
                    buffer+=c
                    column += 1
                elif c=="(":
                    data_buffer+=buffer
                    token_handler.new_token(buffer, 'data', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                    column += 1
                    buffer=""
                    data_buffer+=c
                elif c==")":
                    data_buffer+=c
                    buffer+=c
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    column += 1
                    buffer=""
                    instruction_handler.new_instruction(data_buffer)
                    data_buffer=""
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column += 1
                    buffer=""
                    state=0
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 25, viene de recibir una "p" minúscula en estado 0, por lo que puede indicar la
            # función promedio(parametro), en este caso se recolecta y se verifica
            elif state == 25:
                if  c=="r" or c=="o" or c=="m" or c=="e" or c=="d" or c=="i":
                    buffer+=c
                    column += 1
                else:
                    if buffer == "promedio" and c=="(":
                        token_handler.new_token(buffer, 'average', line, column)
                        average_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        average_buffer+=c
                        buffer=""
                        state=26
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 26, viene de recibir un promedio, en este caso se recolecta, a que se desea
            #sacarle el promedio
            elif state == 26:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    average_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'parameter', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    average_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" " or c=="_" :
                    average_buffer+=c
                    buffer+=c
                    column+=1
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    average_buffer+=c
                    instruction_handler.new_instruction(average_buffer)
                    average_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 27, viene de recibir una letra "m" en el estado 0, verifica si se cumple
            # un max o un min
            elif state == 27:
                if  c=="a" or c=="x" or c=="m" or c=="i" or c=="n":
                    buffer+=c
                    column += 1
                else:
                    if buffer == "max" and c=="(":
                        token_handler.new_token(buffer, 'max', line, column)
                        max_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        max_buffer+=c
                        buffer=""
                        state=28
                    elif buffer=="min":
                        token_handler.new_token(buffer, 'min', line, column)
                        min_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        min_buffer+=c
                        buffer=""
                        state=29
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 28, viene de recibir un max, solo se recoleta, a lo que se le desea sacar max
            elif state == 28:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    max_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'parameter', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    max_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" " or c=="_" :
                    max_buffer+=c
                    buffer+=c
                    column+=1
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    max_buffer+=c
                    instruction_handler.new_instruction(max_buffer)
                    max_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 29, viene de recibir un min, solo revifica que sea la función
            elif state == 29:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    min_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'parameter', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    min_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" " or c=="_" :
                    min_buffer+=c
                    buffer+=c
                    column+=1
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    min_buffer+=c
                    instruction_handler.new_instruction(min_buffer)
                    min_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 30, viene de recibir una "e" minúscula en estado 0, por lo que puede indicar la
            # función exportarReporte(titulo), en este caso se recolecta y se verifica
            elif state == 30:
                if  c=="e" or c=="x" or c=="p" or c=="o" or c=="r" or c=="t" or c=="a" or c=="R":
                    buffer+=c
                    column += 1
                else:
                    if buffer == "exportarReporte" and c=="(":
                        token_handler.new_token(buffer, 'report', line, column)
                        export_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        export_buffer+=c
                        buffer=""
                        state=31
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 31, viene de recibir un exportarReporte, en este caso se recolecta, el título
            #que se desea ponerle al archivo HTML
            elif state == 31:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    export_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'title', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    export_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" " or c=="_" :
                    export_buffer+=c
                    buffer+=c
                    column+=1
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    export_buffer+=c
                    instruction_handler.new_instruction(export_buffer)
                    export_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================



            #=======================================================================================
            #Estado 32, viene de recibir un conteo, se verifica que sea la función
            elif state == 32:
                if c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    count_buffer+=c
                    instruction_handler.new_instruction(count_buffer)
                    count_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================


            #=======================================================================================
            #Estado 33, viene de recibir un contar si, en este caso se recolecta lo que se desea
            #contar
            elif state == 33:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    count_if_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'parameter', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    count_if_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c)  or c==" "  :
                    count_if_buffer+=c
                    buffer+=c
                    column+=1
                elif c==",":
                    count_if_buffer+=c
                    buffer+=c
                    token_handler.new_token(buffer, 'comma', line, column)
                    buffer=""
                    column+=1
                    state=38
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================



            #=======================================================================================
            #Estado 34, viene de recibir una "s" minúscula en estado 0, por lo que puede indicar la
            # función sumar(parametro), en este caso se recolecta y se verifica
            elif state == 34:
                if  c=="r" or c=="s" or c=="m" or c=="u" or c=="a" :
                    buffer+=c
                    column += 1
                else:
                    if buffer == "sumar" and c=="(":
                        token_handler.new_token(buffer, 'sum', line, column)
                        sum_buffer+=buffer
                        buffer=""
                        buffer+=c
                        token_handler.new_token(buffer, 'parenthesis_that_opens', line, column)
                        column+=1
                        sum_buffer+=c
                        buffer=""
                        state=35
                    else:
                        buffer+=c
                        column+=1
                        error_handler.new_error('Palabra ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                        buffer = ""
                        i -= 1
                        state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 35, viene de recibir un sumar, en este caso se recolecta, a que se desea
            #sacarle el promedio
            elif state == 35:
                if  c=='"' and len(buffer)==0:
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    sum_buffer+=c
                    buffer=""
                elif  c=='"' and len(buffer)!=0:
                    token_handler.new_token(buffer, 'parameter', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    sum_buffer+=c
                    buffer=""
                elif re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" " or c=="_" :
                    sum_buffer+=c
                    buffer+=c
                    column+=1
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    sum_buffer+=c
                    instruction_handler.new_instruction(sum_buffer)
                    sum_buffer=""
                    
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
                    state = 0
            #=======================================================================================

            #=======================================================================================
            #Estado 36, viene de recibir un '"', en este caso se recolecta, que se desea
            #imprimir
            elif state == 36:
                if  c=='"':
                    token_handler.new_token(buffer, 'message', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    print_buffer+=c
                    buffer=""
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    print_buffer+=c
                    instruction_handler.new_instruction(print_buffer)
                    print_buffer=""
                    state=0
                elif c=="\n":
                    line += 1
                    column = 1
                elif c == '\t':
                    column += 1
                else:
                    print_buffer+=c
                    buffer+=c
                    column+=1
            #=======================================================================================

            #=======================================================================================
            #Estado 37, viene de recibir un '"', en este caso se recolecta, que se desea
            #imprimirln
            elif state == 37:
                if  c=='"':
                    token_handler.new_token(buffer, 'message', line, column)
                    buffer=""
                    buffer+=c
                    token_handler.new_token(buffer, 'double_quotation_mark', line, column)
                    column += 1
                    println_buffer+=c
                    buffer=""
                elif c==";":
                    buffer+=c
                    token_handler.new_token(buffer, 'semicolon', line, column)
                    column+=1
                    buffer=""
                    state=0
                elif c==")":
                    #print(println_buffer)
                    buffer+=c
                    column+=1
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    println_buffer+=c
                    instruction_handler.new_instruction(println_buffer)
                    println_buffer=""
                    state=0
                elif c=="\n":
                    line += 1
                    column = 1
                elif c == '\t':
                    column += 1
                else:
                    println_buffer+=c
                    buffer+=c
                    column+=1
            #=======================================================================================

            #=======================================================================================
            #Estado 38, verifica si es string el segundo parametro del contarsi
            elif state==38:
                if re.search('[a-z]', c) or re.search('[A-Z]', c)  or c==" " or c=="_":
                    count_if_buffer+=c
                    buffer+=c
                    column+=1
                elif c==')':
                    token_handler.new_token(buffer, 'string_parameter', line, column)
                    buffer=""
                    column+=1
                    buffer+=c
                    token_handler.new_token(buffer, 'parenthesis_that_closes', line, column)
                    buffer=""
                    count_if_buffer+=c
                    instruction_handler.new_instruction(count_if_buffer)
                    count_if_buffer=""
                    state=33
                elif c.isdigit():
                    count_if_buffer+=c
                    buffer += c
                    column += 1
                    state=39
                else:
                    buffer+=c
                    column+=1
                    error_handler.new_error('caracter ' + "'"+buffer +"'"+ ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ""
                    i -= 1
            #=======================================================================================

            #=======================================================================================
            #Estado 39, verifica si es int o float el segundo parametro
            elif state==39:
                if c.isdigit():
                    buffer += c
                    count_if_buffer+=c
                    column += 1
                elif c==".":
                    buffer += c
                    column+=1
                    state=40
                elif c==")":
                    token_handler.new_token(buffer,"int_parameter",line,column)
                    buffer=""
                    column+=1
                    buffer+=c
                    token_handler.new_token(buffer,"parenthesis_that_closes",line,column)
                    buffer=""
                    column+=1
                    count_if_buffer+=c
                    instruction_handler.new_instruction(count_if_buffer)
                    count_if_buffer=""
                    state=33
                else:
                    error_handler.new_error('Caracter ' + buffer + ' no reconocido en el lenguaje.'
                    , 'Léxico', line, column)
                    buffer = ''
                    column += 1
            #=======================================================================================

            #=======================================================================================
            #Estado 40, se recibió un punto, por lo cual se recolecta el número float
            elif state==40:
                if c.isdigit():
                    buffer += c
                    count_if_buffer+=c
                    column += 1
                else:
                    if c==")":
                        token_handler.new_token(buffer,"float_parameter",line,column)
                        buffer=""
                        column+=1
                        buffer+=c
                        token_handler.new_token(buffer,"parenthesis_that_closes",line,column)
                        buffer=""
                        column+=1
                        count_if_buffer+=c
                        instruction_handler.new_instruction(count_if_buffer)
                        count_if_buffer=""
                        state=33
            #=======================================================================================
            i += 1
#========================================================================================================


    def print_tokens(self):
        token_handler.print_token()

    def print_errors(self):
        if len(error_handler.errors_list) == 0:
            print('No hubo errores')
        else:
            error_handler.print_error()