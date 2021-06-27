class Numeros:
    n=int(input("ingrese un numero"))
    def primo(n):
        contador=0
        resultado=True
        for i in range(1,n+1):
            if (n%i==0):
                contador+=1
            if (contador>2):
                resultado=False
                break
            return resultado
    if (primo(n)==True):
        print("el numero es primo")
    else: 
        print("el numero  no es primo ")

    


Numeros=Numeros()
Numeros.primo()


















