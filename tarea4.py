class numeros:
    def factorial(self):
        n=int(input("ingrse un numero : "))
        if n>=0:
            x=1
            f=1
            while x<= n:
                f=f*x
                x+=1
                print("el factorial de",n, "es: ",f)
        else:
            print("no se puede calcular el factorila")
numeros=numeros()
numeros.factorial()



