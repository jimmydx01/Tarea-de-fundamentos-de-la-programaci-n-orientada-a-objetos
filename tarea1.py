class Ejercicos:
    def __init__(self):
        pass
    def calculo(self):
        TC=float(input(" ingrese total de su comopra  "))
        descuento=TC*0.15
        CP=TC-descuento
        print("total de la compra:{}".format(CP))
    


    def aprobado(self):
                nota=float(input("dime la nota de tu examen "))
                if nota < 7:
                    R="reprobado"
                    print("tu notas",nota,R)
                elif nota == 7:
                    R="aprobado con las justas"
                    print("tu notas",nota,R)
                else:
                    R= " sobresaliente "
                    print("tu notas",nota,R ) 

    def salario(self):
        sueldo = float(input("ingrese su sueldo  "))
        v1=float(input("el valor de tu  primera venta "))
        v2=float(input("el valor de tu  segunda venta "))
        v3=float(input("el valor de tu  tercera venta "))
        comicion=(v1+v2+v3)* .10
        print(" tu sueldo es :$",sueldo)
        print("la comicionde las tres ventas  :",comicion)
        print("tu sueldo  mas la comicion es:$ ",sueldo+comicion)  
    

    def aumento(self):
            salario=float(input("dime tu salario actual  "))
            if salario <= 600:
                salario1= salario+salario*0.1
                print(salario1)
                print("tu salario nuevo es  ",salario1)
            else:
                print("tu salario no aplica para el aumento",salario)
    

    def sumas(self):
        n=100
        suma=0
        for i in range(1,n+1):
            elevado=i*i
            suma=suma+elevado
            print("la suma de los cuadrados de los primeros 100 enteros es :  ", suma)

Ejercicos=Ejercicos()
#cal1.calculo()
#Ejercicos.aprobado()
#Ejercicos.salario()
#Ejercicos.aumento()
Ejercicos.sumas()
