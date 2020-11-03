#VERSION 1
# PERMITE SELECCIONAR UNICAMENTE ARCHIVOS DE TIPO .ASC, LOS GUARDA EN UNA LISTA LLAMADA "ARCHIVO" Y ALLI, EN CASO DE QUE NO SE ESCOJA UN NUEVO 
# ARCHIVO SE SEGUIRA COMPILANDO EL QUE FUE ESCOGIDO PREVIAMENTE. SI NO SE ESCOGE NADA O POR ALGUNA RAZON DEL DESTINO QUE NO SE COMO SUCEDERIA PERO SE ESCOJE
# UN ARCHIVO QUE NO SEA .asc ENTONCES ENVIARA UN MENSAJE QUE EL ARCHIVO ES INVALIDO


from tkinter import filedialog
from tkinter import *
import os
from PIL import Image, ImageTk
import shutil




# VARIABLES Y CONSTANTES GLOBALES (AQUI INCLUIR MNEMOTECNICOS Y LISTAS)
archivo = []

IMM={"ADCA":"89", "ADCB":"C9", "ADDA":"8B", "ADDB":"CB", "ADDD":"C3", "ANDA":"84", "ANDB":"C4", "BITA":"85", "BITB":"C5", "CMPA":"81", "CMPB":"C1", "CPD":"1A83", "CPX":"8C", "CPY":"188C", "EORA":"88", "EORB":"C8", "LDAA":"86"}

DIR={"ADCA":"99", "ADCB":"D9", "ADDA":"9B", "ADDB":"DB", "ADDD":"D3", "ANDA":"94", "ANDB":"D4", "BCLR":"15", "BITA":"95", "BITB":"D5", "BRCLR":"13", "BRSET":"12", "BSET":"14", "CMPA":"91", "CMPB":"D1", "CPD":"1A93", "CPX":"9C", "CPY":"189C", "EORA":"98", "EORB":"D8", "JSR":"9D", "LDAA":"96"}

INDX={"ADCA":"A9", "ADCB":"E9", "ADDA":"AB", "ADDB":"EB", "ADDD":"E3", "ANDA":"B4", "ANDB":"E4", "ASL":"68", "ASR":"67", "BCLR":"1D", "BITA":"A5", "BITB":"E5", "BRCLR":"1F", "BRSET":"1E", "BSET":"1C", "CLR":"6F", "CMPA":"A1", "CMPB":"E1", "COM":"63", "CPD":"1AA3", "CPX":"AC", "CPY":"1AAC", "DEC":"6A", "EORA":"A8", "EORB":"E8", "INC":"6C", "JMP":"6E", "JSR":"AD", "LDAA":"A6"}

INDY={"ADCA":"18A9", "ADCB":"18E9", "ADDA":"18AB", "ADDB":"18EB", "ADDD":"18E3", "ANDA":"18A4", "ANDB":"18E4", "ASL":"1868", "ASR":"1867", "BCLR":"181D", "BITA":"18A5", "BITB":"18E5", "BRCLR":"181F", "BRSET":"181E", "BSET":"181C", "CLR":"186F", "CMPA":"18A1", "CMPB":"18E1", "COM":"1863", "CPD":"CDA3", "CPX":"CDAC", "CPY":"18AC", "DEC":"186A", "EORA":"18A8", "EORB":"18E8", "INC":"186C", "JMP":"186E", "JSR":"18AD", "LDAA":"18A6"}

EXT={"ADCA":"B9", "ADCB":"F9", "ADDA":"BB", "ADDB":"FB", "ADDD":"F3", "ANDA":"B4", "ANDB":"F4", "ASL":"78", "ASR":"77", "BITA":"B5", "BITB":"F5", "CLR":"7F", "CMPA":"B1", "CMPB":"F1", "COM":"73", "CPD":"1AB3", "CPX":"BC", "CPY":"18BC", "DEC":"7A", "EORA":"B8", "EORB":"F8", "INC":"7C", "JMP":"7E", "JSR":"BD", "LDAA":"B6"}

INH={"ABA":"1B", "ABX":"3A", "ABY":"183A", "ASLA":"48", "ASLB":"58", "ASLD":"5", "ASRA":"47", "ASRB":"57", "CBA":"11", "CLC":"0C", "CLI":"0E", "CLRA":"4F", "CLRB":"5F", "CLV":"0A", "COMA":"43", "COMB":"53", "DAA":"19", "DECA":"4A", "DECB":"5A", "DES":"34", "DEX":"09", "DEY":"1809", "FDIV":"03", "IDIV":"02", "INCA":"4C", "INCB":"5C", "INS":"31", "INX":"08", "INY":"1808"}

REL={"BCC":"24", "BCS":"25", "BEQ":"27", "BGE":"2C", "BGT":"2E", "BHI":"22", "BHS":"24", "BLE":"2F", "BLO":"25", "BLS":"23", "BLT":"2D", "BMI":"2B", "BNE":"26", "BPL":"2A", "BRA":"20", "BRN":"21", "BSR":"8D", "BVC":"28", "BVS":"29"}

#CARACTERISTICAS DE VENTANA PRINCIPAL
root = Tk()
root.iconbitmap("C:\\Users\\andre\\Desktop\\MC68HC11\\COMPILADOR\\mc68hc11.ico")
ancho = 684
alto = 434
root.title("Basile-Keller compilador MC68HC11")
root.resizable(0, 0)


#
#ESTO SE PUEDE ELIMINAR  
#
# top = Toplevel()
# fondo = PhotoImage(file = "C:\\Users\\andre\\Desktop\\Programacion\\Python\\Python3Nuevo\\CombinarPDFsFINAL\\JuntarPDFs grafico\\fondo2.gif")
# fondo_label = Label(top, image = fondo)
# fondo_label.place(x=0, y=0,relheight = 1, relwidth=1)
# top.config(bg = 'black',)
# top.geometry("600x450")
# top.iconbitmap("C:\\Users\\andre\\Desktop\\Programacion\\Python\\Python3Nuevo\\CombinarPDFsFINAL\\JuntarPDFs grafico\\klimt.ico")
# top.title("Archivos Seleccionados")

"""scrollbary = Scrollbar(top)
scrollbary.pack(side = RIGHT,fill = Y)
scrollbarx = Scrollbar(top)
scrollbarx.pack(side = BOTTOM, fill= X)
"""

"""
AGREGAR EN FUNCION BUSCAR PDF
D.config(yscrollcommand=scrollbary.set)
				scrollbary.config(command = D.yview)
				D.config(xscrollcommand=scrollbarx.set)
				scrollbarx.config(command = D.xview)"""


"""def cambiarTamanio(event):

	new_width = event.width
	new_height = event.height
	image = copy_of_image.resize((new_width,new_height))
	photo = ImageTk.PhotoImage(image)
	label.config(image = photo)
	label.image = photo
"""
#

# CARACTERISTICAS DE INTERFAZ GRAFICA
w = Canvas(root,width = ancho, height = alto, background = "black")
image = PhotoImage(file = "C:\\Users\\andre\\Desktop\\\\MC68HC11\\COMPILADOR\\fondo1.gif")
#copy_of_image = image.copy()
#photo = PhotoImage(image)
background_label = Label(root, image=image)
#background_label.bind('<Configure>',cambiarTamanio)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
w.pack()

s = Button(root, text = "Seleccionar archivo a compilar", font = ('Montserrat',11), foreground = 'black')
s.config(background = 'white')
s.pack()
s.place(relheight = 0.12, relwidth = 0.4, relx = 0.55 , rely = 0.3)

u = Button(root, text = "Compilar", font = ('Montserrat',11), foreground = 'black')
u.config(background = 'white')
u.pack()
u.place(relheight = 0.12, relwidth = 0.4, relx = 0.55 , rely = 0.5)
# CARACTERISTICAS DE INTERFAZ GRAFICA

def buscarArchivo():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Ensamblador","*.asc"),("all files","*.*")))
	if(root.filename==""):
		pass
	else:
		archivo.insert(0,root.filename)
	# lista_PDFS.append(root.filename)
	# D = Listbox(top)
	# D.config(bg = 'black', font = 'Serif', fg = 'white', highlightthickness = 0, selectbackground = 'black', width = 55)
	# i = 1
	# for x in lista_PDFS:
	# 	D.insert(i,x)
	# 	i+=1
	# D.pack()
	# D.place(relx = 0.1, rely = 0.17)


def compilar():
	if (len(archivo)==0):
		print("archivo no escogido bla bla bla ")
	else:
		print("aqui estariamos compilando el archivo de nombre " + archivo[0])
		with open(archivo[0],'r') as programa:

			contenido = programa.readlines()
			
			dic_var_EQU = {}
			
			cadena_aux = ""
			cadena_aux2 = ""

			lista_aux = []
			lista_aux2 = []
			lista_aux3 = []

			dev_op = []

			
			
			#SEPARACION DE ELEMENTOS DEL PROGRAMA EN LISTA
			#ELIMINACION DE COMENTARIOS *

			for linea in contenido:
				for caracter in linea:
					caracter = caracter.upper()
					if caracter == "*":
						lista_aux.append("\n")
						break
					else:
						lista_aux.append(caracter)

			for elemento in lista_aux:
				cadena_aux += elemento
			
			lista_aux.clear()
			lista_aux = cadena_aux.split("\n")	
			print(lista_aux)
			

			#DICCIONARIO CON VARIABLES EQU

			for linea in contenido:
				if "EQU" in linea:
					lista_aux2 = linea.split()
					dic_var_EQU[lista_aux2[0].upper()] = lista_aux2[2].upper()
			print("\n\n\n\n\n\n\n")
			print(dic_var_EQU)


			for elemento in lista_aux:
				dev_op.append(devOp(elemento))
			for x in dev_op:
				if len(x)==0 or x == "":
					dev_op.remove(x)
			print(dev_op)


		# i = 0
		# for elemento in lista_aux:
		# 	for caracter in elemento:
		# 		if caracter == " " and i!=1:
		# 			pass
		# 		else:
		# 			if caracter == " ":
		# 				pass
		# 			i = 1
		# 			lista_aux3.append(caracter)
		# for elemento in lista_aux3:
		# 	cadena_aux2 += elemento
		# print(cadena_aux2)



def devOp(a):
	b = []
	b = a.split()
	return b

# def estaHexa(op):
# 	if op.startswith("$"):
# 		return op
# 	else:
# 		hex(op)

# def unirPDF():

# 	path = "C:\\Users\\andre\\Desktop\\BASILE_PDF"

# 	try:
# 		os.mkdir(path)
# 	except OSError:
# 		print("Creation of the directory %s failed" % path)
# 	else:
# 		print("Successfully created the directory %s " % path)

	
# 	for x in lista_PDFS:
# 		copiar = 'C:\\Users\\andre\\Desktop\\BASILE_PDF'
# 		shutil.copy(x, copiar)

# 	pdfFinal = []

# 	for archivo in os.listdir(path):
# 		if archivo.endswith('.pdf'):
# 			pdfFinal.append(archivo)

# 	escritor = PyPDF2.PdfFileWriter()

# 	for archivo in pdfFinal:
# 		obj = open(path + "/" + archivo, 'rb')
# 		lector = PyPDF2.PdfFileReader(obj)
# 		for numPagina in range(0, lector.numPages):
# 			pgo = lector.getPage(numPagina)
# 			escritor.addPage(pgo)

# 	archivoFinal = open(path + "/" + 'PDF_RESULTANTE.pdf','wb')
# 	escritor.write(archivoFinal)
# 	archivoFinal.close()

# 	print("Se guard[o] el resultado con el nombre PDF_RESULTANTE en la misma carpeta en"
# 		  "donde se estaba trabajando")





	

u.config(command = compilar)
s.config(command = buscarArchivo)

mainloop()