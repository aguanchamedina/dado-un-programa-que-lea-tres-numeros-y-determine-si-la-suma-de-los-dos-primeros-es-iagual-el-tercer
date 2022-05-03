"""programa para determinar si dado 
tres numeros enteros la suma de los dos primeros es igual al tres""" 

print("----------------------------------------------")
print("----------SI_DADO_TRES_NUMEROS_ENTEROS--------")
print("----------------------------------------------")

#input

X = int(input("ingresa el primer valor:"))
Y = int(input("ingresa el segundo valor:"))
Z = int(input("ingresa el tercer valor:"))

#Procesinng
if Z == X + Y:
    msg = print("Es correcto")

else :
    msj = print("Es incorrecto")


#Output
print("el numero digitadon ", msg)