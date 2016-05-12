def read ():
	f=open("frasepr.txt")
	linea=f.readline()
	print("Numero de palabras: " + str(len(linea.split(" "))))


read()