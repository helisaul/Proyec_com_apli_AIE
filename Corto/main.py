
import os


def opcion1():


            numero1 = int(input('Ingrese el primer numero :'))
            numero2 = int(input('Ingrese el segundo numero :'))
            numero3 = int(input('Ingrese el tercer numero :'))

            if numero1 > numero2 and numero1 > numero3 :

                suma = numero1+numero2+numero3
                print(suma)
                f = open ('holamundo.txt','w')
                f.write('str(suma)')
                f.close()

            elif numero2 > numero1 and numero2 > numero3:

                multi = numero1*numero2*numero3
                print(multi)
            elif numero3 > numero1 and numero3 > numero2:
                con = str(numero1) +" "+str(numero2) +" "+str(numero3) 
                print("la conquetanacion es  ",con)

            elif numero1 == numero2:

                if numero3 != numero2 and numero3:

                    print(numero3)
            elif numero2 == numero3:

                if numero1 != numero2 and numero3:

                    print(numero1)
            elif numero1 == (numero2 and numero3 ) or numero2 == (numero1 and numero3) or numero3 == (numero1 and numero2):

                print("Todos son iguales ")

def opcion2():

            numero = int(input("Ingrese un numero :"))

            for i in range(1, numero + 1):
              if numero % i == 0:
               print("sus divisores son :",i)
def opcion3():
     
        palabra= input("ingrese una palabra : ")
        palabra = palabra.lower()
        vocales = "aeiou"
        contador_vocales = 0
    
    # Contar las vocales en la palabra
        for letra in palabra:
            if letra in vocales:
                contador_vocales += 1
        
        print("la palabra tiene ",contador_vocales,"vocales")
         
def opcion4():
     

     numero = int(input("ingrese un numero : "))
     contador =0


     for i in range(0 , numero):
          contador = contador +i

     print("la suma del numero , de 0 al numero es ",contador)
          
def opcion5():
     for numero in range(1, 101, 2):
      print(numero)
def opcion6():
     numero1 = int(input('Ingrese el primer numero :'))
     numero2 = int(input('Ingrese el segundo numero :'))
     numero3 = int(input('Ingrese el tercer numero :'))

     if numero1 == numero2 and numero3:
          print("es equilatero")
     elif numero1 == numero2 or numero1 == numero3 or numero2 == numero1 or numero3 == numero1:
          print("es isoceles")
     elif numero1 != (numero2 and numero3) or numero2 != (numero1 and numero3) or numero3 != (numero1 and numero2):
          print("es escaleno")


def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
def opcion7():
     
     numero_ingresado = int(input("Ingresa un número entero: "))
    
    # Verificar si el número es divisible por 7
     if numero_ingresado % 7 == 0:
        resultado = factorial(numero_ingresado)
        print(f"El factorial de {numero_ingresado} es {resultado}")
     else:
        print(f"{numero_ingresado} no es divisible por 7, no se calculará el factorial.")


def opcion8():
     inicio = int(input('Ingrese el primer numero :'))
     fin = int(input('Ingrese el segundo numero :'))

     for i in range(inicio, fin):
         res = 2*i
         print(res)
         if res == fin:
             
          
             break


while True:

        print("\nMenú de Opciones:")
        print("1. Pedri 3 numeros")
        print("2. Pedir numero y mostara divisores")
        print("3. Pedir palabra")
        print("4. Pedir numero y mostrar de 0 al numeros")
        print("5. Numeros impares")
        print("6. que clase de triangulo es ")
        print("7. factorial de 1 a 100")
        print("8. inicio y fin de un numero")
        print("9. Opción 3")
        print("10. Salir")
        print("11. Opción 2")
        print("12. Opción 3")
        print("13. Salir")

        
        seleccion = int(input("Ingresa el número de la opción que deseas: ") )



        if seleccion == 1:

           opcion1()


        elif seleccion == 2:
            
           opcion2()
        elif seleccion == 3:
            
           opcion3()
        elif seleccion == 4:
            
           opcion4()
        elif seleccion == 5:
            
           opcion5()
        elif seleccion == 6:
            
           opcion6()
        elif seleccion == 7:
            
           opcion7()
        elif seleccion == 8:
            
           opcion8()

        else:
             
             print("Elije nuevam,ente")
