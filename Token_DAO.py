from Token import  Token
class Token_DAO:
    def __init__(self):
        self.tokens_list = []
        self.color=""

    #Función para crear nuevos Tokens
    def new_token(self,lexem, type,  line, column):
        new = Token(lexem, type,  line, column)
        self.tokens_list.append(new)
        return True

    def print_token(self):
        for token in self.tokens_list:
            print(token.lexem,token.type,str(token.line),str(token.column))
    
    def tokens_html_report(self):
        f = open('Reportes/TOKENS.html','w')
        token_html ="""<html>
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
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">P</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">O</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">T</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">_</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">D</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">_</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">T</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">O</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">K</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">N</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">S</font>

        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="500" border="2" cellpadding="5" >
        <tr>
        <th>TOKEN</th>
        <th>LEXEMA</th>
        <th>FILA</th>
        <th>COLUMNA</th>
        </tr>"""
        for token in self.tokens_list:
            if token.type == 'CLAVES' or token.type == 'Clave' or token.type == 'Registros':
                token_html+="""
                <tr>
                <td bgcolor= "#39BBC4">"""+token.type+"""</td>
                <td bgcolor= "#39BBC4">"""+token.lexem+"""</td>
                <td bgcolor= "#39BBC4">"""+str(token.line)+"""</td>
                <td bgcolor= "#39BBC4">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'open_key' or token.type == 'closed_key'  or token.type == 'semicolon' or token.type == 'comma'or token.type == 'equals'or token.type == 'double_quotation_mark' or token.type=='open_square_bracket'or token.type=='closed_square_bracket'  or token.type=="parenthesis_that_closes" or token.type=="parenthesis_that_opens":
                token_html+="""
                <tr>
                <td bgcolor= "#1DEA38">"""+token.type+"""</td>
                <td bgcolor= "#1DEA38">"""+token.lexem+"""</td>
                <td bgcolor= "#1DEA38">"""+str(token.line)+"""</td>
                <td bgcolor= "#1DEA38">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'int_value':
                token_html+="""
                <tr>
                <td bgcolor= "#E9AC17">"""+token.type+"""</td>
                <td bgcolor= "#E9AC17">"""+token.lexem+"""</td>
                <td bgcolor= "#E9AC17">"""+str(token.line)+"""</td>
                <td bgcolor= "#E9AC17">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'float_value':
                token_html+="""
                <tr>
                <td bgcolor= "#5883DB">"""+token.type+"""</td>
                <td bgcolor= "#5883DB">"""+token.lexem+"""</td>
                <td bgcolor= "#5883DB">"""+str(token.line)+"""</td>
                <td bgcolor= "#5883DB">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'string_value':
                token_html+="""
                <tr>
                <td bgcolor= "#C784EA">"""+token.type+"""</td>
                <td bgcolor= "#C784EA">"""+token.lexem+"""</td>
                <td bgcolor= "#C784EA">"""+str(token.line)+"""</td>
                <td bgcolor= "#C784EA">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'simple_comment' or token.type=="multiple_comment":
                token_html+="""
                <tr>
                <td bgcolor= "#BDEC0D">"""+token.type+"""</td>
                <td bgcolor= "#BDEC0D">"""+token.lexem+"""</td>
                <td bgcolor= "#BDEC0D">"""+str(token.line)+"""</td>
                <td bgcolor= "#BDEC0D">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type=="print" or token.type=="println":
                token_html+="""
                <tr>
                <td bgcolor= "#FF7AF5">"""+token.type+"""</td>
                <td bgcolor= "#FF7AF5">"""+token.lexem+"""</td>
                <td bgcolor= "#FF7AF5">"""+str(token.line)+"""</td>
                <td bgcolor= "#FF7AF5">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'count' or token.type=="max" or token.type=="min" or token.type=="count_if":
                token_html+="""
                <tr>
                <td bgcolor= "#3650EB">"""+token.type+"""</td>
                <td bgcolor= "#3650EB">"""+token.lexem+"""</td>
                <td bgcolor= "#3650EB">"""+str(token.line)+"""</td>
                <td bgcolor= "#3650EB">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'data' or token.type=="average" :
                token_html+="""
                <tr>
                <td bgcolor= "#3DDDE3">"""+token.type+"""</td>
                <td bgcolor= "#3DDDE3">"""+token.lexem+"""</td>
                <td bgcolor= "#3DDDE3">"""+str(token.line)+"""</td>
                <td bgcolor= "#3DDDE3">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'message' or token.type=="parameter" or token.type=="int_parameter" :
                token_html+="""
                <tr>
                <td bgcolor= "#3EEBA8">"""+token.type+"""</td>
                <td bgcolor= "#3EEBA8">"""+token.lexem+"""</td>
                <td bgcolor= "#3EEBA8">"""+str(token.line)+"""</td>
                <td bgcolor= "#3EEBA8">"""+str(token.column)+"""</td>
                </tr>"""
            elif token.type == 'title' or token.type=="report" :
                token_html+="""
                <tr>
                <td bgcolor= "#FC8D3B">"""+token.type+"""</td>
                <td bgcolor= "#FC8D3B">"""+token.lexem+"""</td>
                <td bgcolor= "#FC8D3B">"""+str(token.line)+"""</td>
                <td bgcolor= "#FC8D3B">"""+str(token.column)+"""</td>
                </tr>"""
        token_html+="""
        </table>
        </body>
        </html>"""
        f.write(token_html)
        f.close()