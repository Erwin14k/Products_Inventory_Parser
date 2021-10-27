from Expressions import *
from Lexical_Analyzer import register_handler
#from Products_Inventory_Parser import lexical_analyzer_handler


class Print_Instruction() :
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        value = self.expression.get_value(environment)
        register_handler.report_console+=value+" "
        print(value)
    
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "PRINT_INS")

        id_print = str(start())
        dot.node(id_print, "imprimir")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()
        #print(self.expression.get_nodes(),"=000")

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_print)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("print_todo bien")
        return id_node



class Println_Instruction() :
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        value = self.expression.get_value(environment)
        register_handler.report_console+="\n"+value
        print(value)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "PRINTLN_INS")

        id_print = str(start())
        dot.node(id_print, "imprimirln")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_print)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("println todo bien")
        return id_node

class Instruction_Instruction() :
    def __init__(self, instruction) :
        self.instruction = instruction

    def do_it(self, environment):
        self.instruction.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "INSTRUCTION")

        son = self.instruction.get_nodes()

        dot.edge(id_node, son)
        #print("Instruccion instruccion todo bien")
        return id_node



class Instructions_List_2() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        #print(self.list)
        if self.instruction:
            #print("aheeeeeeeeeeeeeee")
            self.instruction.do_it(environment)
            if self.list:
                #print("aheeeeeeeeeeeeeee2")
                self.list.do_it(environment)
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "INSTRUCTIONS_LIST_2")
        if self.instruction:
            son = self.instruction.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
        #print("Instruccion list 2 todo bien")
        return id_node


class Instructions_List() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        if self.instruction:
            print("qie peee")
            self.instruction.do_it(environment)
            if self.list:
                print("queueuueue")
                self.list.do_it(environment)


    
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "INSTRUCTIONS_LIST")
        if self.instruction:
            son = self.instruction.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
        #print("Instruccion list todo bien")
        return id_node
class Sum_Instruction():
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        parameter= self.expression.get_value(environment)
        print(parameter)
        temp_data=[]
        temp_data+=register_handler.registers_list
        column_number=0
        column_number=int(temp_data[0].index(parameter))
        column = [row[column_number] for row in temp_data]
        total_sum=0
        for j in column:
            if j!=parameter:
                total_sum = total_sum+ int(j)
        print("=======================================Reporte Suma==========================================")
        print("sumar: ",str(total_sum))
        register_handler.report_console+="\n"+str(total_sum)
        total_sum=0
        print("=============================================================================================")
        print("\n\n")
    
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "SUM_INS")

        id_sum = str(start())
        dot.node(id_sum, "sumar")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_sum)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion suma todo bien")
        return id_node

class Data_Instruction():
    def __init__(self) :
        self.expression = 0

    def do_it(self,environment):
        temp_data=[]
        temp_data+=register_handler.registers_list
        register_handler.report_console+="\n"
        print("========================================Reporte Datos========================================")
        for i in temp_data:
            for j in  i:
                print( j, end="  ")
                register_handler.report_console+=">>>"+str(j)+"  "
            print()
            register_handler.report_console+="\n"

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "DATA_INS")

        id_data = str(start())
        dot.node(id_data, "datos")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_data)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion Datos todo bien")
        return id_node

class Count_Instruction():
    def __init__(self) :
        self.expression=0
    def do_it(self,environment):
        temp_data=[]
        temp_data+=register_handler.registers_list
        register_counter=0
        register_counter=len(temp_data)-1
        print("=======================================Reporte Conteo========================================")
        print("conteo: ",str(register_counter))
        register_handler.report_console+="\n"+str(register_counter)
        print("=============================================================================================")
        print("\n\n")

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "COUNT_INS")

        id_count = str(start())
        dot.node(id_count, "conteo")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_count)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion conteo todo bien")
        return id_node
class Countif_Instruction():
    def __init__(self,key,value) :
        self.key = key
        self.value =value
    def do_it(self,environment):
        parameter1 = self.key.get_value(environment)
        parameter2 = self.value.get_value(environment)
        temp_data=[]
        temp_data+=register_handler.registers_list
        column_number=0
        column_number=int(temp_data[0].index(parameter1))
        column = [row[column_number] for row in temp_data]
        total_sum=0
        for j in column:
            if j!=parameter1 and float(j)==float(parameter2):
                total_sum +=1
        print("====================================Reporte Contarsi=========================================")
        print("contarsi: ",str(total_sum))
        register_handler.report_console+="\n"+str(total_sum)
        total_sum=0
        print("=============================================================================================")
        print("\n\n")
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "COUNTIF_INS")

        id_count_if = str(start())
        dot.node(id_count_if, "contarsi")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.key.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_comma = str(start())
        dot.node(id_comma, ',')
        son2 = self.value.get_nodes()

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_count_if)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_comma)
        dot.edge(id_node, son2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion conteoif todo bien")
        return id_node

class Average_Instruction():
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        parameter= self.expression.get_value(environment)
        temp_data=[]
        temp_data+=register_handler.registers_list
        column_number=0
        column_number=int(temp_data[0].index(parameter))
        column = [row[column_number] for row in temp_data]
        total_count=len(column)-1
        total_sum=0
        for j in column:
            if j!=parameter:
                total_sum = total_sum+ int(j)
        avg=float(total_sum/total_count)
        print("=======================================Reporte Promedio======================================")
        print("promedio",str(avg))
        register_handler.report_console+="\n"+str(avg)
        print("=============================================================================================")
        print("\n\n")
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "AVERAGE_INS")

        id_average = str(start())
        dot.node(id_average, "promedio")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_average)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion promedio todo bien")
        return id_node

class Max_Instruction():
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        parameter = self.expression.get_value(environment)
        temp_data=[]
        temp_data+=register_handler.registers_list
        column_number=0
        column_number=int(temp_data[0].index(parameter))
        column = [row[column_number] for row in temp_data]
        length = len(column)
        for i in range(0,length):
            if column[i]==parameter:
                column[i]=float(-2.00)
        for i in range(len(column)):
            for j in range(len(column) - 1):
                if column[j] < column[j+1]:
                    column[j], column[j+1] = column[j+1], column[j]
        print("========================================Reporte Max==========================================")
        print("max",str(column[0]))
        register_handler.report_console+="\n"+str(column[0])
        print("=============================================================================================")
        print("\n\n")

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "MAX_iNS")

        id_max = str(start())
        dot.node(id_max, "max")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_max)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion MAX todo bien")
        return id_node

class Min_Instruction():
    def __init__(self, expression) :
        self.expression = expression

    def do_it(self, environment):
        parameter = self.expression.get_value(environment)
        temp_data=[]
        temp_data+=register_handler.registers_list
        column_number=0
        column_number=int(temp_data[0].index(parameter))
        column = [row[column_number] for row in temp_data]
        length = len(column)
        for i in range(0,length):
            if column[i]==parameter:
                column[i]=float(9999999.00)
        for i in range(len(column)):
            for j in range(len(column) - 1):
                if column[j] > column[j+1]:
                    column[j], column[j+1] = column[j+1], column[j]
        print("========================================Reporte Min==========================================")
        print("max",str(column[0]))
        register_handler.report_console+="\n"+str(column[0])
        print("=============================================================================================")
        print("\n\n")

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "MIN_INS")

        id_min = str(start())
        dot.node(id_min, "min")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_min)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion MIN todo bien")
        return id_node
class Export_Instruction():
    def __init__(self, expression) :
        self.expression = expression
    def do_it(self, environment):
        parameter = self.expression.get_value(environment)
        rows=0
        cols=0
        temp_data=[]
        temp_data+=register_handler.registers_list
        rows=len(temp_data)
        cols=len(temp_data[0])
        f = open('Reportes/'+parameter+'.html','w')
        instruction_html ='''<html>
        <head></head>
        <body bgcolor="#FFA07A">
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">r</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">w</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">i</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">n</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">_</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">V</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">á</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">s</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">q</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">u</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">e</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">z</font>
        <center>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">L</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">F</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">P</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">_</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">P</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">O</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">Y</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">C</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">T</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">O</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">_</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">2</font>
        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="500" border="2" cellpadding="5" >
        <caption>'''+parameter+"""</caption>"""
        for i in range(0,rows):
            instruction_html+="""<tr>"""
            for j in  range(0,cols):
                instruction_html+='''
                <td>'''+str(temp_data[i][j])+'''</td>'''
            instruction_html+='''</tr>'''
        instruction_html+="""
        </table>
        </body>
        </html>"""
        f.write(instruction_html)
        f.close()
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "EXPORT_INS")

        id_export = str(start())
        dot.node(id_export, "exportarReporte")

        id_parenthesis_that_opens = str(start())
        dot.node(id_parenthesis_that_opens, "(")

        id_double_quotation_mark = str(start())
        dot.node(id_double_quotation_mark, '"')

        son = self.expression.get_nodes()

        id_double_quotation_mark_2 = str(start())
        dot.node(id_double_quotation_mark_2, '"')

        id_parenthesis_that_closes = str(start())
        dot.node(id_parenthesis_that_closes, ")")

        id_semicolon = str(start())
        dot.node(id_semicolon, ";")        

        dot.edge(id_node, id_export)
        dot.edge(id_node, id_parenthesis_that_opens)
        dot.edge(id_node, id_double_quotation_mark)
        dot.edge(id_node, son)
        dot.edge(id_node, id_double_quotation_mark_2)
        dot.edge(id_node, id_parenthesis_that_closes)
        dot.edge(id_node, id_semicolon)
        #print("Instruccion Export todo bien")
        return id_node
class Register_Instruction():
    def __init__(self,list) :
        self.list = list
    def do_it(self, environment):
        self.list.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "REGISTERS")
        id_reg = str(start())
        dot.node(id_reg, "Registros")

        id_equals = str(start())
        dot.node(id_equals, "=")

        id_open_square_bracket = str(start())
        dot.node(id_open_square_bracket, '[')

        son = self.list.get_nodes()

        id_closed_square_bracket = str(start())
        dot.node(id_closed_square_bracket, "]")
        dot.edge(id_node, id_reg)
        dot.edge(id_node, id_equals)
        dot.edge(id_node, id_open_square_bracket)
        dot.edge(id_node, son)
        dot.edge(id_node, id_closed_square_bracket)
        #print("Instruccion Register todo bien")
        return id_node
class Register_List() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        if self.instruction:
            self.instruction.do_it(environment)
            if self.list:
                self.list.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "REGISTER_LIST")
        if self.instruction:
            son = self.instruction.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
        #print("Instruccion Register_list todo bien")
        return id_node

class Register_List_2() :
    def __init__(self, instruction, list) :
        self.instruction = instruction
        self.list = list

    def do_it(self, environment):
        #print(self.list)
        if self.instruction:
            self.instruction.do_it(environment)
            if self.list:
                self.list.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "REGISTER_LIST_2")
        if self.instruction:
            son = self.instruction.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
        #print("Instruccion Register list2 todo bien")
        return id_node

class Keys_Instruction():
    def __init__(self,list) :
        self.list = list
    def do_it(self, environment):
        self.list.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "KEYS_INS")

        id_keys = str(start())
        dot.node(id_keys, "CLAVES")

        id_equals = str(start())
        dot.node(id_equals, "=")

        id_open_square_bracket = str(start())
        dot.node(id_open_square_bracket, '[')

        son = self.list.get_nodes()

        id_closed_square_bracket = str(start())
        dot.node(id_closed_square_bracket, ']')

        dot.edge(id_node, id_keys)
        dot.edge(id_node, id_equals)
        dot.edge(id_node, id_open_square_bracket)
        dot.edge(id_node, son)
        dot.edge(id_node, id_closed_square_bracket)
        #print("Instruccion keys todo bien")
        return id_node


    
class Keys_List() :
    def __init__(self, key, list) :
        self.key = key
        self.list = list

    def do_it(self, environment):
        print(self.list,"0000000000")
        if self.key:
            print("si 1")
            self.key.do_it(environment)
            if self.list:
                print("si 2")
                self.list.do_it(environment)

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "KEYS_LIST")
        #print("aqui por lo menos")
        if self.key:
            #print("aquí si se llega")
            son = self.key.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
                #print("holaaaaaaaaaa2")
        #print("Instruccion key_List todo bien")
        return id_node

class Keys_List_2() :
    def __init__(self, key, list) :
        self.key = key
        self.list = list

    def do_it(self, environment):
        print(self.list,"=0000000000000")
        if self.key:
            self.key.do_it(environment)
            if self.list:
                self.list.do_it(environment)
                print("holaaaaaaaaaa3")

    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "KEYS_LIST_2")
        if self.key:
            son = self.key.get_nodes()
            dot.edge(id_node, son)
            if self.list:
                son2 = self.list.get_nodes()
                dot.edge(id_node, son2)
        #print("Instruccion key_list2 todo bien")
        return id_node
class Epsilon_Instruction() :
    def __init__(self) :
        pass
    
    def do_it(self, environment):
        pass

    def get_nodes(self):
        global dot

        #padre
        id_node = str(start())
        dot.node(id_node, "Epsilon")
        #print("Instruccion Epsilon todo bien")

        return id_node


class Beggining_Instruction() :
    def __init__(self,list) :
        self.list = list

    def do_it(self, environment):
        self.list.do_it(environment)
        #print("hola")
    
    def get_nodes(self):
        global dot
        id_node = str(start())
        dot.node(id_node, "BEGGINING")
        son = self.list.get_nodes()
        dot.edge(id_node, son)
        #print("al fin1!!")
        print("")
        print("")
        print("Gerando Árbol de derivación......")
        dot.view()
        return id_node



