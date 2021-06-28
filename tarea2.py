class Trabajo:
    def __init__(self):
        pass
    def pagoJornadaExtra(self):
        horas_trabajadas,horas_extras,horas_triples=0,0,0
        valor_hora,pago_horas_extras,pago_total=0,0,0
        horas_trabajadas=int(input("dime cunatas horas has trabajado :"))
        valor_hora=float(input("ingrese el valor de hora :"))
        if (horas_trabajadas > 40):
            horas_extras=horas_trabajadas - 40
            if (horas_extras > 8):
                horas_triples=horas_extras - 8
                pago_horas_extras=valor_hora* 2 * 8 + valor_hora * 3 * horas_triples
            else:
                pago_horas_extras=valor_hora * 2 * horas_extras
            pago_total=valor_hora * 40 + pago_horas_extras
        else:
                pago_total=valor_hora * horas_trabajadas
        print("""Horas trabajadas:{} Horas extras:{} Horas triples:{} valor hora:{} 
            Pago valor extra:{} Pagp total:{}""".format(horas_trabajadas,horas_extras,horas_triples,
                                                        valor_hora,pago_horas_extras,pago_total)) 




    def mayor(self):
        n1,n2,n3=0,0,0
        n1=int(input("ingrse numero1: "))
        n2=int(input("ingrse numero2: "))
        n3=int(input("ingrse numero3: "))
        if (n1>n2>n3):
            print("el mayor es:",n1)
        elif (n2>n1>n3):
            print("el mayor es:",n2)
        else:
            print("el mayor es:",n3)


    def cien(self):
        numero=1
        while numero <= 100:
            contador=1
            x=0
            while contador <= numero:
                x=x+1
                contador=contador+1
            print(numero)
            numero=numero+1     



    def sumad(num):
        s=0
        while num>0:
            s=s+num%10
            num=num//10
        return s    
    n=int(input("cantidad de numeros: "))
    suma=0
    prod=1
    while n>0 and n>1:
        num=int(input("numero: "))
        suma=suma+sumad(num)
        prod=prod*sumad(num)
        n=n-1   
    print(suma)
    print(prod)     
    


                

        

pago=Trabajo()
#pago.pagoJornadaExtra()
#pago.mayor()
#pago.cien()
pago.sumad()
