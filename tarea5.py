class Selectiva:
    def  entero( self ):
        val1  =  int ( input ( "Ingrese un número:" ))
        val2  =  int ( input ( "Ingrese un valor:" ))
        if val1  ==  1 :
            res  =  100  *  val2
        elif  val1  ==  2 :
            res  =  100  **  val2
        elif  val1  ==  3 :
            res  =  100 / val2
        else :
            res  =  0
        print ( "El resultado del número {} y el valor {} es de: {}" . formato ( val1 , val2 , res ))



    def Aceptado(self):
        nota1 = int(input("Ingrese la primera calificación: "))
        nota2 = int(input("Ingrese la segunda calificación: "))
        if nota1 >= 80 and nota2 >= 80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(nota1, nota2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(nota1, nota2))  

Selectiva=Selectiva()
Selectiva.entero()
Selectiva.Aceptado()