print ("HOLA SOY JAZMIN")
a=float(input("INGRESE SU ESTATURA(en m): "))
b=float(input("INGRESE SU PESO(en kg): "))

def indice_mm ():
	indice=b/(a*a)
	return indice

resp=indice_mm()
print("Su indice de masa corporal es: "+str(round(resp,2)))

if(resp<18):		
	print ("SU PESO ESTA POR DEBAJO DEL PROMEDIO")
if(resp>=18 and resp<=24.9):
	print ("SU PESO ES NORMAL")
if(resp>=25 and resp<=26.9):
	print ("UD TIENE SOBREPESO \n")
	print ("PARECES CHANCHITO")
if(resp>=27):
	print ("UD TIENE OBESIDAD")
