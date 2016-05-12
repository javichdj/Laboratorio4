#frase=input("INGRESE UNA FRASE POR FAVOR: ")
#print("Numero de palabras: " + str(len(frase.split(" "))))
def openread():
	f=open("frasepr.txt","w")
	f.write('Esto es una prueba\n')
	f.close()
	
def leer ():
	f=open("frasepr.txt")
	linea=f.readline()
	print("Numero de palabras: " + str(len(linea.split(" "))))

openread()
leer()