#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Aquest programa accedeix a un volcat d'una base de dades de pel�licules i genera una p�gina HTML
on mostra la informaci.
"""

import json


PATH_HTML = "C:/Users/damia/Desktop/DAM2022-23/M6/movies.html"
PATH_JSON = "C:/Users/damia/Desktop/DAM2022-23/M6/movies.json"


def get_informacio_pelicules(PATH_JSON):
    with open (PATH_JSON) as archivo:
        database = json.load(archivo)
    return database




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
        html.write('<th>Punts</th>')
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
            html.write(f'<td>{pelicula["punts"]}</td>')
            html.write(f'<td>{pelicula["vots"]}</td>')
            html.write('</tr>')
        html.write('</table>')
        html.write('</body>\n')
        html.write('</html>\n')


def main():
    pelis = get_informacio_pelicules(PATH_JSON)
    genera_taula(pelis, PATH_HTML)
    


if __name__ == "__main__":
    main()