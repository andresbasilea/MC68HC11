from tkinter import filedialog
from tkinter import *
import os
import shutil
import re
archivo = []
MNEMONICOS={"ABA":["","","","","","1B",""], "ABX":["","","","","","3A",""], "ABY":["","","","","","183A",""], "ADCA":["89","99","A9","18A9","B9","",""], "ADCB":["C9","D9","E9","18E9","F9","",""], "ADDA":["8B","9B","AB","18AB","BB","",""], "ADDB":["CB","DB","EB","18EB","FB","",""], "ADDD":["C3","D3","E3","18E3","F3","",""], "ANDA":["84","94","B4","18A4","B4","",""], "ANDB":["C4","D4","E4","18E4","F4","",""], "ASL":["","","68","1868","78","",""], "ASLA":["","","","","","48",""], "ASLB":["","","","","","58",""], "ASLD":["","","","","","05",""], "ASR":["","","67","1867","77","",""], "ASRA":["","","","","","47",""], "ASRB":["","","","","","57",""], "BCC":["","","","","","","24"], "BCLR":["","15","1D","181D","","",""], "BCS":["","","","","","","25"], "BEQ":["","","","","","","27"], "BGE":["","","","","","","2C"], "BGT":["","","","","","","2E"], "BHI":["","","","","","","22"], "BHS":["","","","","","","24"], "BITA":["85","95","A5","18A5","B5","",""], "BITB":["C5","D5","E5","18E5","F5","",""], "BLE":["","","","","","","2F"], "BLO":["","","","","","","25"], "BLS":["","","","","","","23"], "BLT":["","","","","","","2D"], "BMI":["","","","","","","2B"], "BNE":["","","","","","","26"], "BPL":["","","","","","","2A"], "BRA":["","","","","","","20"], "BRCLR":["","13","1F","181F","","",""], "BRN":["","","","","","","21"], "BRSET":["","12","1E","181E","","",""], "BSET":["","14","1C","181C","","",""], "BSR":["","","","","","","8D"], "BVC":["","","","","","","28"], "BVS":["","","","","","","29"], "CBA":["","","","","","11",""], "CLC":["","","","","","0C",""], "CLI":["","","","","","0E",""], "CLR":["","","6F","186F","7F","",""], "CLRA":["","","","","","4F",""], "CLRB":["","","","","","5F",""], "CLV":["","","","","","0A",""], "CMPA":["81","91","A1","18A1","B1","",""], "CMPB":["C1","D1","E1","18E1","F1","",""], "COM":["","","63","1863","73","",""], "COMA":["","","","","","43",""], "COMB":["","","","","","53",""], "CPD":["1A83","1A93","1AA3","CDA3","1AB3","",""], "CPX":["8C","9C","AC","CDAC","BC","",""], "CPY":["188C","189C","1AAC","18AC","18BC","",""], "DAA":["","","","","","19",""], "DEC":["","","6A","186A","7A","",""], "DECA":["","","","","","4A",""], "DECB":["","","","","","5A",""], "DES":["","","","","","34",""], "DEX":["","","","","","09",""], "DEY":["","","","","","1809",""], "EORA":["88","98","A8","18A8","B8","",""], "EORB":["C8","D8","E8","18E8","F8","",""], "FDIV":["","","","","","03",""], "IDIV":["","","","","","02",""], "INC":["","","6C","186C","7C","",""], "INCA":["","","","","","4C",""], "INCB":["","","","","","5C",""], "INS":["","","","","","31",""], "INX":["","","","","","08",""], "INY":["","","","","","1808",""], "JMP":["","","6E","186E","7E","",""], "JSR":["","9D","AD","18AD","BD","",""], "LDAA":["86","96","A6","18A6","B6","",""], "LDAB":["C6","D6","E6","18E6","F6","",""],"LDD":["CC","DC","EC","18EC","FC","",""], "LDS":["8E","9E","AE","18AE","BE","",""], "LDX":["CE","DE","EE","CDEE","FE","",""], "LDY":["18CE","18DE","1AEE","18EE","18FE","",""], "LSL":["","","68","1868","78","",""], "LSLA":["","","","","48",""], "LSLB":["","","","","","58",""], "LSLD":["","","","","","05",""], "LSR":["","","64","1864","74","",""], "LSRA":["","","","","","44",""], "LSRB":["","","","","","54",""], "LSRD":["","","","","","04",""], "MUL":["","","","","","3D",""], "NEG":["","","60","1860","70","",""], "NEGA":["","","","","","40",""], "NEGB":["","","","","","50",""], "NOP":["","","","","","01",""], "ORAA":["8A","9A","AA","18AA","BA","",""], "ORAB":["CA","DA","EA","18EA","FA","",""], "PSHA":["","","","","","36",""], "PSHB":["","","","","","37",""], "PSHX":["","","","","","3C",""], "PSHY":["","","","","","183C",""], "PULA":["","","","","","32",""], "PULB":["","","","","","33",""], "PULX":["","","","","","38",""], "PULY":["","","","","","1838",""], "ROL":["","","69","1869","79","",""], "ROLA":["","","","","","49",""], "ROLB":["","","","","","59",""], "ROR":["","","66","1866","76","",""], "RORA":["","","","","","46",""], "RORB":["","","","","","56",""], "RTI":["","","","","","3B",""], "RTS":["","","","","","39",""], "SBA":["","","","","","10",""], "SBCA":["82","92","A2","18A2","B2","",""], "SBCB":["C2","D2","E2","18E2","F2","",""], "SEC":["","","","","","OD",""], "SEI":["","","","","","OF",""], "SEV":["","","","","","OB",""], "STAA":["","97","A7","18A7","B7","",""], "STAB":["","D7","E7","18E7","F7","",""], "STD":["","DD","ED","18ED","FD","",""], "STOP":["","","","","","CF",""], "STS":["","9F","AF","18AF","BF","",""], "STX":["","DF","EF","CDEF","FF","",""], "STY":["","18DF","1AEF","18EF","FF","",""], "SUBA":["80","90","A0","18A0","B0","",""], "SUBB":["C0","D0","E0","18E0","F0","",""], "SUBD":["83","93","A3","18A3","B3","",""], "SWI":["","","","","","3F",""], "TAB":["","","","","","16",""], "TAP":["","","","","","06",""], "TBA":["","","","","","17",""], "TETS":["","","","","","00",""], "TPA":["","","","","","07",""], "TST":["","","6D","186D","7D","",""], "TSTA":["","","","","","4D",""], "TSTB":["","","","","","5D",""], "TSX":["","","","","","30",""], "TSY":["","","","","","1830",""], "TXS":["","","","","","35",""], "TYS":["","","","","","1835",""],"WAI":["","","","","","3E",""], "XGDX":["","","","","","8F",""], "XGDY":["","","","","","188F",""]}
 
# GLOBALES 
i=0
x=0
n = 0
END = 0
cadena_aux = ""
cadena_aux2 = ""
cadena_aux3 = ""
dic_var_EQU = {}
opCodeOperandoVar = ""
opCodeOperandoVar2 = ""
direccionMemVar = ""
ERRORES = False
HeRRoRRRReZVar = ""
var_const = []
op_op = []
lista = []
operando = ""
mnemonico = ""
modo_DIR = False  
caracteristicas_operando = []
sin_cero = False
contador_errores = 0
numeracion = ""

html_encabezado = '''

        <style>
        body {
          background-color: #fbf6f0;
          margin-left: 250px;
          margin-right: 250px;
          font-family: Verdana
        }

        h1 {
          color: #bb2205;
          text-align: center;
          font-family: Verdana;
        }

        h3 {
            font-weight: 600;
            text-align: center;
            font-family: Verdana;
        }

        span{
            font-weight: 600;
            text-align: justify;
            font-family: Verdana;
        }
        </style>
        <br><br>
        <h1 style = "color:#222831">Basile-Keller compilador MC68HC11</h1><br><br>
        <h1>Código Objeto: </h1>
        <h3 style = "color:#056674"> OpCode </h3>
        <h3 style = "color:#900d0d"> Operando </h3>
        <br><br><br><br>
'''
# REGEX
patronIMM = re.compile(r'^#[$][A-F0-9]{4}|#[$][A-F0-9]{2}$')
patronINDX = re.compile(r'^[$][A-F0-9]{2},[X]$')
patronINDY = re.compile(r'^[$][A-F0-9]{2},[Y]$')
patronDIR_REL = re.compile(r'^[$][A-F0-9]{2}$')
patronEXT = re.compile(r'^[$][A-F0-9]{4}$')
patronOPERANDO = re.compile(r'^[#]{0,1}[$]{0,1}[a-fA-F0-9]{1,4}$')

# CARACTERISTICAS DE VENTANA PRINCIPAL
root = Tk()
root.iconbitmap("Img\\mc68hc11.ico")
ancho = 684
alto = 434
root.title("Basile-Keller compilador MC68HC11")
root.resizable(0, 0)

# CARACTERISTICAS DE INTERFAZ GRAFICA
w = Canvas(root,width = ancho, height = alto, background = "black")
image = PhotoImage(file = "Img\\fondo1.gif")
background_label = Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w.pack()

s = Button(root, text = "Seleccionar archivo a compilar", font = ('Montserrat',11), foreground = 'black')
s.config(background = 'white')
s.pack()
s.place(relheight = 0.12, relwidth = 0.4, relx = 0.55 , rely = 0.1)

u = Button(root, text = "Compilar", font = ('Montserrat',11), foreground = 'black')
u.config(background = 'white')
u.pack()
u.place(relheight = 0.12, relwidth = 0.4, relx = 0.55 , rely = 0.3)

l = Label(root, text = "¡Compila para ver los resultados!", font = ('Montserrat', 11), foreground = 'black')
l.config(background = "white")
l.pack()
l.place(relheight = 0.4, relwidth = 0.4, relx = 0.55 , rely = 0.5)

def buscarArchivo():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Ensamblador","*.asc"),("all files","*.*")))
    if(root.filename==""):
        pass
    else:
        archivo.insert(0,root.filename)

def compilar():
    if (len(archivo)==0):
        print("Archivo no seleccionado")
        cambiarTexto2()
    else:
        print("Se está compilando el archivo: " + archivo[0])
        with open("archivos_generados\\compiladoHTML1.html", "w") as compiladoHTML:
            compiladoHTML.write(html_encabezado)
        with open(archivo[0],'r') as programa:

            contenido = programa.readlines()
            
            global x
            global i
            global n
            global END
            global lista
            global opCode
            global ERRORES
            global contador
            global operando
            global modo_DIR
            global mnemonico 
            global cadena_aux
            global cadena_aux2
            global cadena_aux3
            global dic_var_EQU
            global HeRRoRRRReZVar
            global direccionMemVar
            global opCodeOperandoVar
            global opCodeOperandoVar2
            global caracteristicas_operando
            global sin_cero
            global contador_errores
            global cadena_resumen_errores
            global numeracion

            i = 0
            x = 0
            n = 0
            m = 0
            END = 0
            op_op = []
            lista = []
            operando = ""
            mnemonico = ""
            var_const = []
            dic_var_EQU = {}
            cadena_aux = ""
            cadena_aux2 = ""
            cadena_aux3 = ""
            HeRRoRRRReZVar = ""
            cadena_codigoObjeto = ""
            cadena_resumen_errores = "RESUMEN DE ERRORES: \n\n\n\n"

            checksum_motorola = 0
            linea_16_motorola = ""
            longitudes_s19_motorola = []
            lista_contadora_motorola = []
            elementos_checksum_motorola = ""
            lista_aux_linea_16_motorola = []

            linea_16 = ""
            lista_contadora = []
            lista_aux_linea_16 = []

            
            for x in range(2):
                contador = "8000"
                inicio_s19 = "8000"
                contador_errores = 0
                inicio_s19_motorola = "8000"
                programa.seek(0,0)
                for linea in contenido:

                    opCode = ""
                    operando = ""
                    mnemonico = ""
                    ERRORES = False
                    cadena_aux2 = ""
                    modo_DIR  = False
                    direccionMemVar = ""
                    HeRRoRRRReZVar = ""
                    opCodeOperandoVar = ""
                    opCodeOperandoVar2 = ""
                    caracteristicas_operando = [0,0,0,0,0,0,0,0,0] # [0]->modo_IMM  [1]->hexa  [2]->decimal  [3]->ASCII  [4]->indx  [5]->indy  [6]->dic_var_EQU  [7]->len(operando)  [8]->modo_direccionamiento
                    

                    for caracter in linea:
                        cadena_aux2 += caracter

                    if cadena_aux2.startswith("*"):
                        direccionMem("")
                        opCodeOperando("")
                        pass
                    else:
                        pos = cadena_aux2.find("*")
                        cadena_aux3 = cadena_aux2[0:pos]
                        if (" EQU " or " EQu " or " Equ " or " EqU " or " eQu " or " eqU " or " eQU " or " equ ") in cadena_aux3:
                            var_const = cadena_aux3.split()
                            dic_var_EQU[var_const[0]] = var_const[2]
                            direccionMem("")
                            opCodeOperando2(var_const[2].lstrip("$"))
                        elif (" END " or " ENd " or " End " or " EnD " or " eNd " or " enD " or " eND " or " end ") in cadena_aux3:
                            END += 1
                        elif (" FCB " or " FCb " or " Fcb " or " FcB " or " fCb " or " fcB " or " fCB " or " fcb ") in cadena_aux3:
                            op_op = cadena_aux3.split()
                            for a in op_op:
                                if a == ("FCB" or " FCb " or " Fcb " or " FcB " or " fCb " or " fcB " or " fCB " or " fcb "):
                                    a = op_op.index(a)
                                    break


                            mnemonico = op_op[a].upper()
                            operando = op_op[a+1]
                            operandos = op_op[a+1].split(",")
                            operando = operandos[0]
                            trabajando_operando()
                            tmp = operando 
                            operando = operandos[1]
                            caracteristicas_operando[1] -= 1
                            trabajando_operando()
                            operando = tmp.lstrip("$") + operando.lstrip("$")
                            if a == 1: #CASO DEL RESET
                                dic_var_EQU[op_op[0]] = "$" + contador.lstrip("0x") 
                                direccionMem(contador.lstrip("$"))
                                opCodeOperando(operando)
                            else:
                                direccionMem(contador)
                                opCodeOperando(operando)
                            contador = suma_hex(contador, operando)


                        else:
                            op_op = cadena_aux3.split()


                            if len(op_op) == 0:
                                pass


                            elif len(op_op) == 1:
                                mnemonico = op_op[0]
                                if cadena_aux3.startswith(" "):
                                    if mnemonico.upper() in MNEMONICOS:
                                        mnemonico = mnemonico.upper()
                                        lista = MNEMONICOS.get(mnemonico)
                                        if lista[5] != "": 
                                            modo_direccionamiento_inherente()
                                        else: 
                                            HeRRoRRRReZ(5)
                                    else:
                                        HeRRoRRRReZ(4)
                                else:
                                    almacenar_etiquetas()
                                    

                            elif len(op_op) == 2:
                                if cadena_aux3.startswith(" "):
                                    if op_op[0].upper() == "ORG":
                                        mnemonico = op_op[0].upper()
                                        operando = op_op[1]
                                        trabajando_operando()
                                        contador = operando.lstrip("$")
                                        direccionMem("")
                                        opCodeOperando(contador)
                                        inicio_s19 = opCodeOperandoVar.rstrip(" ")
                                        inicio_s19_motorola = opCodeOperandoVar.rstrip(" ")
                                    buscando_mnemonico_dic_var_EQU(op_op[0])
                                    if mnemonico in MNEMONICOS:
                                        mnemonico = mnemonico.upper()
                                        operando = op_op[1]
                                        lista = MNEMONICOS.get(mnemonico)
                                        conociendo_modo_dir()
                                        if lista[6] != "":
                                            trabajando_operando()
                                            modo = 6
                                            opCode = lista[modo]
                                            modo_direccionamiento_relativo(hex(int(str(contador),16)+int(str(len(opCode)//2+1),16)))
                                        else:
                                            trabajando_operando()
                                            modo = encontrar_modo_dir(mnemonico)
                                            if modo == -1:
                                                if patronOPERANDO.search(operando):
                                                    print("error en el operando (no encontro regex)")
                                                    HeRRoRRRReZ(11)
                                                else:
                                                    if caracteristicas_operando[0] > 0:
                                                        operando = "#EE" #A MODO DE ERROR
                                                        HeRRoRRRReZ(2)
                                                    elif caracteristicas_operando[1] > 0:
                                                        operando = "$EE" #A MODO DE ERROR
                                                        HeRRoRRRReZ(1)
                                                    else:
                                                        operando = "$EE" #A MODO DE ERROR
                                                        HeRRoRRRReZ(3)
                                            else:
                                                opCode = lista[modo]                                       
                                        direccionMem(contador)
                                        op_code_operando = concat(opCode, operando)
                                        opCodeOperando(op_code_operando)
                                        contador = suma_hex(contador, op_code_operando)
                                else:
                                    HeRRoRRRReZ(9)


                            elif len(op_op) == 3:

                                if cadena_aux3.startswith(" "):
                                    buscando_mnemonico_dic_var_EQU(op_op[0])
                                    if mnemonico in MNEMONICOS:
                                        operando = op_op[1]
                                        if mnemonico == "BRSET" or mnemonico == "BRCLR":
                                            modo = modo_dir_exc()
                                            operando_intermedio = operando
                                            operando = op_op[2]
                                            lista = MNEMONICOS.get(mnemonico)
                                            opCode = lista[modo]                                            
                                            if operando in dic_var_EQU:
                                                operando = dic_var_EQU.get(operando)
                                                caracteristicas_operando[6] += 1
                                                modo_direccionamiento_relativo(hex(int(str(contador),16)+int(str(len(opCode)//2+3),16)))
                                            else:
                                                HeRRoRRRReZ(3)
                                                print("El segundo operando no es una etiqueta")
                                                operando = "$EE" #A MODO DE ERROR
                                            direccionMem(contador)
                                            op_code_operando = concat(opCode,operando_intermedio)
                                            op_code_operando = concat(op_code_operando,operando)
                                            opCodeOperando(op_code_operando)
                                            contador = suma_hex(contador, op_code_operando)
                                                        
                                        else:
                                            HeRRoRRRReZ(7)
                                else:
                                    HeRRoRRRReZ(9)
                            else:
                                HeRRoRRRReZ(11) 

                    if x == 1:
                        n += 1
                    if x == 1 and END == 0:
                        sin_cero = True
                        END += 1

                    if sin_cero == True and n == len(contenido):
                        HeRRoRRRReZ(10)
                    impresion_a_color()
                    numeracionfun()

                    ############################################################
                    #IMPRESION RESUMEN_ERRORES.TXT
                    if contador_errores > 0 and ERRORES == True:
                        cadena_resumen_errores += numeracion
                        cadena_resumen_errores += direccionMemVar
                        cadena_resumen_errores += opCodeOperandoVar
                        cadena_resumen_errores += cadena_aux2
                        cadena_resumen_errores += HeRRoRRRReZVar
                    ############################################################

                    ############################################################
                    #IMPRESION COMPILADO.LST
                    if ERRORES == False:
                        cadena_aux += numeracion 
                        cadena_aux += direccionMemVar
                        if (" EQU " or " EQu " or " Equ " or " EqU " or " eQu " or " eqU " or " eQU " or " equ ") in cadena_aux3:
                            cadena_aux += opCodeOperandoVar2
                        else:
                            cadena_aux += opCodeOperandoVar
                        cadena_aux += cadena_aux2
                    else: 
                        cadena_aux += numeracion
                        cadena_aux += direccionMemVar
                        cadena_aux += opCodeOperandoVar
                        cadena_aux += cadena_aux2
                        cadena_aux += HeRRoRRRReZVar

                    cadena_aux.split('\n')
                    if x == 0:
                        cadena_aux = ""
                        cadena_codigoObjeto = ""
                        cadena_codigoObjeto_motorola = ""
                    #############################################################

                    #############################################################
                    # IMPRESION CODIGOOBJETO.S19
                    if END > 0:
                        opCodeOperandoVar = opCodeOperandoVar.rstrip(" ")
                        if mnemonico == "ORG":                                          #Cambio en contador
                            if (len(linea_16)+len(opCodeOperandoVar)) == 32:                   
                                lista_contadora.append(inicio_s19.lstrip("0x").upper())
                                linea_16 += opCodeOperandoVar
                                lista_aux_linea_16.append(linea_16)
                                linea_16 = ""
                            elif (len(linea_16)+len(opCodeOperandoVar)) > 32:
                                lista_contadora.append(inicio_s19.lstrip("0x").upper())
                                while(len(linea_16)<32):
                                    linea_16 += opCodeOperandoVar[0]
                                    opCodeOperandoVar = opCodeOperandoVar[1:]
                                lista_aux_linea_16.append(linea_16)
                                linea_16 = ""
                                linea_16 = opCodeOperandoVar
                            else:
                                lista_contadora.append(inicio_s19.lstrip("0x").upper())
                                lista_aux_linea_16.append(linea_16)
                                linea_16 = ""
                        else:                                                           #Contador suma automática
                            if (len(linea_16)+len(opCodeOperandoVar)) == 32:
                                inicio_s19 = str(hex(int(inicio_s19,16)+16))                    
                                lista_contadora.append(inicio_s19.lstrip("0x").upper())
                                linea_16 += opCodeOperandoVar
                                lista_aux_linea_16.append(linea_16)
                                linea_16 = ""
                            elif (len(linea_16)+len(opCodeOperandoVar)) > 32:
                                inicio_s19 = str(hex(int(inicio_s19,16)+16))
                                lista_contadora.append(inicio_s19.lstrip("0x").upper())
                                while(len(linea_16)<32):
                                    linea_16 += opCodeOperandoVar[0]
                                    opCodeOperandoVar = opCodeOperandoVar[1:]
                                lista_aux_linea_16.append(linea_16)
                                linea_16 = ""
                                linea_16 = opCodeOperandoVar
                            else:
                                linea_16 += opCodeOperandoVar
                    #############################################################

                    #############################################################
                    # IMPRESION CODIGOOBJETOMOTOROLA.S19 
                    if END > 0:
                        opCodeOperandoVar = opCodeOperandoVar.rstrip(" ")
                        if mnemonico == "ORG":                                          #Cambio en contador
                            if (len(linea_16_motorola)+len(opCodeOperandoVar)) == 60:                   
                                lista_contadora_motorola.append(inicio_s19_motorola.lstrip("0x").upper())
                                linea_16_motorola += opCodeOperandoVar
                                lista_aux_linea_16_motorola.append(linea_16_motorola)
                                linea_16_motorola = ""
                                longitudes_s19_motorola.append(str(21))
                            elif (len(linea_16_motorola)+len(opCodeOperandoVar)) > 60:
                                lista_contadora_motorola.append(inicio_s19_motorola.lstrip("0x").upper())
                                while(len(linea_16_motorola)<60):
                                    linea_16_motorola += opCodeOperandoVar[0]
                                    opCodeOperandoVar = opCodeOperandoVar[1:]
                                lista_aux_linea_16_motorola.append(linea_16_motorola)
                                linea_16_motorola = ""
                                linea_16_motorola = opCodeOperandoVar
                                longitudes_s19_motorola.append(str(21))
                            else:
                                lista_contadora_motorola.append(inicio_s19_motorola.lstrip("0x").upper())
                                lista_aux_linea_16_motorola.append(linea_16_motorola)
                                if len(linea_16_motorola) != 0:
                                    longitudes_s19_motorola.append(str(str(hex(len(linea_16_motorola)//2+3)).lstrip("0x").upper()))
                                linea_16_motorola = ""
                        else:                                                           #Contador suma automática
                            if (len(linea_16_motorola)+len(opCodeOperandoVar)) == 60:
                                inicio_s19_motorola = str(hex(int(inicio_s19_motorola,16)+30))                    
                                lista_contadora_motorola.append(inicio_s19_motorola.lstrip("0x").upper())
                                linea_16_motorola += opCodeOperandoVar
                                lista_aux_linea_16_motorola.append(linea_16_motorola)
                                linea_16_motorola = ""
                                longitudes_s19_motorola.append(str(21))
                            elif (len(linea_16_motorola)+len(opCodeOperandoVar)) > 60:
                                inicio_s19_motorola = str(hex(int(inicio_s19_motorola,16)+30))
                                lista_contadora_motorola.append(inicio_s19_motorola.lstrip("0x").upper())
                                while(len(linea_16_motorola)<60):
                                    linea_16_motorola += opCodeOperandoVar[0]
                                    opCodeOperandoVar = opCodeOperandoVar[1:]
                                lista_aux_linea_16_motorola.append(linea_16_motorola)
                                linea_16_motorola = ""
                                linea_16_motorola = opCodeOperandoVar
                                longitudes_s19_motorola.append(str(21))
                            else:
                                linea_16_motorola += opCodeOperandoVar
                    ###############################################################

            ########################################################################
            #IMPRESION FINAL RESUMEN_ERRORES.TXT
            cadena_resumen_errores += "\n\n\n\n" + "        TOTAL ERRORS=    " + str(contador_errores)
            ########################################################################

            ########################################################################
            #IMPRESION FINAL COMPILADO.LST
            cadena_aux += "\n\n\n\n" + "        TOTAL ERRORS=    " + str(contador_errores) 
            cadena_aux += "\n\n\n\n" + "        " + "SYMBOL TABLE:     "  
            cadena_aux += "\n\n" + "        Total Entries=    " + str(len(dic_var_EQU)) + "\n\n\n"

            for y in sorted(dic_var_EQU):
                cadena_aux += "     " + y 
                a = 20
                a -= len(y)
                if len(y)<20:
                    while a!=0:
                        cadena_aux += " "
                        a -= 1
                cadena_aux += dic_var_EQU.get(y) + "\n"
            #########################################################################

            #########################################################################
            # IMPRESION FINAL CODIGOOBJETO.S19
            lista_aux_linea_16.append("")
            for j in range(len(lista_contadora)):
                if lista_aux_linea_16[j+1] != "":
                    cadena_codigoObjeto += "<" + lista_contadora[j] + "> " + lista_aux_linea_16[j+1] + "\n"
            #########################################################################

            #########################################################################
            # IMPRESION FINAL CODIGOOBJETOMOTOROLA.S19
            lista_aux_linea_16_motorola.append("")
            longitudes_s19_motorola.append(str(str(hex(len(linea_16_motorola)//2+3)).lstrip("0x").upper()))
            for j in range(len(longitudes_s19_motorola)):
                if len(longitudes_s19_motorola[j]) == 1:
                    longitudes_s19_motorola[j] = "0" + longitudes_s19_motorola[j]
            for j in range(len(lista_contadora_motorola)):
                if lista_aux_linea_16_motorola[j+1] != "":
                    elementos_checksum_motorola = longitudes_s19_motorola[j] + lista_contadora_motorola[j] + lista_aux_linea_16_motorola[j+1]
                    checksum_motorola = 0
                    while m < len(elementos_checksum_motorola): 
                        checksum_motorola = hex(int(str(elementos_checksum_motorola[:2]),16) + int(str(checksum_motorola),16))
                        elementos_checksum_motorola = elementos_checksum_motorola[2:]
                    checksum_motorola = complemento1(checksum_motorola)
                    checksum_motorola = checksum_motorola[-2:].lstrip("0x").upper()
                    if len(checksum_motorola) == 1:
                    	checksum_motorola = "0" + checksum_motorola
                    cadena_codigoObjeto_motorola += "S1 " + longitudes_s19_motorola[j] + " " + lista_contadora_motorola[j] + " " + lista_aux_linea_16_motorola[j+1] + " " + checksum_motorola + "\n"
            cadena_codigoObjeto_motorola += "S9 03 8000 7C"
            ##########################################################################

            ##########################################################################
            #CREACIÓN Y ESCRITURA DE ARCHIVOS
            with open("archivos_generados\\compilado.lst","w") as compilado:
                compilado.writelines(cadena_aux)

            with open("archivos_generados\\codigoObjeto.s19", "w") as codigoObjeto:
                codigoObjeto.writelines(cadena_codigoObjeto)

            with open("archivos_generados\\codigoObjetoMotorola.s19", "w") as codigoObjetoMotorola:
                codigoObjetoMotorola.writelines(cadena_codigoObjeto_motorola)

            with open("archivos_generados\\resumen_errores.txt", "w") as resumen_errores:
                resumen_errores.writelines(cadena_resumen_errores)
            ##########################################################################

            cambiarTexto()

def complemento1(a):
	a = bin(int(a,16))
	a = a.lstrip("0b")
	a_complemento = ""
	for k in range(len(a)):
		if a[k] == "0":
			a_complemento += "1"
		else:
			a_complemento += "0"
	a = hex(int(a_complemento,2))
	return a

def cambiarTexto():
    global contador_errores
    global dic_var_EQU
    l.config(text = "Compilado con éxito.\n\nSe crearon los archivos:\n'compilado.lst'\n'codigoObjeto.s19'\n'codigoObjetoMotorola.s19'\n'compiladoHTML1.html'\n'resumen_errores.txt'\n\n No. errores:  " + str(contador_errores) + "   No. entradas: " + str(len(dic_var_EQU)), font = ("Montserrat",9))

def cambiarTexto2():
    l.config(text = "¡No has escogido un archivo!")                

def impresion_a_color():
    global operando
    global mnemonico
    global opCode
    html=""
    with open("archivos_generados\\compiladoHTML1.html", "a") as compiladoHTML:

        if operando != "" and END>=1 and mnemonico != "ORG":
            operando = operando.lstrip("#")
            operando = operando.lstrip("$")
            operando = operando.lstrip("#$")
            html += """
             <span style = "color: #056674">{opCode}</span><span style = "color:#900d0d"> {operando}</span>

            """.format(opCode=opCode, operando=operando)
            compiladoHTML.write(html)   
        else:
            pass 

def numeracionfun():
    global i
    global x
    global numeracion
    numeracion = ""
    if x == 1 or x == 2:
        i+=1
        if i<10:
            numeracion += "   " + str(i)
        elif i<100:
            numeracion += "  " + str(i)
        elif i<1000:
            numeracion += " " + str(i)
        else:
            numeracion += str(i)
        numeracion += ' | '

def direccionMem(a):
    global cadena_aux
    global direccionMemVar
    a = a.lstrip("$")
    a = a.lstrip("0x")
    if a == "":
        direccionMemVar += "     "
    else:
        direccionMemVar += a + " "

def opCodeOperando(a):
    global cadena_aux
    global opCodeOperandoVar   
    b = 11
    b -= len(a)
    opCodeOperandoVar += a
    while b!=0:
        opCodeOperandoVar += " "
        b -= 1

def opCodeOperando2(a):
    global cadena_aux
    global opCodeOperandoVar2    
    b = 11
    b -= len(a)
    opCodeOperandoVar2 += a
    while b!=0:
        opCodeOperandoVar2 += " "
        b -= 1

def verificar_ceros():
    global operando
    global caracteristicas_operando
    if len(operando) == 4 or len(operando) == 2:
        if caracteristicas_operando[0] == 1:
            operando = "#$" + operando
        else:
            operando = "$" + operando
    elif len(operando) == 1 or len(operando) == 3:
        if caracteristicas_operando[0] == 1:
            operando = "#$0" + operando
        else:
            operando = "$0" + operando
    elif len(operando) == 0:
        if caracteristicas_operando[0] == 1:
            operando = "#$00"
        else:
            operando = "$00"
    else:
        HeRRoRRRReZ(7)

def buscando_mnemonico_dic_var_EQU(buscando):
    global dic_var_EQU
    global mnemonico
    global MNEMONICOS
    global opCode
    temp = buscando
    mnemonico = buscando
    while mnemonico not in MNEMONICOS and mnemonico.upper() != ("ORG" or "END" or "FCB" or "EQU"):
        if mnemonico.upper() in MNEMONICOS:
            mnemonico = mnemonico.upper()
        else:
            buscando = dic_var_EQU.get(buscando)
            if buscando != None:
                mnemonico = buscando
            else:
                mnemonico = temp
                HeRRoRRRReZ(4)
                break

def obteniendo_caracteristicas_operando():
    global operando   
    global caracteristicas_operando

    if operando.startswith("#"):
        operando = operando.lstrip("#")
        caracteristicas_operando[0] += 1

    if operando.startswith("$"):
        operando = operando.lstrip("$")
        caracteristicas_operando[1] += 1
    else:
        caracteristicas_operando[2] += 1

    if operando.startswith("'"):
        operando = operando.lstrip("'")
        operando = hex(ord(operando))
        operando = operando.lstrip("0x").upper()
        caracteristicas_operando[1] += 1
        caracteristicas_operando[3] += 1

    if operando.endswith(",X") or operando.endswith(",x"):
        operando = operando.rstrip(",X")
        operando = operando.rstrip(",x")
        caracteristicas_operando[4] += 1

    if operando.endswith(",Y") or operando.endswith(",y"):
        operando = operando.rstrip(",Y")
        operando = operando.rstrip(",y")
        caracteristicas_operando[5] += 1  
     
def trabajando_operando():
    global dic_var_EQU
    global END
    global operando   
    global mnemonico
    global lista
    global modo_DIR
    global caracteristicas_operando # [0]->modo_IMM  [1]->hexa  [2]->decimal  [3]->ASCII  [4]->indx  [5]->indy  [6]->dic_var_EQU  [7]->len(operando)
    
    lista = MNEMONICOS.get(mnemonico)
    obteniendo_caracteristicas_operando()
    if operando in dic_var_EQU:
        operando = dic_var_EQU.get(operando)
        caracteristicas_operando[6] += 1
        trabajando_operando()
    else:
        if mnemonico == ("BSET" or "BCLR" or "BRSET" or "BRCLR"): #CUATRO EXCEPCIONES
            pass
        elif caracteristicas_operando[1] == 1:                                          # ESTÁ EN HEXADECIMAL
            if caracteristicas_operando[0] == 1:                                            # ES MODO IMM
                verificar_ceros()                                                           
            elif caracteristicas_operando[0] == 0:                                          # ES MODO DIR, EXT, INDX, INDY
                if modo_DIR == True:                                                            #PARA MODO DIR, PASAR OPERANDO A 1 BYTE
                    if len(operando) != 2 and operando.startswith("00"):
                        operando = operando.lstrip("00")
                    verificar_ceros()
                else:                                                                       # ENVÍA MODO EXT, INDX, INDY
                    verificar_ceros()
            else:
                print("Error en el operando, exceso de #")
        elif caracteristicas_operando[1] == 0:                                          # ESTÁ EN DECIMAL, CONVERTIR A HEXADECIMAL
            if caracteristicas_operando[0] == 1:                                            # ES MODO IMM
                try:
                    operando = str(hex(int(operando)))
                    operando = hex(operando).lstrip("0x")
                    verificar_ceros()
                except Exception:
                    pass
            elif caracteristicas_operando[0] == 0:                                          # ES MODO DIR, EXT, INDX, INDY
                try:
                    operando = str(hex(int(operando)))
                    operando = hex(operando).lstrip("0x")
                    verificar_ceros()
                except Exception:
                    if mnemonico in MNEMONICOS and END==0:
                        if lista[4] != "":          
                            operando = "0000"
                            verificar_ceros()
                        elif lista[6] != "":      
                            operando =  "00"
                            verificar_ceros()
            else:
                print("Error en el operando, exceso de #")
        else:
            print("Error en el operando, exceso de $")

def conociendo_modo_dir():
    global lista
    global modo_DIR
    if lista[1] != "": #Tiene #
        modo_DIR = True
        caracteristicas_operando[8] == 1

def encontrar_modo_dir(mnemonico):
    global caracteristicas_operando
    global operando
    modo = -1
    num_comas_op = operando.count(",")
    lista = MNEMONICOS.get(mnemonico)
    if mnemonico == "BCLR" or mnemonico == "BSET":
        modo = modo_dir_exc()
    elif lista[5] != "" and caracteristicas_operando[4] == 0 and caracteristicas_operando[5] == 0:
        HeRRoRRRReZ(6)
    elif patronIMM.search(operando) and num_comas_op == 0 and lista[0]!= "":  
        modo = 0
    elif caracteristicas_operando[4] == 1 and patronINDX.search(operando+",X"):
        modo = 2
    elif caracteristicas_operando[5] == 1 and patronINDY.search(operando+",Y"):
        modo = 3        
    elif patronDIR_REL.search(operando) and num_comas_op == 0 and lista[1]!= "":
        lista = MNEMONICOS.get(mnemonico)
        if lista[1] != "":
            modo = 1
    elif len(operando)==3:
        operando = operando.lstrip("$")
        operando = "$00" + operando
        if patronEXT.search(operando) and num_comas_op == 0 and lista[4]!= "": 
            modo = 4
    elif patronEXT.search(operando) and num_comas_op == 0 and lista[4]!= "":
        modo = 4
    return modo

def almacenar_etiquetas():
    global dic_var_EQU
    global mnemonico
    global contador
    dic_var_EQU[mnemonico] = "$" + contador.lstrip("0x")
    direccionMem(contador)
    opCodeOperando("")    

def modo_direccionamiento_inherente():
    global opCode
    global lista
    global contador
    opCode = lista[5]
    direccionMem(contador)
    opCodeOperando(opCode)
    contador = suma_hex(contador, opCode)

def suma_hex(a, b):
    if "$" in a:
        a = a.lstrip("$")
    if "#" in b:
        b = b.lstrip("#")
    if "$" in b:
        b = b.lstrip("$")
    resultado = hex(int(str(a),16)+int(str(len(str(b))//2),16))
    return resultado.lstrip("0x").upper()
    

def concat(a,b):
    if "$" in a:
        a = a.lstrip("$")
    if "#" in b:
        b = b.lstrip("#")
    if "$" in b:
        b = b.lstrip("$")
    if ",Y" in b:
        b = b.rstrip(",Y")
    if ",X" in b:
        b = b.rstrip(",X")
    resultado = str(a)+str(b)
    return resultado.upper()

def modo_direccionamiento_relativo(a):
    global operando
    global mnemonico
    global x
    if x == 0:
        operando = "$00"
    else:
        a = a.lstrip("0x")
        operando = operando.lstrip("$")
        resultado = -1
        if hex(int(str(a),16))>hex(int(str(operando),16)):
            resultado = hex(int(str(operando),16)-int(str(a),16))
            resultado = hex(int("100",16)+int(resultado.lstrip("0x"),16))
            if int(str(resultado),16) > 256 or int(str(resultado),16) < 129:
                HeRRoRRRReZ(8)
        elif hex(int(str(a),16))<hex(int(str(operando),16)):
            resultado = hex(int(str(operando),16)-int(str(a),16))
            if int(str(resultado),16) > 128 or int(str(resultado),16) < 0:
                HeRRoRRRReZ(8)
        else:
            # print("Son iguales")
            pass
        resultado = resultado.lstrip("0x").upper()
        if caracteristicas_operando[6] == 0:  
            HeRRoRRRReZ(3)
        if len(resultado) == 1:
            resultado = "0" + resultado
        operando = "$" + resultado    

def modo_dir_exc():    
    global operando
    modo = -1
    if "X" in operando:
        modo = 2
        operando = operando.lstrip("$")
        operandos = operando.split(",X,#$")  
        operando = operandos[0] + operandos[1]
    elif "Y" in operando:
        modo = 3
        operando = operando.lstrip("$")
        operandos = operando.split(",Y,#$")
        operando = operandos[0] + operandos[1]
    else:
        modo = 1
        operando = operando.lstrip("$")
        operandos = operando.split(",#$")
        operando = operandos[0] + operandos[1]
    return modo


def HeRRoRRRReZ(codigo_error):
    global cadena_aux
    global HeRRoRRRReZVar
    global ERRORES
    global END
    global contador_errores
    ERRORES = True
    switcher={
        1: "E       ^ 001 Constante inexistente \n",
        2: "E       ^ 002 Variable inexistente \n",
        3: "E       ^ 003 Etiqueta inexistente \n",
        4: "E       ^ 004 Mnemónico inexistente \n",
        5: "E       ^ 005 Instrucción carece de operando(s) \n",
        6: "E       ^ 006 Instrucción no lleva operando(s) \n",
        7: "E       ^ 007 Magnitud de operando erronea \n",
        8: "E       ^ 008 Salto relativo muy lejano \n",
        9: "E       ^ 009 Instrucción carece de al menos un espacio relativo al margen \n",
        10: "E       ^ 010 No se encuentra END \n"
    }
    HeRRoRRRReZVar += switcher.get(codigo_error, "E       ^ Error 011 \n")
    if END > 0:
        contador_errores += 1
        # print(switcher.get(codigo_error, "E       ^ Error 011 \n"))

u.config(command = compilar)
s.config(command = buscarArchivo)
mainloop()