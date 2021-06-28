from tarea4 import numeros


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

    def notas1(self):
        nota = float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if nota >= 7:
            print("La nota es {}, APROBADO" .format(nota))


    def suma_pro(self):
        suma = 0
        prod = 1
        res = "S"
        while res == "S":
            n = int(input("Ingrese un número: "))
            suma = suma + n
            prod = prod * n
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(prod))
            print("Desea continuar [S/N]:  ")
            res = input().capitalize()

Numeros=Numeros()
Numeros.primo()
Numeros.notas1()
numeros.suma_pro()

















