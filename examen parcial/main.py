import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable
import random
conn = psycopg2.connect(
    dbname='estudiantes',
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)
cur = conn.cursor()
def opcion1():

    


    while True:

        print("Menu de Opciones:")
        print("1. Ingresar datos")
        print("2. Eliminar")
        print("3. Actualizar")
        print("4. Salir")

        while True:

            try:


                op = int(input("ingres opcion "))
                break
            except ValueError:
                            print("La edad debe ser un valor numérico.")

        if op == 1:
                    
                try:
                    conn = psycopg2.connect(
                        dbname='estudiantes',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432'
                    )
                    cur = conn.cursor()


                    while True:
                                
                            

                            nombre = input("Ingrese su nombre: ")
                            if nombre.isalpha():
                                 break
                            else:
                                 print("Deber debe ser caracter ")


                    while True:
                        try:
                            edad = int(input("Ingrese su edad: "))
                            break
                        except ValueError:
                            print("La edad debe ser un valor numérico.")




                    while True:
                             genero = input("Ingrese su género: ")
                             if genero.isalpha():
                                  
                                  break
                             else:
                                  print("Debe ser caracter ")
                    direccion = input("Ingrese su dirección: ")

                    try:
                        Ins1 = 'INSERT INTO datos (nombre,edad,genero,direccion) VALUES (%s,%s,%s,%s);'
                        Instruccion = cur.mogrify(Ins1, (nombre, edad, genero, direccion))

                        cur.execute(Instruccion)
                        conn.commit()

                    except psycopg2.Error as e:
                        print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                    finally:
                        cur.close()
                        conn.close()

                except psycopg2.Error as e:
                    print(f"Error de conexión a la DB. Consulte el error: {e}")
            
        elif op == 2:
            try:
                # Establecer la conexión a la base de datos
                conn = psycopg2.connect(
                    dbname='estudiantes',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor()

                # Obtener el nombre para identificar el registro a eliminar
                while True:
                    nombre_a_eliminar = input("Ingrese el nombre a eliminar: ")
                    if nombre_a_eliminar.isalpha():
                        break
                    else:
                        print("El nombre debe contener solo caracteres.")

                # Construir y ejecutar la sentencia DELETE
                sentencia_delete = "DELETE FROM datos WHERE nombre = %s;"
                cur.execute(sentencia_delete, (nombre_a_eliminar,))

                # Confirmar la transacción
                conn.commit()
                print("Registro eliminado exitosamente.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar el cursor y la conexión
                cur.close()
                conn.close()
        elif op == 3:
        
            conn = psycopg2.connect(
                    dbname='estudiantes',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto


                while True:
                        

                        nombre_estudiante = input("Ingrese el nombre del estuante que desea actualizar: ")

                        if nombre_estudiante.isalpha():
                             break
                        
                        else:
                         print("El nombre debe contener solo caracteres.") 

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM datos WHERE nombre = %s;", (nombre_estudiante,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún estudiante con el nombre '{nombre_estudiante}'.")
                else:
                    # Solicitar al usuario los nuevos valores



                    while True:

                        try:
                            nuevo_edad = int(input("Ingrese la nueva edad: "))
                            break
                        except ValueError:
                            print("La edad debe ser un valor numérico.")
                            



                    nueva_genero = (input("Ingrese el nuevo genero: "))
                    nuevo_direccion = (input("Ingrese una nueva direccion: "))
                    
                    # Sentencia SQL de actualización
                    sql_actualizacion = """
                        UPDATE datos
                        SET edad = %s, genero = %s , direccion = %s
                        WHERE nombre = %s;
                    """

                    # Ejecutar la actualización
                    cur.execute(sql_actualizacion, (nuevo_edad, nueva_genero,nuevo_direccion ,nombre_estudiante))

                    # Confirmar la transacción
                    conn.commit()

                    print(f"Se ha actualizado la información del estudiante '{nombre_estudiante}'.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()
        elif op == 4:

            break










def opcion2():

    while True:
        

        print("Menu de Opciones:")
        print("1. Ingresar gasto")
        print("2. ver resumen")
        print("3. Actualizar")
        print("4. Salir")

        while True:
             
            try:
             op = int(input("ingres opcion "))
             break
            except ValueError:
                 print("Debe ser numerico la opcion")

        if op == 1:
            conn = psycopg2.connect(
                dbname='gasto',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()

            while True:
                        

                    nombre_gasto= input("nombre del gasto : ")
                    if nombre_gasto.isalpha():
                         
                         break
                    else:
                         
                         print("Deber ser caracter")



            while True:
                     
                try:

                     gasto = float(input("ingrese cantidad de gasto: "))

                     break
                except ValueError:
                     
                     print("Deber ser numerico ")


            while True:

                try:
                     presupuesto = float(input("ingrese su presupuesto actual : "))
                     break
                except ValueError:
                     
                     print("Debe ser numerico ")
            try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO gasto1 (nombregasto,cantidad,presupuesto) VALUES (%s,%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (nombre_gasto,gasto,presupuesto))

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
        elif op == 2:
           # Parámetros de conexión a la base de datos
            conn = psycopg2.connect(
                dbname='gasto',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()

            # Nombre de la tabla que deseas consultar
            nombre_tabla = "gasto1"

            # Consulta SQL para obtener todos los datos de la tabla
            consulta_sql = f"SELECT * FROM {nombre_tabla};"

            # Ejecutar la consulta
            cur.execute(consulta_sql)

            # Obtener todos los resultados
            resultados = cur.fetchall()

            # Mostrar los resultados
            
            for fila in resultados:
                print(" id "," nombre "," cantidad ", " presupuesto ")
                print("   ",fila)

            # Cerrar la conexión
            cur.close()
            conn.close()
        elif op == 3:
        
            conn = psycopg2.connect(
                    dbname='gasto',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto

                while True:
                         
                    
                         nombre_gasto= input("Ingrese el nombre del gasto que desea actualizar: ")
                         if nombre_gasto.isalpha():
                              
                              break
                         else:
                              print("Deber ser caracter")

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM gasto1 WHERE nombregasto = %s;", (nombre_gasto,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún gasto con el nombre '{nombre_gasto}'.")
                else:
                    # Solicitar al usuario los nuevos valores
                       
                    while True:
                            try:
                                nuevo_cantidad = int(input("Ingrese la nueva cantidad: "))
                                nueva_presupuesto = int(input("Ingrese el nuevo presupesuto: "))
                                break
                            except ValueError:
                                 
                                 print("Deber ser valor numerico ")
                    
                    # Sentencia SQL de actualización
                    sql_actualizacion = """
                        UPDATE gasto1
                        SET cantidad = %s, presupuesto = %s 
                        WHERE nombregasto = %s;
                    """

                    # Ejecutar la actualización
                    cur.execute(sql_actualizacion, (nuevo_cantidad, nueva_presupuesto,nombre_gasto))

                    # Confirmar la transacción
                    conn.commit()

                    print(f"Se ha actualizado la información del gasto '{nombre_gasto}'.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()
        elif op == 4:

              break



def opcion3():

  
    while True:

        print("Menu de Opciones:")
        print("1. Ingresar producto")
        print("2. Eliminar")
        print("3. Actualizar")
        print("4. Salir")

        while True:
                 

            try:
                 op = int(input("ingres opcion "))
                 break
            except ValueError:
                 print("Deber ser numerico la opcion ")

        if op == 1:


            conn = psycopg2.connect(
                dbname='produc',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
            cur = conn.cursor()
            nombre = input("Ingrese nombre del producto : ")
            precio = input("Ingrese el pprecio: ")

            cantidad = input("ingrese la cantidad : ")
           
            try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO productos (nombre,precio,cantidad) VALUES (%s,%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (nombre,precio,cantidad))

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
        elif op == 2:
            try:
                # Establecer la conexión a la base de datos
                
                conn = psycopg2.connect(
                dbname='produc',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
                cur = conn.cursor()
                # Obtener el nombre para identificar el registro a eliminar
                nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")

                # Construir y ejecutar la sentencia DELETE
                sentencia_delete = "DELETE FROM productos WHERE nombre = %s;"
                cur.execute(sentencia_delete, (nombre_a_eliminar,))

                # Confirmar la transacción
                conn.commit()
                print("Registro eliminado exitosamente.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar el cursor y la conexión
                cur.close()
                conn.close()
        elif op == 3:
        
             
            conn = psycopg2.connect(
                    dbname='produc',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto
                nombre_producto= input("Ingrese el nombre del producto que desea actualizar: ")

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM productos WHERE nombre = %s;", (nombre_producto,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún gasto con el nombre '{nombre_producto}'.")
                else:
                    # Solicitar al usuario los nuevos valores
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    
                    
                    # Sentencia SQL de actualización
                    sql_actualizacion = """
                        UPDATE productos
                        SET precio = %s, cantidad = %s 
                        WHERE nombre = %s;
                    """

                    # Ejecutar la actualización
                    cur.execute(sql_actualizacion, (nuevo_precio, nueva_cantidad,nombre_producto))

                    # Confirmar la transacción
                    conn.commit()

                    print(f"Se ha actualizado la información del producto '{nombre_producto}'.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()
        elif op == 4:

            break

def opcion4():

    
    while True:

        print("Menu de Opciones:")
        print("1. Ingresar datos")
        print("2. Eliminar")
        print("3. Actualizar")
        print("4. Salir")

        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")

                

        if op == 1:
            conn = psycopg2.connect(
                dbname='pedidos',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
            cur = conn.cursor()
            nombre = input("Ingrese el nombre del solicitante : ")
            nombre_pedido = input("Ingrese nombre del pedido : ")

            precio = input("ingrese el precio del pedido: ")
            cantidad = input("Ingrese la cantidad del pedido: ")
            try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO pedido (nombre,nombrepedido,precio,cantidad) VALUES (%s,%s,%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (nombre,nombre_pedido,precio,cantidad))

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
        elif op == 2:
            try:
                # Establecer la conexión a la base de datos
                
                conn = psycopg2.connect(
                dbname='pedidos',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
                cur = conn.cursor()
                # Obtener el nombre para identificar el registro a eliminar
                nombre_a_eliminar = input("Ingrese el nombre  a eliminar: ")

                # Construir y ejecutar la sentencia DELETE
                sentencia_delete = "DELETE FROM pedido WHERE nombre = %s;"
                cur.execute(sentencia_delete, (nombre_a_eliminar,))

                # Confirmar la transacción
                conn.commit()
                print("Registro eliminado exitosamente.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar el cursor y la conexión
                cur.close()
                conn.close()
        elif op == 3:
        
            conn = psycopg2.connect(
                    dbname='pedidos',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto
                nombre_pedido= input("Ingrese el nombre  que desea actualizar: ")

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM pedido WHERE nombre = %s;", (nombre_pedido,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún gasto con el nombre '{nombre_pedido}'.")
                else:
                    # Solicitar al usuario los nuevos valores
                    nuevo_pedido = (input("Ingrese el nuevo nombre del pedido: "))
                    nueva_precio = int(input("Ingrese el nuevo precio: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    
                    
                    # Sentencia SQL de actualización
                    sql_actualizacion = """
                        UPDATE pedido
                        SET nombrepedido = %s, precio = %s , cantidad = %s
                        WHERE nombre = %s;
                    """

                    # Ejecutar la actualización
                    cur.execute(sql_actualizacion, (nuevo_pedido, nueva_precio,nueva_cantidad,nombre_pedido))

                    # Confirmar la transacción
                    conn.commit()

                    print(f"Se ha actualizado la información del pedido '{nombre_pedido}'.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()
        elif op == 4:

            break

def opcion5():

    while True:
        

        print("Menu de Opciones:")
        print("1. Ingresar venta")
        print("2. Informe")
        print("3. Tendencia")
        print("4. Analisis")
        print("5. Salir")


        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")

        if op == 1:
            conn = psycopg2.connect(
                dbname='ventas',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()
            nombre_gasto= input("nombre venta : ")
            gasto = float(input("ingrese cantidad : "))
            
            try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO venta (nombre,cantidad) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (nombre_gasto,gasto))

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
        elif op == 2:
           # Parámetros de conexión a la base de datos
            conn = psycopg2.connect(
                dbname='ventas',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
            )
            cur = conn.cursor()

            # Nombre de la tabla que deseas consultar
            nombre_tabla = "venta"

            # Consulta SQL para obtener todos los datos de la tabla
            consulta_sql = f"SELECT * FROM {nombre_tabla};"

            # Ejecutar la consulta
            cur.execute(consulta_sql)

            # Obtener todos los resultados
            resultados = cur.fetchall()

            # Mostrar los resultados
            
            for fila in resultados:
                print(" id "," nombre "," cantidad ")
                print("   ",fila)

            # Cerrar la conexión
            cur.close()
            conn.close()
        elif op == 3:
        
             
                conn = psycopg2.connect(
                dbname='ventas',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
                cur = conn.cursor()
                

                # Consulta SQL para obtener datos de la tabla
                consulta_sql = "SELECT nombre, cantidad FROM venta;"
                cur.execute(consulta_sql)

                # Obtener resultados
                resultados = cur.fetchall()

                # Extraer columnas para el gráfico
                columna_x, columna_y = zip(*resultados)

                # Graficar los datos
                plt.plot(columna_x, columna_y, marker='o', linestyle='-')
                plt.title("Tendencia de ventas")
                plt.xlabel("Nombre de la Venta")
                plt.ylabel("Cantidad de ventas")

                # Mostrar el gráfico
                plt.show()

                # Cerrar la conexión
                cur.close()
                conn.close()
        
        
        elif op ==4:
              
            conn = psycopg2.connect(
                dbname='ventas',
                user='postgres',
                password='1234',
                host='localhost',
                port='5432'
                )
            cur = conn.cursor()
            # Consulta SQL para obtener datos de la tabla
            consulta_sql = "SELECT * FROM venta;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['cantidad'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: histograma)
            df['cantidad'].plot(kind='hist', bins=10, title="Histograma")
            plt.show()

            # Cerrar la conexión
            conn.close()



        elif op == 5:

              break
        







def opcion6():

    

    while True:
          
        print("Menu de Opciones:")
        print("1. Ingresar datos de los senores")
        print("2. PTC")
        print("3. PT100")
        print("4. PT100")
        print("5. Gratica y Tabla ")
        print("6. Salir")


        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")
        
        if op == 1:

                conn = psycopg2.connect(
                    dbname='sensores',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor()
                nombre_sensor= input("nombre : ")
                dato = float(input("datos : "))
                
                try:
                            # Preparar la instrucción SQL para la inserción
                                Ins1 = 'INSERT INTO sensor (ntc,datos) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                               
                                
                                
                                Instruccion = cur.mogrify(Ins1, (nombre_sensor,dato))
                                

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion)

                                # Confirmar la transacción
                                conn.commit()

               

                                nombre_sensor2= input("nombre : ")
                                dato2 = float(input("datos : "))
                                
                
                            # Preparar la instrucción SQL para la inserción
                               
                                Ins2 = 'INSERT INTO sensor2 (ptc,datos) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                               
                                
                                
                                Instruccion2 = cur.mogrify(Ins2, (nombre_sensor2,dato2))
                                

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion2)

                                # Confirmar la transacción
                                conn.commit()

                
                                nombre_sensor3= input("nombre : ")
                                dato3 = float(input("datos : "))
                                
                
                            # Preparar la instrucción SQL para la inserción
                               
                                Ins3 = 'INSERT INTO sensor3 (pt100,datos) VALUES (%s,%s);'  # %s es un marcador de posición para el valor
                               
                                
                                
                                Instruccion3 = cur.mogrify(Ins3, (nombre_sensor3,dato3))
                                

                                # Ejecutar la instrucción SQL
                                cur.execute(Instruccion3)

                                # Confirmar la transacción
                                conn.commit()

                except psycopg2.Error as e:
                            print(f"Error durante la conexión a la DB. Consulte el error: {e}")

                finally:
                        # Cerrar el cursor y la conexión
                            cur.close()
                            conn.close()


        elif op == 2:
            conn = psycopg2.connect(
                    dbname='sensores',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM sensor;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            
           

            # Mostrar los datos como una tabla utilizando prettytable
           


            # Cerrar la conexión
            conn.close()


        elif op == 3:
            conn = psycopg2.connect(
                    dbname='sensores',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM sensor2;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            # Cerrar la conexión
            conn.close()

        elif op ==4:
              

            conn = psycopg2.connect(
                    dbname='sensores',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM sensor3;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            # Cerrar la conexión
            conn.close()

        
        elif op == 5:
              
            conn = psycopg2.connect(
                    dbname='sensores',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 
            consulta_sql = "SELECT * FROM sensor;"
            df = pd.read_sql_query(consulta_sql, conn)

            consulta_sql2 = "SELECT * FROM sensor2;"
            df2 = pd.read_sql_query(consulta_sql2, conn)

            consulta_sql3 = "SELECT * FROM sensor3;"
            df3 = pd.read_sql_query(consulta_sql3, conn)

            # Mostrar los datos como una tabla utilizando pandas
            print("Datos de la Tabla NTC:")
            print(df)
            print("Datos de la Tabla PTC:")
            print(df2)
            print("Datos de la Tabla PT100:")
            print(df3)

            # Cerrar la conexión
            conn.close()



        elif op == 6:
              
              break

        
              
           


        
          


def opcion7():

    
        while True: 
            while True:
                      buscar = input("Buscar Gusto : ")
                      if buscar.isalpha():
                           break
                      else:
                           print("Deber ser caracter ")

             
            if buscar == "accion":
                

                conn = psycopg2.connect(
                    dbname='peliculas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor() 
                consulta_sql = "SELECT * FROM pelicula;"
                df = pd.read_sql_query(consulta_sql, conn)

                

                # Mostrar los datos como una tabla utilizando pandas
                print("Peliculas de accion:")
                print(df)
                

                # Cerrar la conexión
                conn.close()

            elif buscar == "comedia":
                  
                conn = psycopg2.connect(
                    dbname='peliculas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor() 
                consulta_sql = "SELECT * FROM pelicula3;"
                df = pd.read_sql_query(consulta_sql, conn)

                

                # Mostrar los datos como una tabla utilizando pandas
                print("peliculas de comedia:")
                print(df)
                

                # Cerrar la conexión
                conn.close()

            elif buscar == "miedo":
                conn = psycopg2.connect(
                    dbname='peliculas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor() 
                consulta_sql = "SELECT * FROM pelicula2;"
                df = pd.read_sql_query(consulta_sql, conn)

                

                # Mostrar los datos como una tabla utilizando pandas
                print("peliculas de miedo:")
                print(df)
                

                # Cerrar la conexión
                conn.close()


            elif buscar == "salir":
                  
                  break





def opcion8():

     while True:
          
        print("Menu de Opciones:")
        
        print("1. Google")
        print("2. Cementos Progresos")
        print("3. Intel")
        print("4. Gratica y Tabla ")
        print("5. Salir")


        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")
        
        


        if op == 1:
            conn = psycopg2.connect(
                    dbname='empresas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM empresa;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            
           

            # Mostrar los datos como una tabla utilizando prettytable
           


            # Cerrar la conexión
            conn.close()


        elif op == 2:
            conn = psycopg2.connect(
                    dbname='empresas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM empresa2;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            # Cerrar la conexión
            conn.close()

        elif op ==3:
              

            conn = psycopg2.connect(
                    dbname='empresas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM empresa3;"
            df = pd.read_sql_query(consulta_sql, conn)

            # Convertir la columna 'cantidad' a tipo numérico y manejar NaN
            df['datos'] = pd.to_numeric(df['datos'], errors='coerce')

            # Eliminar filas con valores nulos
            df.dropna(subset=['datos'], inplace=True)

            # Realizar análisis de datos (ejemplo: obtener estadísticas descriptivas)
            analisis_descriptivo = df.describe()

            # Mostrar estadísticas descriptivas
            print("Estadísticas Descriptivas:")
            print(analisis_descriptivo)

            # Visualizar los datos (ejemplo: gráfico de dispersión)
            plt.scatter(df.index, df['datos'])
            plt.title("Gráfico de Dispersión")
            plt.xlabel("Índice de Datos")
            plt.ylabel("Cantidad")
            plt.show()

            # Cerrar la conexión
            conn.close()

        
        elif op == 4:
              
            conn = psycopg2.connect(
                    dbname='empresas',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 
            consulta_sql = "SELECT * FROM empresa;"
            df = pd.read_sql_query(consulta_sql, conn)

            consulta_sql2 = "SELECT * FROM empresa2;"
            df2 = pd.read_sql_query(consulta_sql2, conn)

            consulta_sql3 = "SELECT * FROM empresa3;"
            df3 = pd.read_sql_query(consulta_sql3, conn)

            # Mostrar los datos como una tabla utilizando pandas
            print("Datos de la Tabla Google:")
            print(df)
            print("Datos de la Tabla Cementos progresos:")
            print(df2)
            print("Datos de la Tabla INTEL:")
            print(df3)

            # Cerrar la conexión
            conn.close()



        elif op == 5:
              
              break

def opcion9():

    
    while True:

        print("Menu de Opciones:")
        print("1. Ingresar productos")
        print("2. actualizar")
        print("3. vender")
        print("4. Generar informe de ventas en tabla")
        print("5. Salir")


        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")

        if op == 1:
            nombre = input("Ingrese su producto : ")
            precio = input("Ingrese su precio : ")

            cantidad = input("ingrese su cantidad : ")

            conn = psycopg2.connect(
                    dbname='problema9',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 
           
            try:
                        # Preparar la instrucción SQL para la inserción
                            Ins1 = 'INSERT INTO productos (nombre,precio,cantidad) VALUES (%s,%s,%s);'  # %s es un marcador de posición para el valor
                            
                            
                            Instruccion = cur.mogrify(Ins1, (nombre,precio,cantidad))

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
        elif op == 2:
            
            conn = psycopg2.connect(
                    dbname='problema9',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto
                nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ")

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM productos WHERE nombre = %s;", (nombre_producto,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")
                else:
                    # Solicitar al usuario los nuevos valores
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

                    # Sentencia SQL de actualización
                    sql_actualizacion = """
                        UPDATE productos
                        SET precio = %s, cantidad = %s
                        WHERE nombre = %s;
                    """

                    # Ejecutar la actualización
                    cur.execute(sql_actualizacion, (nuevo_precio, nueva_cantidad, nombre_producto))

                    # Confirmar la transacción
                    conn.commit()

                    print(f"Se ha actualizado la información del producto '{nombre_producto}'.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()











        elif op == 3:
        
            conn = psycopg2.connect(
                    dbname='problema9',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 

            try:
                # Solicitar al usuario el nombre del producto
                nombre_producto = input("Ingrese el nombre del producto que desea vender: ")

                # Verificar si el producto existe antes de continuar
                cur.execute("SELECT COUNT(*) FROM productos WHERE nombre = %s;", (nombre_producto,))
                cantidad_productos = cur.fetchone()[0]

                if cantidad_productos == 0:
                    print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")
                else:
                    # Solicitar al usuario la cantidad que desea vender
                    cantidad_a_vender = int(input("Ingrese la cantidad que desea vender: "))

                    # Verificar si hay suficiente cantidad en el inventario
                    cur.execute("SELECT cantidad FROM productos WHERE nombre = %s;", (nombre_producto,))
                    cantidad_actual = int(cur.fetchone()[0])

                    if cantidad_a_vender > cantidad_actual:
                        print(f"No hay suficiente cantidad en inventario para vender {cantidad_a_vender} unidades.")
                    else:
                        # Actualizar la cantidad en el inventario
                        nueva_cantidad = cantidad_actual - cantidad_a_vender
                        cur.execute("UPDATE productos SET cantidad = %s WHERE nombre = %s;", (nueva_cantidad, nombre_producto))

                        # Confirmar la transacción
                        conn.commit()

                        print(f"Se han vendido {cantidad_a_vender} unidades del producto '{nombre_producto}'. Nuevo inventario: {nueva_cantidad} unidades.")

            except psycopg2.Error as e:
                print(f"Error durante la conexión a la DB. Consulte el error: {e}")

            finally:
                # Cerrar la conexión
                cur.close()
                conn.close()
                
        elif op == 4:

            conn = psycopg2.connect(
                    dbname='problema9',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 
            consulta_sql = "SELECT * FROM productos;"
            df = pd.read_sql_query(consulta_sql, conn)

            
            # Mostrar los datos como una tabla utilizando pandas
            print("Informes de ventas:")
            print(df)
           

            # Cerrar la conexión
            conn.close()
        elif op == 5:

            break

def opcion10():




      while True: 
            

            while True:
                      buscar = input("Informacion del producto  : ")
                      if buscar.isalpha():
                           break
                      else:
                           print("Debe ser carcter ")

             
            if buscar == "block":
                

                conn = psycopg2.connect(
                    dbname='problema10',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
                cur = conn.cursor() 
                try:
                    # Consulta SQL para obtener la cantidad de arena
                    consulta_sql = "SELECT cantidad FROM optimizar WHERE nombre = 'arena';"

                    # Ejecutar la consulta
                    cur.execute(consulta_sql)
                    cantidad_arena_str = cur.fetchone()[0]

                    # Convertir la cantidad de arena a entero
                    cantidad_arena = int(cantidad_arena_str)

                    # Calcular la cantidad de bloques que se pueden fabricar
                    bloques_disponibles = cantidad_arena // 2  # Usamos "//" para la división entera

                    # Mostrar el resultado
                    print(f"Con {cantidad_arena} unidades de arena, puedes fabricar {bloques_disponibles} bloques.")

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la base de datos. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()

        

            elif buscar == "salir":
                  
                  break
def opcion11():
     while True:

        print("Menu de Opciones:")
        print("1. Desplegar lista de canciones")
        print("2. Buscar por artita ")
        print("3. Buscar por cancion")
        print("4. salir")
        


        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")

        if op == 1:
            conn = psycopg2.connect(
                    dbname='canciones',
                    user='postgres',
                    password='1234',
                    host='localhost',
                    port='5432'
                )
            cur = conn.cursor() 
            consulta_sql = "SELECT * FROM tablacancion;"
            df = pd.read_sql_query(consulta_sql, conn)
            # Mostrar los datos como una tabla utilizando pandas
            print("Lista de canciones :")
            print(df)
           

            # Cerrar la conexión
            conn.close()
        elif op == 2:
            
                conn = psycopg2.connect(
                        dbname='canciones',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432'
                    )
                cur = conn.cursor() 
                artista_buscar = input('Ingrese el nombre del artista: ')

                try:
                    # Consulta SQL para obtener información del artista
                    consulta_sql = f"SELECT * FROM tablacancion WHERE artista = '{artista_buscar}';"

                    # Ejecutar la consulta
                    cur.execute(consulta_sql)

                    # Obtener los resultados
                    resultados = cur.fetchall()

                    if resultados:
                        for resultado in resultados:
                            print(f"Artista: {resultado[1]}\nCanción: {resultado[2]}\nLetra:\n{resultado[3]}\n")
                    else:
                        print(f"No se encontraron resultados para el artista {artista_buscar}.")

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la base de datos. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()











        elif op == 3:
          
                conn = psycopg2.connect(
                        dbname='canciones',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432'
                    )
                cur = conn.cursor() 
                # Solicitar al usuario que ingrese el nombre de la canción
                

                cancion_buscar = input('Ingrese el nombre de la canción: ')

                try:
                    # Consulta SQL para obtener información de la canción
                    consulta_sql = f"SELECT * FROM tablacancion WHERE cancion = '{cancion_buscar}';"

                    # Ejecutar la consulta
                    cur.execute(consulta_sql)

                    # Obtener los resultados
                    resultados = cur.fetchall()

                    if resultados:
                        for resultado in resultados:
                            print(f"Artista: {resultado[1]}\nCanción: {resultado[2]}\nLetra:\n{resultado[3]}\n")
                    else:
                        print(f"No se encontraron resultados para la canción {cancion_buscar}.")

                except psycopg2.Error as e:
                    print(f"Error durante la conexión a la base de datos. Consulte el error: {e}")

                finally:
                    # Cerrar el cursor y la conexión
                    cur.close()
                    conn.close()
                
        elif op == 4:

            break
    
def opcion12():

    while True:
         
        print("Menu de Opciones:")
        print("1. Jugar")
        print("2. Instruciones ")
        print("3. Ver Preguntas")
        print("4. salir")
        
        

        while True:
                try:
                     op = int(input("ingres opcion "))
                     break
                except ValueError:
                     
                     print("Deber ser numerico la opcion ")

        if op == 1:
             

            conn = psycopg2.connect(
                        dbname='problema12',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432'
                    )
            cur = conn.cursor() 
            # Realiza una consulta para obtener preguntas y respuestas
            cur.execute("SELECT pregunta, respuesta FROM juego;")
            preguntas_respuestas = cur.fetchall()

            # Inicializa el puntaje del usuario
            puntaje = 0
            puntaje_objetivo = 5

            # Baraja aleatoriamente las preguntas
            random.shuffle(preguntas_respuestas)

            # Presenta preguntas hasta que el usuario alcance el puntaje objetivo
            for pregunta, respuesta in preguntas_respuestas:
                print(f"Pregunta: {pregunta}")
                respuesta_usuario = input("Respuesta (Verdadero o Falso): ").lower()

                if respuesta_usuario == respuesta.lower():
                    print(" Ganaste 1 punto.")
                    puntaje += 1
                else:
                    print("Incorrecto. Perdistes puntos.")

                print(f"puntaje actual: {puntaje}")

                if puntaje == puntaje_objetivo:
                    print(f"Felicidades, tu puntaje es {puntaje_objetivo} puntos.")
                    break

            # Cierra la conexión a la base de datos
            cur.close()
            conn.close()
        elif op == 2:
             
             print(" ")
             print(" Las instrcciones son : \n se presentaran una serie de pregunatas \n cada pregunta si aciertas sumaras un punto \n de lo contrario perderas 1 punto tienes 3 vidas")
             print(" ")
        elif op == 3:
            conn = psycopg2.connect(
                        dbname='problema12',
                        user='postgres',
                        password='1234',
                        host='localhost',
                        port='5432'
                    )
            cur = conn.cursor() 

            consulta_sql = "SELECT * FROM juego;"
            df = pd.read_sql_query(consulta_sql, conn)
            # Mostrar los datos como una tabla utilizando pandas
            print("Lista de preguntas :")
            print(df)

        elif op == 4:
             break




while True:


    print("Menu de Opciones:")
    print("1.Programa de registro de estudiantes")
    print("2.Programa de seguimiento de presupuesto personal gastos")
    print("3.Programa de gestión de inventario")
    print("4.Programa de seguimiento de pedidos")
    print("5.Programa de monitoreo de ventas")
    print("6.Programa de análisis de datos de sensores")
    print("7.Sistema de recomendación de películas")
    print("8.Programa de análisis financiero")
    print("9.Sistema de gestión de inventario")
    print("10.Sistema de planificación de producción")
    print("11. Buscador de canciones")
    print("12. Concurso")
    print("13. Salir")

    while True:
               
            try:
               seleccion = int(input("ingrese una opcion : "))
               break
            except ValueError:
                 print("Debe ser valor numerico ")

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
        exit()