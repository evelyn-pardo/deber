#ejercicio17
#Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.

class Tarea17:
    def _init_(self):
        pass
    def fases(self):
        print("")
        num[20],i,j,k,A[20],B[20]=0,0,0,0,0,0
        j=1
        k=1
        for i==1 in range(1,20,1):
            num[i]=int(input("Ingrese numero: "))
            if num[i]>0:
                A[j]=num[i]
                j=j+1
            else:
                B[k]=num[i]
                k=k+1
        for i==1 in j:
            print(A[j])
        for i==1 in k:
            print(B[k])
        print("")
    fases("")