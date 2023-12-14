
import os
import psycopg2
conn = psycopg2.connect(
    dbname='primer_programa',
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)
cur = conn.cursor()
def opcion1():
            

    numero_programa = 1
    try:
            numero1 = int(input('Ingrese el primer numero :'))
            numero2 = int(input('Ingrese el segundo numero :'))
            numero3 = int(input('Ingrese el tercer numero :'))

            if numero1 > numero2 and numero1 > numero3 :

                    suma = numero1+numero2+numero3
                    print(suma)
                    f = open ('salida.txt','w')
                    f.write('Primer programa '+str(suma))
                    f.close()

                    #aquiva la base de datos
                    try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (numero_programa,suma))

                            # Ejecutar la instrucción SQL
                            cur.execute(Instruccion)

                            # Confirmar la transacción
                            conn.commit()

                    except psycopg2.Error as e:
                        print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                        # Cerrar el cursor y la conexión
                        cur.close()
                        conn.close()

                    #fin 
            
            elif numero2 > numero1 and numero2 > numero3:

                multi = numero1*numero2*numero3
                print(multi)
                
                f = open ('salida.txt','w')
                f.write('Primer programa '+str(multi))
                f.close()
                try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,multi))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()

            elif numero3 > numero1 and numero3 > numero2:
                con = "La conquetanacion es "+str(numero1) +" "+str(numero2) +" "+str(numero3) 
                print("la conquetanacion es  ",con)
                
                f = open ('salida.txt','w')
                f.write('Primer programa '+"la conquetanacion es  "+str(con))
                f.close()
                try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,str(con)))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()

            elif numero1 == numero2:

                if numero3 != numero2 and numero1:

                    print(numero3)
                    f = open ('salida.txt','w')
                    f.write('Primer programa '+" resultado  "+str(numero3))
                    f.close()
                    try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,str(numero3)))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

                    except psycopg2.Error as e:
                     print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                    # Cerrar el cursor y la conexión
                        cur.close()
                        conn.close()

            elif numero2 == numero3:

                if numero1 != numero2 and numero3:

                    print(numero1)
                    f = open ('salida.txt','w')
                    f.write('Primer programa '+" resultado  "+str(numero1))
                    f.close()
                    try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,str(numero1)))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

                    except psycopg2.Error as e:
                        print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                        # Cerrar el cursor y la conexión
                        cur.close()
                        conn.close()

            if numero1 == numero2 == numero3:

                print("Todos son iguales ")
                
                f = open ('salida.txt','w')
                f.write('Primer programa '+" resultado  "+"Todos son iguales")
                f.close()
                try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,"son iguales"))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()

    except ValueError as ve:
                print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
    except Exception as ex:
                print(f"Error inesperado: {ex}")
def opcion2():
           
    try:
            try:
                # Configuración de la conexión a la base de datos
                conn = psycopg2.connect(
                    dbname='primer_programa',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )

                # Crear un cursor para ejecutar consultas
                cur = conn.cursor()

                numero_programa = 2
                numero = int(input("Ingrese un número: "))

                for i in range(1, numero + 1):
                    if numero % i == 0:
                        print("Sus divisores son:", i)
                        a = [i]

                        f = open('segundo_programa.txt', 'w')
                        f.write('segundo programa ' + " resultado  " + "sus divisores son " + str(i))
                        f.close()

                        try:
                            # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                            
                            Instruccion = cur.mogrify(Ins1, (numero_programa, i))

                            # Ejecutar la instrucción SQL
                            cur.execute(Instruccion)

                            # Confirmar la transacción
                            conn.commit()

                        except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar el cursor y la conexión fuera del bucle for
                cur.close()
                conn.close()

    except ValueError as ve:
     print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
    except Exception as ex:
     print(f"Error inesperado: {ex}")

def opcion3():
        numero_programa =3
        try:
                palabra = input("Ingrese una palabra: ")
                if not palabra.isalpha():
                    raise ValueError("Por favor, asegúrese de ingresar una palabra válida.")
    
                palabra = palabra.lower()
                vocales = "aeiou"
                contador_vocales = 0
            
            # Contar las vocales en la palabra
                for letra in palabra:
                    if letra in vocales:
                        contador_vocales += 1
                
                print("la palabra tiene ",contador_vocales,"vocales")
                f = open ('tercer_programa.txt','w')
                f.write('tercer programa '+" resultado  "+"vocales son "+str(contador_vocales))
                f.close()
                cont = "numero de vocales "+str(contador_vocales)
                try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                            # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close()
        except ValueError as ve:
         print(f"Error: {ve}")
        except Exception as ex:
         print(f"Error inesperado: {ex}")
def opcion4():
     
     numero_programa = 4
     try:
            numero = int(input("ingrese un numero : "))
            contador =0


            for i in range(0 , numero):
                contador = contador +i

            print("la suma del numero , de 0 al numero es ",contador)
            f = open ('cuarto_programa.txt','w')
            f.write('cuarto programa '+" resultado  "+"de la suma es "+str(contador))
            f.close()
            cont = "la suma del numero de 0 al numero es "+str(contador)
            try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

            except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                            # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close()
     except ValueError as ve:
      print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
     except Exception as ex:
      print(f"Error inesperado: {ex}")
def opcion5():
     

    try:
        # Configuración de la conexión a la base de datos
        conn = psycopg2.connect(
            dbname='primer_programa',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        numero_programa = 5
        contador = 0
        # Abrir el archivo fuera del bucle para no sobrescribir en cada iteración
        with open('quinto_programa.txt', 'w') as f:
            for numero in range(1, 101, 2):
                print(numero)
                contador = contador +1
                cont = " los numeros son : "+str(numero)+" la cantidad es "+str(contador)
                # Escribir en el archivo
                f.write('quinto programa ' + " resultado  " + "de los números impares son " + str(numero) + '\n')

                try:
                    # Preparar la instrucción SQL para la inserción
                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                    
                    Instruccion = cur.mogrify(Ins1, (numero_programa, cont))

                    # Ejecutar la instrucción SQL
                    cur.execute(Instruccion)

                    # Confirmar la transacción
                    conn.commit()

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")

    # Manejar excepciones fuera del bucle
    except Exception as ex:
        print(f"Error general: {ex}")

    finally:
        # Cerrar el cursor y la conexión fuera del bucle
        cur.close()
        conn.close()

def opcion6():
     numero_programa = 6
     try:
            numero1 = int(input('Ingrese el primer numero :'))
            numero2 = int(input('Ingrese el segundo numero :'))
            numero3 = int(input('Ingrese el tercer numero :'))

            if numero1 == numero2 == numero3:
                    print("es equilatero")
                    f = open ('sexto programa.txt','w')
                    f.write('sexto programa '+" resultado  "+"es"+"equilatero")
                    f.close()
                    try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa,"es equilatero"))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                    except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                            # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close() 
            elif numero1 == numero2 or numero1 == numero3 or numero2 == numero1 or numero3 == numero1:
                print("es isoceles")
                f = open ('sexto programa.txt','w')
                f.write('sexto programa '+" resultado  "+"es"+"isoceles")
                f.close()
                try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa,"es isoceles"))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                            # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close() 
            elif numero1 != (numero2 and numero3) or numero2 != (numero1 and numero3) or numero3 != (numero1 and numero2):
                print("es escaleno")
                f = open ('sexto programa.txt','w')
                f.write('sexto programa '+" resultado  "+"es"+"escaleno")
                f.close()
                try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa,"es escaleno"))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                            # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close() 
     except ValueError as ve:
      print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
     except Exception as ex:
      print(f"Error inesperado: {ex}")

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
def opcion7():
     numero_programa = 7
     try:
                numero_ingresado = int(input("Ingresa un número entero: "))
                
                # Verificar si el número es divisible por 7
                if numero_ingresado % 7 == 0:
                    resultado = factorial(numero_ingresado)
                    print(f"El factorial de {numero_ingresado} es {resultado}")
                    f = open ('septimo programa.txt','w')
                    f.write('septimo programa '+" resultado  "+"de factorial es"+str(resultado))
                    f.close()

                    cont = "el factorial es"+str(resultado)
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
                else:
                    print(f"{numero_ingresado} no es divisible por 7, no se calculará el factorial.")
                    f = open ('septimo programa.txt','w')
                    f.write('septimo programa '+" resultado  "+"no es divisible por 7, no se calculará el factorial "+str(numero_ingresado))
                    f.close()
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,"no es divisible por 7, no se calculará el factorial"))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
     except ValueError as ve:
      print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
     except Exception as ex:
      print(f"Error inesperado: {ex}")

def opcion8():
      

    try:
        # Configuración de la conexión a la base de datos
        conn = psycopg2.connect(
            dbname='primer_programa',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        numero_programa = 8

        # Pedir al usuario que ingrese el primer y segundo número
        try:
                inicio = int(input('Ingrese el primer número: '))
                fin = int(input('Ingrese el segundo número: '))

                # Abrir el archivo fuera del bucle para no sobrescribir en cada iteración
                with open('octavo_programa.txt', 'w') as f:
                    for i in range(inicio, fin + 1, 2):
                        res = i
                        print(res)

                        # Escribir en el archivo
                        f.write('octavo programa ' + " resultado  " + "" + str(res) + '\n')
                        cont = "los numeros son "+str(res)
                        try:
                            # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                            
                            Instruccion = cur.mogrify(Ins1, (numero_programa, cont))

                            # Ejecutar la instrucción SQL
                            cur.execute(Instruccion)

                            # Confirmar la transacción
                            conn.commit()

                        except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                # No cierres el cursor y la conexión aquí, sino al final del bloque `try`.
        except ValueError as ve:
         print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
        except Exception as ex:
         print(f"Error inesperado: {ex}")

    except Exception as ex:
        print(f"Error general: {ex}")

    finally:
        # Cerrar el cursor y la conexión fuera del bucle
        cur.close()
        conn.close()



def opcion9():
   

    try:
        # Configuración de la conexión a la base de datos
        conn = psycopg2.connect(
            dbname='primer_programa',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        numero_programa = 9
        try:
                numero1 = int(input('Ingrese el primer numero: '))
                numero2 = int(input('Ingrese el segundo numero: '))

                # Abrir el archivo fuera del bucle para no sobrescribir en cada iteración
                with open('noveno_programa.txt', 'w') as f:
                    if numero1 > numero2:
                        for i in range(numero1, numero2-1, -1):
                            print(" ", i)
                            
                            # Escribir en el archivo
                            f.write('noveno programa ' + " resultado  " + "" + str(i) + '\n')
                            
                            try:
                                # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa, i))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                            except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    elif numero2 > numero1:
                        for i in range(numero2, numero1-1, -1):
                            print(" ", i)
                            
                            # Escribir en el archivo
                            f.write('noveno programa ' + " resultado  " + "" + str(i) + '\n')
                            
                            try:
                                # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                                
                                Instruccion = cur.mogrify(Ins1, (numero_programa, i))

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

                            except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")
        except ValueError as ve:
         print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
        except Exception as ex:
         print(f"Error inesperado: {ex}")

    # Manejar excepciones fuera del bucle
    except Exception as ex:
        print(f"Error general: {ex}")

    finally:
        # Cerrar el cursor y la conexión fuera del bucle
        cur.close()
        conn.close()

def opcion10():
        
    numero_programa = 10
    try:
        palabra= input("ingrese una palabra : ")
        if not palabra.isalpha():
         raise ValueError("Por favor, asegúrese de ingresar una palabra válida.")
    
        palabra = palabra.lower()
        vocales = "aeiou"
        contador_vocales1 = 0
        contador_vocales2 = 0
        contador_vocales3 = 0
        contador_vocales4 = 0
        contador_vocales5= 0

       
    
    # Contar las vocales en la palabra
        for letra in palabra:
            if letra in vocales :
                if letra == "a":
                 contador_vocales1 += 1 
                elif letra == "e":
                 contador_vocales2+=1
                elif letra == "i":
                 contador_vocales3+=1
                elif letra == "o":
                 contador_vocales4+=1
                elif letra == "u":
                 contador_vocales5+=1

        print("a",contador_vocales1)
        print("e",contador_vocales2)
        print("i",contador_vocales3)
        print("o",contador_vocales4)
        print("u",contador_vocales5)

        cont = "a "+str(contador_vocales1)+" e "+str(contador_vocales2)+" i "+str(contador_vocales3)+" o "+str(contador_vocales4)+" u "+str(contador_vocales5)
        f = open ('decimo programa.txt','w')
        f.write('decimo programa '+"repeticion"+" a  "+""+str(contador_vocales1)+"\n")
        f.write('decimo programa '+"repeticion"+" e "+""+str(contador_vocales2)+"\n")
        f.write('decimo programa '+"repeticion"+" i  "+""+str(contador_vocales3)+"\n")
        f.write('decimo programa '+"repeticion"+" o "+""+str(contador_vocales4)+"\n")
        f.write('decimo programa '+"repeticion"+" u  "+""+str(contador_vocales5))
        f.close()
        try:
                    # Preparar la instrucción SQL para la inserción
                        Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                        
                        
                        Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                        # Ejecutar la instrucción SQL
                        cur.execute(Instruccion)

                        # Confirmar la transacción
                        conn.commit()

        except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")

        finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close() 
    except ValueError as ve:
     print(f"Error: {ve}")
    except Exception as ex:
     print(f"Error inesperado: {ex}")

def opcion11():
        

    try:
        # Configuración de la conexión a la base de datos
        conn = psycopg2.connect(
            dbname='primer_programa',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        numero_programa = 11

        while True:
            print("\nMenú de Opciones:")
            print("1. Área círculo")
            print("2. Área triángulo")
            print("3. Área cuadrado")
            print("4. Área rectángulo")
            print("5. Salir")
            try:
                        seleccion = int(input("Ingresa el número de la opción: "))

                        if seleccion == 1:
                            try:
                                numero = float(input("Ingrese el radio: "))
                                area = 2 * 3.1416 * numero ** 2
                                print("El área del círculo es ", area)
                            except ValueError as ve:
                             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
                            except Exception as ex:
                             print(f"Error inesperado: {ex}")
                        elif seleccion == 2:
                            try:
                                base = float(input("Ingrese la base: "))
                                altura = float(input("Ingrese la altura: "))
                                area = 0.5 * base * altura
                                print("El área del triángulo es ", area)
                            except ValueError as ve:
                             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
                            except Exception as ex:
                             print(f"Error inesperado: {ex}")

                        elif seleccion == 3:
                            try:
                                lado = float(input("Ingrese el lado: "))
                                area = lado ** 2
                                print("El área del cuadrado es ", area)
                            except ValueError as ve:
                             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
                            except Exception as ex:
                             print(f"Error inesperado: {ex}")

                        elif seleccion == 4:
                            try:
                                lado1 = float(input("Ingrese el ancho: "))
                                lado2 = float(input("Ingrese el largo: "))
                                area = lado1 * lado2
                                print("El área del rectángulo es ", area)
                            except ValueError as ve:
                             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
                            except Exception as ex:
                             print(f"Error inesperado: {ex}")

                        elif seleccion == 5:
                            try:
                             break
                            except ValueError as ve:
                             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
                            except Exception as ex:
                             print(f"Error inesperado: {ex}")

                        else:
                            print("La opción no está disponible.")

                        # Abrir el archivo fuera del bucle para no sobrescribir en cada iteración
                        with open('onceavo_programa.txt', 'w') as f:
                            # Escribir en el archivo
                            f.write(f'onceavo programa - Resultado del área: {area}\n')

                        cont = f'El área es: {area}'
                        try:
                            # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                            Instruccion = cur.mogrify(Ins1, (numero_programa, cont))

                            # Ejecutar la instrucción SQL
                            cur.execute(Instruccion)

                            # Confirmar la transacción
                            conn.commit()

                        except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")
            except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
            except Exception as ex:
             print(f"Error inesperado: {ex}")

    finally:
        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()



def opcion12():
    numero_programa=12
    try:
                nota1 = float(input("Ingrese la primera nota : "))
                nota2 = float(input("Ingrese la segunda  nota : "))
                nota3 = float(input("Ingrese la trecera nota : "))
                promedio = (nota1+nota2+nota3)/3
                if promedio >= 60:
                    print("Aprovado")
                    print("el priomedio es : ",promedio)
                    f = open ('doceavo programa.txt','w')
                    f.write('doceavo programa '+" resultado "+" "+str("Aprobado")+"\n")
                    f.write('doceavo programa '+" resultado del promedio es "+" "+str(promedio))
                    f.close()
                    cont =" Es Aprobado "+"El promedio es "+str(promedio)
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
                if promedio < 60:
                    print("Reprobado")
                    print("el priomedio es : ",promedio)
                    f = open ('onceavo programa.txt','w')
                    f.write('doceavo programa '+" resultado "+" "+str("Reprobado")+"\n")
                    f.write('doceavo programa '+" resultado del promedio es "+" "+str(promedio))
                    f.close()
                    cont =" Es Reprobado "+"El promedio es "+str(promedio)
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
    except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
    except Exception as ex:
             print(f"Error inesperado: {ex}")

def opcion13():

    numero_programa = 13
    try:
                anio = int(input("Ingrese su año de nacimiento : "))
                if anio % 4 == 0:
                    print("El año es "+" bisiesto")
                    f = open ('terceavo programa.txt','w')
                    f.write('terceavo programa '+" resultado "+" "+str("Bisiesto")+"\n")
                    
                    f.close()
                    cont =" Año de nacimiento "+str(anio)+" Es Bisiesto"
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
                else:
                    
                    print("El año  "+" no bisiesto")
                    f = open ('terceavo programa.txt','w')
                    f.write('terceavo programa '+" resultado "+" "+str("no es bisiesto")+"\n")
                    f.close()
                    cont =" Año de nacimiento "+str(anio)+" No Es Bisiesto"
                    try:
                                # Preparar la instrucción SQL para la inserción
                                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                                    
                                    
                                    Instruccion = cur.mogrify(Ins1, (numero_programa,cont))

                                    # Ejecutar la instrucción SQL
                                    cur.execute(Instruccion)

                                    # Confirmar la transacción
                                    conn.commit()

                    except psycopg2.Error as e:
                                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                                # Cerrar el cursor y la conexión
                                cur.close()
                                conn.close() 
    except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
    except Exception as ex:
             print(f"Error inesperado: {ex}")

def opcion14():
        

    try:
        # Configuración de la conexión a la base de datos
        conn = psycopg2.connect(
            dbname='primer_programa',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )

        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        numero_programa = 14
        try:

                ingreso_modelo = int(input("Ingrese el modelo del taxi: "))
                recorrido = int(input("Ingrese el recorrido en km: "))

                resultado = None

                if ingreso_modelo < 2007 and recorrido > 20:
                    resultado = "Debe renovarse"

                elif 2007 < ingreso_modelo < 2013 and recorrido == 20000:
                    resultado = "Debe recibir mantenimiento"

                elif ingreso_modelo > 2013 and recorrido < 10000:
                    resultado = "Óptimas condiciones"

                else:
                    resultado = "Mecánico, por favor :)"

                print(resultado)

                # Abrir el archivo fuera del bucle para no sobrescribir en cada iteración
                with open('catorceavo_programa.txt', 'w') as f:
                    # Escribir en el archivo
                    f.write(f'catorceavo programa - Resultado: {resultado}\n')

                cont = f'Modelo: {ingreso_modelo}, Recorrido: {recorrido}, Resultado: {resultado}'

                try:
                    # Preparar la instrucción SQL para la inserción
                    Ins1 = 'INSERT INTO tablaresultados (numeroprograma,resultados) VALUES (%s,%s);'
                    Instruccion = cur.mogrify(Ins1, (numero_programa, cont))

                    # Ejecutar la instrucción SQL
                    cur.execute(Instruccion)

                    # Confirmar la transacción
                    conn.commit()

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la DB. Consulte el error: {e}")
        except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
        except Exception as ex:
             print(f"Error inesperado: {ex}")

    finally:
        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()


def salir():
    try:
          

     exit()

    except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar números enteros.")
    except Exception as ex:
             print(f"Error inesperado: {ex}")
while True:

        print("\nMenú de Opciones:")
        print("1. Pedri 3 numeros")
        print("2. Pedir numero y mostara divisores")
        print("3. Pedir palabra")
        print("4. Pedir numero y mostrar de 0 al numeros")
        print("5. Numeros impares de 1 al 100")
        print("6. que clase de triangulo es ")
        print("7. factorial si y solo si es divisible entre 7")
        print("8. inicio y fin de un numero")
        print("9. Pedir dos numeros verificar el mayor")
        print("10. Cuantas veces se repite una vocal")
        print("11. Calculadora geometrica")
        print("12. Promedio de notas")
        print("13. Año de nacimeinto bisiesto o no")
        print("14 clasificacion de taxis")
        print("15. Salir")

        try:
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
                elif seleccion == 9:
                    
                 opcion9()
                elif seleccion == 10:
                    
                 opcion10()
                elif seleccion == 11:
                    
                 opcion11()
                elif seleccion == 12:
                    
                 opcion12()
                elif seleccion == 13:
                    
                 opcion13()
                elif seleccion == 14:

                    opcion14()
                elif seleccion == 15:

                    salir()
                else:
                    
                    print("Elije nuevam,ente")
        except ValueError as ve:
             print(f"Error: {ve}. Asegúrese de ingresar una de las opciones.")
        except Exception as ex:
             print(f"Error inesperado: {ex}")
