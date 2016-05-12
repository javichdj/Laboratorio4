def read ():
	f=open("texto.txt")
	linea=f.readline()
	print("Numero de palabras: " + str(len(linea.split(" "))))


read()