import sqlite3
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def solo_letras(mensaje):
    while True:
        nombre = input(mensaje)
        if nombre.isalpha():
            return nombre.capitalize()
        else:
            print("Por favor solo utilize letras de A hasta Z.")
            
def solo_numeros(mensaje):
    while True:
        try:
            ingreso = int(input(mensaje))
            return ingreso
        except ValueError:
            print("Opcion incorrecta.")
    
def create_table():
    try:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            precio REAL NOT NULL)''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            
def add():
    
    id = solo_numeros("ID: ")
    name = solo_letras("NOMBRE: ")
    price = solo_numeros("PRECIO: ")
    
    try:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
    
        cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", (id, name, price))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def view():
    try:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM productos")
        vista = cursor.fetchall()
        for producto in vista:
            print(producto)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            
create_table()

while True:
    clear()
    print("Menu")
    print("1 - Agregar Productos")
    print("2 - Ver Productos")
    print("3 - Salir")

    opcion = solo_numeros("> ")

    if opcion == 1:
        add()
    elif opcion == 2:
        view()
    elif opcion == 3:
        break
    else:
        print("La opcion que elejiste no existe.")
        
    input("Presiona Enter para continuar...")
