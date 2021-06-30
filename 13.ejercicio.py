#ejercicio13
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.

class Ejercicio13:
    def __init__(self):
        pass
    def Variable  (self):
        print("")
        produc= 1
        suma=0
        numero=int(input("Ingresar un numero entero"))
        print("")
        while numero != -1:
             numero=int(input("Ingresar un numero: "))
             suma=suma+numero
             prod=prod*numero
             print(" ")   
        print("""Total de la suma es:""",suma,"""Total del producto es: """,prod)
    print(" ")
    Variable(" ")
