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


    def  series ( self):
        I = 1
        serie = 0
        num = int(input("Ingrese un número: "))
        band =True
        while band:
            if band == True:
                serie = serie+(1/I)
                band = False
            else:
                serie = serie-(1/I)
                band = True
            I += 1
            if I > num:
                break
            print("El resultado de la serie es: {}" .format(serie))
    
            

numeros=numeros()
numeros.factorial()
numeros.series()



