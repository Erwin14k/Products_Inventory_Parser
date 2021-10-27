#-*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import re
import webbrowser as wb
from Lexical_Analyzer import Lexical_Analyzer
from Lexical_Analyzer import token_handler,error_handler,register_handler,instruction_handler
from Parser import Parser
report_text=""
parser_handler=Parser()
lexical_analyzer_handler=Lexical_Analyzer()

#============================================================================================================
#Creación de la raíz aplicando algunos atributos
root=Tk()
root.title("Products Inventory Parser v1.0")
root.resizable(False,False)
root.iconbitmap("img/cobra_kai.ico")
root.config(cursor="hand2")
root.geometry("1200x600")
root.config(bg="Red")
root.config(relief="groove")
root.config(bd="30")
#============================================================================================================



#============================================================================================================
#Creación del frame principal aplicando algunos atributos y elementos
main_frame=Frame(root,width="800",height="430")
main_frame.pack()
main_frame.config(bg="SpringGreen4")
main_frame.config(bd="20")
main_frame.config(relief="flat")
main_frame.config(cursor="hand2")
#Label del titulo del frame principal
Label(main_frame,text="PRODUCT INVENTORY PARSER ",fg="gold",font=("showcard gothic",30),bg="SpringGreen4").place(x=70,y=20)
#Label que contendrá una imagen de inicio
logo_image=PhotoImage(file="img/inventory.png")
Label(main_frame,image=logo_image,bg="SpringGreen4").place(x=170,y=80)
#Botón para iniciar la aplicación
principal_Button=Button()
principal_Button.config(text="Iniciar", width="25",height="1",bg="SpringGreen4",fg="gold",font=("showcard gothic",20))
principal_Button.pack()
#============================================================================================================



#============================================================================================================
#Creación del frame con todas las funciones 
master_frame=Frame(root,width="650",height="100")
master_frame.config(bg="gold")
master_frame.config(bd="20")
master_frame.config(relief="groove")
master_frame.config(cursor="hand2")
upload_Button=Button(master_frame,text="Cargar Archivo",font=("showcard gothic",15),bg="SpringGreen4",fg="yellow")
upload_Button.grid(row=0,column=0,padx=10)
analyze_Button=Button(master_frame,text="Analizar Archivo",font=("showcard gothic",15),bg="SpringGreen4",fg="yellow")
analyze_Button.grid(row=0,column=1,padx=10)
reports_Button=Button(master_frame,text="Reportes",font=("showcard gothic",15),bg="SpringGreen4",fg="yellow")
reports_Button.grid(row=0,column=2,padx=10)
information_Button=Button(master_frame,text="Información",font=("showcard gothic",15),bg="SpringGreen4",fg="yellow")
information_Button.grid(row=0,column=3,padx=10)
exit_Button=Button(master_frame,text=" Salir",font=("showcard gothic",15),bg="SpringGreen4",fg="yellow")
exit_Button.grid(row=0,column=4,padx=10)

#============================================================================================================



#============================================================================================================
#Función encargada de iniciar la aplicación
def master_mind_window():
    main_frame.destroy()
    principal_Button.destroy()
    root.geometry("1450x700")
    master_frame.pack()
    Label(text="Edición De Texto: ",bg="red",font=("showcard gothic",20),fg="yellow").place(x=30,y=100)
    edit_frame.place(x=30,y=150)
    Label(text="Reportes En Consola: ",bg="red",font=("showcard gothic",20),fg="yellow").place(x=690,y=100)
    console_frame.place(x=700,y=150)
    #master_frame.grid(row=0,column=0)
    #edit_frame.grid(row=1,column=0)
#Con este botón inicializamos esta función
principal_Button.config(command=master_mind_window)
#============================================================================================================ 



#============================================================================================================
#Creación del área donde se puede editar el texto
edit_frame=Frame(root,width="600",height="470")
edit_frame.grid_propagate(FALSE)
edit_frame.config(relief="groove")
edit_frame.config(cursor="hand2")
#Se crea el área de texto
editable_text=Text(edit_frame,width=85,height=29)
editable_text.config(font=("Arial",10))
editable_text.grid(row=1, column=0)
#Se crea el scrollbar en y
scrolly = Scrollbar(edit_frame,command=editable_text.yview)
scrolly.grid(row=1, column=0, sticky="nse")
editable_text.config(yscrollcommand=scrolly.set)












#============================================================================================================



#============================================================================================================
#Creación del botón donde se pueden visualizar los datos generados
console_frame=Frame(root,width="650",height="470")
console_frame.grid_propagate(FALSE)
console_frame.config(relief="groove")
console_frame.config(cursor="hand2")
console_text=Text(console_frame)
console_text.configure(state='disabled')
console_text.pack()
#============================================================================================================





#============================================================================================================
#Función para cargar el archivo con extensión "lfp" a memoria, además de poder visualizarlo y editarlo.
route=""
original_text=""
def upload_file():
    global route,original_text,editable_text
    route = askopenfilename()
    if route.endswith("lfp"):
        archive = open(route,"r")
        original_text=archive.read()
        archive.close()
        #print(original_text)
        editable_text.insert("1.0",original_text)
        messagebox.showinfo(title="Products Inventory Parser v1.0",message="El archivo fue cargado con éxito al sistema!!")
    else:
        messagebox.showerror(title="Products Inventory Parser v1.0",message="No es un archivo con extensión 'lfp', intenta de nuevo!!")
        upload_file()
upload_Button.config(command=upload_file)
#============================================================================================================



#============================================================================================================
#Función para analizar el archivo "lfp", dónde se recolectan tokens, además, errores léxicos y sintácticos.

def analyze_file():
    global editable_text,console_text
    lexical_analyzer_handler.lexical_analyze_file(editable_text.get("1.0",'end-1c'))
    parser_handler.analyze(token_handler.tokens_list)
    console_text.configure(state='normal')
    console_text.insert("end-1c",register_handler.report_console)
    console_text.configure(state='disabled')
    #lexical_analyzer_handler.print_tokens()
    #lexical_analyzer_handler.print_errors()
    #register_handler.print_registers()
    #instruction_handler.print_instructions()
    #lexical_analyzer_handler.print_errors()
    #reports_generator()

analyze_Button.config(command=analyze_file)
#============================================================================================================


#============================================================================================================
#Función que muestra información del estudiante
def student_information():
    messagebox.showinfo(title="Products Inventory Parser v1.0",message="Master Mind: Erwin Vásquez\n LFP Sección 'B+'\n Proyecto 2")
information_Button.config(command=student_information)
#============================================================================================================

#============================================================================================================
#Función para abrir automáticamente los reportes de tokens y de errores
def reports_view():
    token_handler.tokens_html_report()
    error_handler.errors_html_report()
    messagebox.showinfo(title="Image Maker V1.0", message="Se Abrirán Los siguientes Reportes:\n-Reporte De Tokens\n"
    "-Reporte De errores")
    os.system("C:/Users/Erwin14k/Documents/Products_Inventory_Parser/REPORTES/TOKENS.html")
    os.system("C:/Users/Erwin14k/Documents/Products_Inventory_Parser/REPORTES/ERRORS.html")
reports_Button.config(command=reports_view)
#============================================================================================================

#============================================================================================================
#Función que termina con la ejecución de la aplicación
def exit_application():
    exit()
exit_Button.config(command=exit_application)
#============================================================================================================

#============================================================================================================
#La útlima instrucción de la raíz, ejecutará todo lo que esté arriba de este método
root.mainloop()
#============================================================================================================

'''def reports_generator():
    global report_text,console_text
    report_text=""
    temporal_text=""
    for instruction in instruction_handler.instructions_list:
        if instruction.what_should_I_do.count("exportarReporte(")>=1:
            aux=""
            archive_name=""
            aux+=instruction.what_should_I_do.replace('exportarReporte("',"")
            aux.replace('")',"")
            archive_name+=aux.replace('")',"")
            rows=0
            cols=0
            temp_data=[]
            temp_data+=register_handler.registers_list
            rows=len(temp_data)
            cols=lexical_analyzer_handler.cols
            f = open('Reportes/'+archive_name+'.html','w')
            instruction_html =''' '''<html>'''
'''<head></head>
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
            <caption>+archive_name+/caption>"""
            for i in range(0,rows):
                instruction_html+="""<tr>"""
                for j in  range(0,cols):
                    instruction_html+=
                    <td>+str(temp_data[i][j])+</td>
                instruction_html+=</tr>
            instruction_html+="""
            </table>
            </body>
            </html>"""
            f.write(instruction_html)
            f.close()
        elif instruction.what_should_I_do.count("datos(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            print("========================================Reporte Datos========================================")
            for i in temp_data:
                for j in  i:
                    print( j, end="  ")
                    report_text+=">>>"+str(j)+"  "
                print()
                report_text+="\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("promedio(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            aux2=""
            parameter=""
            aux2+=instruction.what_should_I_do.replace('promedio("',"")
            aux2.replace('")',"")
            parameter+=aux2.replace('")',"")
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
            report_text+=">>>"+str(avg)+"\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("max(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            aux3=""
            parameter2=""
            aux3+=instruction.what_should_I_do.replace('max("',"")
            aux3.replace(')',"")
            parameter2+=aux3.replace('")',"")
            column_number=0
            column_number=int(temp_data[0].index(parameter2))
            column = [row[column_number] for row in temp_data]
            length = len(column)
            for i in range(0,length):
                if column[i]==parameter2:
                    column[i]=float(0.00)
            for i in range(len(column)):
                for j in range(len(column) - 1):
                    if column[j] < column[j+1]:
                        column[j], column[j+1] = column[j+1], column[j]

            print("========================================Reporte Max==========================================")
            print("max",str(column[0]))
            report_text+=">>>"+str(column[0])+"\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        
        elif instruction.what_should_I_do.count("min(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            aux3=""
            parameter2=""
            aux3+=instruction.what_should_I_do.replace('min("',"")
            aux3.replace(')',"")
            parameter2+=aux3.replace('")',"")
            column_number=0
            column_number=int(temp_data[0].index(parameter2))
            column = [row[column_number] for row in temp_data]
            length = len(column)
            for i in range(0,length):
                if column[i]==parameter2:
                    column[i]=float(999999.00)
            for i in range(len(column)):
                for j in range(len(column) - 1):
                    if column[j] > column[j+1]:
                        column[j], column[j+1] = column[j+1], column[j]

            print("========================================Reporte Min==========================================")
            print("min",str(column[0]))
            report_text+=">>>"+str(column[0])+"\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("sumar(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            aux2=""
            parameter=""
            aux2+=instruction.what_should_I_do.replace('sumar("',"")
            aux2.replace('")',"")
            parameter+=aux2.replace('")',"")
            column_number=0
            column_number=int(temp_data[0].index(parameter))
            column = [row[column_number] for row in temp_data]
            total_count=len(column)-1
            total_sum=0
            for j in column:
                if j!=parameter:
                    total_sum = total_sum+ int(j)
            print("=======================================Reporte Suma==========================================")
            print("sumar: ",str(total_sum))
            report_text+=">>>"+str(total_sum)+"\n"
            total_sum=0
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("contarsi(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            aux2=""
            parameter=""
            parameters=""
            final_parameters=[]
            aux2+=instruction.what_should_I_do.replace('contarsi("',"")
            parameter+=aux2.replace('"',"")
            parameters+=parameter.replace(")","")
            final_parameters+=parameters.split(",")
            column_number=0
            column_number=int(temp_data[0].index(final_parameters[0]))
            column = [row[column_number] for row in temp_data]
            total_sum=0
            for j in column:
                if j!=final_parameters[0] and float(j)==float(final_parameters[1]):
                    total_sum +=1
            print("====================================Reporte Contarsi=========================================")
            print("contarsi: ",str(total_sum))
            report_text+=">>>"+str(total_sum)+"\n"
            total_sum=0
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("conteo(")>=1:
            temp_data=[]
            temp_data+=register_handler.registers_list
            register_counter=0
            register_counter=len(temp_data)-1
            print("=======================================Reporte Conteo========================================")
            print("conteo: ",str(register_counter))
            report_text+=">>>"+str(register_counter)+"\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("imprimir(")>=1:
            aux2=""
            parameter=""
            aux2+=instruction.what_should_I_do.replace('imprimir("',"")
            aux2.replace('")',"")
            parameter+=aux2.replace('")',"")
            temporal_text+=parameter
            print("============================================PRINT============================================")
            print("imprimir en consola: ",temporal_text)
            report_text+=">>>"+str(temporal_text)+"\n"
            temporal_text=""
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
        elif instruction.what_should_I_do.count("imprimirln(")>=1:
            aux2=""
            parameter=""
            text=""
            aux2+=instruction.what_should_I_do.replace('imprimirln("',"")
            aux2.replace('")',"")
            parameter+=aux2.replace('")',"")
            text+=parameter
            print("==========================================PRINTLN============================================")
            print("imprimir en consola: ",text)
            report_text+=">>>"+str(text)+"\n"
            print("=============================================================================================")
            print("\n\n")
            console_text.configure(state='normal')
            console_text.insert("end-1c",report_text)
            console_text.configure(state='disabled')
            report_text=""
            '''
''''''