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
    
    def errors_html_report(self):
        f = open('REPORTES/ERRORS.html','w')
        error_html ="""<html>
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
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">O</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">R</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="red">E</font>
        <FONT SIZE=7 FACE="showcard gothic" COLOR="blue">S</font>

        </center>
        <style type="text/css" media="all">
        h1, h2 {display: inline;}
        </style>
        <hr />
        <center>
        <table width="500" border="2" cellpadding="5" >
        <tr>
        <th>DESCRIPCIÓN</th>
        <th>TIPO</th>
        <th>FILA</th>
        <th>COLUMNA</th>
        </tr>"""
        for error in self.errors_list:
            error_html+="""
            <tr>
            <td bgcolor= "#FF0F0F">"""+error.description+"""</td>
            <td bgcolor= "#FF0F0F">"""+error.type+"""</td>
            <td bgcolor= "#FF0F0F">"""+str(error.line)+"""</td>
            <td bgcolor= "#FF0F0F">"""+str(error.column)+"""</td>
            </tr>"""
        error_html+="""
        </table>
        </body>
        </html>"""
        f.write(error_html)
        f.close()