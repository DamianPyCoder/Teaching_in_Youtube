#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
"""
Nos han encargado un programa que debe guardar la información de los usuarios de forma permanente.

Hemos pensado en utilizar un archivo de texto plano para implementar esta tarea. El programa estará estructurado en funciones:

     def guarda_usuario(dny, nombre, apellido, fecha_nacimiento, teléfono)
     def lee_usuarios(path_archivo)

El campo DNI funciona como clave primaria de una base de datos, debe ser único y no se puede omitir.
Debe justificar el formato utilizado para guardar los datos.
La interacción con el usuario se realizará mediante un menú con opciones numéricas que se mostrará por consola.
La ruta del archivo de datos estará definida en una variable global llamada PATH_DADES = "./dades.txt"
"""

__author__ = "X. Quesada"
__license__ = "GPL3"

PATH_DADES = "./dades.txt"
usuaris = []

def show_menu():
    print("0. Sortir")
    print("1. Llegir usuaris")
    print("2. Afegir usuari")


def llegir_usuaris():
    global PATH_DADES
    global usuaris
    try:
        with open(PATH_DADES, 'r') as f:
            usuaris = json.loads(f.read())
    except FileNotFoundError:
        pass

def mostrar_usuaris():
    global usuaris
    llegir_usuaris()
    print(json.dumps(usuaris, sort_keys=True, indent=2))


def afegir_usuari():
    llegir_usuaris()
    dni = input("Introdueix DNI: ")
    nom = input("Introdueix nom: ")
    cognom = input("Introdueix cognom: ")
    telefon = input("Introdueix telèfon: ")
    usuari_desat = list(filter(lambda u : u["dni"] == dni, usuaris))
    
    if len(usuari_desat) > 0:
        selected_user = usuari_desat[0]
        selected_user["nom"] = nom
        selected_user["cognom"] = cognom
        selected_user["telefon"] = telefon
    else:
        usuaris.append({"dni": dni, "nom": nom, "cognom": cognom, "telefon": telefon})
    
    with open(PATH_DADES, 'w') as f:
        f.write(json.dumps(usuaris))


def procesa_opcio(option):
    return {
        "0": lambda : print("Fins aviat!"),
        "1": mostrar_usuaris,
        "2": afegir_usuari
    }.get(option, lambda : print("Opció incorrecta."))    


def main():
    option = None
    while option != "0":
        show_menu()
        option = input("Selecciona una opció: ")
        procesa_opcio(option)()
    
if __name__ == "__main__":
    main()
