#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Un compañero de su equipo de desarrollo ha empezado un proyecto para obtener información de un archivo sql (producto de hacer un dump de una base de datos de películas), pero ha sido asignado a otro proyecto y ahora le toca a vosotros terminar su trabajo.
Dispone del archivo sql: 'BBDDPeliculas_utf8.sql' que será su fuente de información y debe generar una página web como la que se muestra en la imagen adjunta con una tabla que muestra los campos de las películas que hay en la base de datos.
Como puede apreciar, el programa ya tiene la estructura hecha y falta crear el patrón de expresión regular que haga match con las líneas que contienen la información relativa a las películas y también falta implementar dos funciones:
1.- def get_informacio_pelicules(path_db, patro_busqueda): Que debe devolver un array de diccionarios python donde cada diccionario contendrá los siguientes campos:
     - id
     - título
     - año
     - puntuación
     - votos
2.- def genera_taula(pelicules, path_web): El array obtenido en la función definida en el punto anterior será uno de los parámetros de entrada de esta función que escribirá el archivo HTMl.

Como puede observar en el código fuente que ha dejado su compañero, está marcado con un comentario '# TODO' todas aquellas partes del programa incumplidas que necesitan que las llene de código.

Pistas:
     Para utilizar RegEx en python debe importar la biblioteca: 're'
     La función match = re.search(patrón_regex, texto) devuelve un objeto con el resultado del match o None si no ha hecho match.
     La función match.group(x) devuelve el grupo x del match con el patrón en el que 0 es todo el match ya partir del 1 están los grupos definidos en el patrón.
"""

import re

PATH_DATABASE = "./Estructures/Exercicis/BBDDPeliculas_utf8.sql"
PATH_HTML = "./movies.html"


def get_informacio_pelicules(path_db, patro_busqueda):
    pelis = []
    with open(PATH_DATABASE) as database:
        linia = database.readline()
        while linia != "":
            match = re.search(patro_busqueda, linia)
            if match is not None:
                pelicula = {}
                pelicula['id'] = match.group(1)
                pelicula['titol'] = match.group(2)
                pelicula['any'] = match.group(4)
                pelicula['puntuacio'] = match.group(5)
                pelicula['vots'] = match.group(3)
                pelis.append(pelicula)
            linia = database.readline()
    return pelis


def genera_taula(pelicules, path_web):
    odd = False
    with open (PATH_HTML, "wt") as html:
        html.write('<!DOCTYPE html>\n')
        html.write('<html lang="ca">\n')
        html.write('<head>\n')
        html.write('<meta charset="UTF-8"><title>Pel·licules</title><meta name="viewport" content="width=device-width,initial-scale=1">\n')
        html.write('<style>')
        html.write('.odd { background-color: lavender;}')
        html.write('.even { background-color: wheat;}')
        html.write('</style>')
        html.write('</head>\n')
        html.write('<body>\n')
        html.write('<h1>Base de dades de pel·licules</h1>\n')
        html.write('<table>')
        html.write('<tr>')
        html.write('<th>Id</th>')
        html.write('<th>Titol</th>')
        html.write('<th>Any</th>')
        html.write('<th>Puntuació</th>')
        html.write('<th>Vots</th>')
        html.write('</tr>')
        for pelicula in pelicules:
            odd = not odd
            if odd:
                html.write('<tr class="odd">')
            else:
                html.write('<tr class="even">')
            html.write(f'<td>{pelicula["id"]}</td>')
            html.write(f'<td>{pelicula["titol"]}</td>')
            html.write(f'<td>{pelicula["any"]}</td>')
            html.write(f'<td>{pelicula["puntuacio"]}</td>')
            html.write(f'<td>{pelicula["vots"]}</td>')
            html.write('</tr>')
        html.write('</table>')
        html.write('</body>\n')
        html.write('</html>\n')


def main():
    patro = "INSERT\s*INTO\s*PELICULA\s*VALUES\s*\((\d+),('.*'),(\d+),([\d.]+),(\d+)\);"
    pelis = get_informacio_pelicules(PATH_DATABASE, patro)
    genera_taula(pelis, PATH_HTML)
    


if __name__ == "__main__":
    main()