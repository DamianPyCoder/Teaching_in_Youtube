import xml.dom.minidom
import io

def get_peliculas(info_dom):
    peliculas = []
    classe = info_dom.getElementsByTagName("pelicula")
    for pelicula in classe:
        titol = pelicula.getElementsByTagName("titol")[0]
        any = pelicula.getElementsByTagName("any")[0]
        puntuacio = pelicula.getElementsByTagName("puntuacio")[0]
        vots = pelicula.getElementsByTagName("vots")[0]
        peliculas.append({
            "id": getText(pelicula._attrs["id"].childNodes),
            "titol": getText(titol.childNodes),
            "any": getText(any.childNodes),
            "puntuacio": getText(puntuacio.childNodes),
            "vots": getText(vots.childNodes)
        })
    return peliculas


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def genera_taula(pelis, path_web):
    odd = False
    with open (path_web, "wt") as html:
        html.write('<!DOCTYPE html>\n')
        html.write('<html lang="ca">\n')
        html.write('<head>\n')
        html.write('<meta charset="UTF-8"><title>PELICULAS</title><meta name="viewport" content="width=device-width,initial-scale=1">\n')
        html.write('<style>')
        html.write('.odd { background-color: lavender;}')
        html.write('.even { background-color: wheat;}')
        html.write('</style>')
        html.write('</head>\n')
        html.write('<body>\n')
        html.write('<h1>BASE DE DATOS DE PELIS</h1>\n')
        html.write('<table>')
        html.write('<tr>')
        html.write('<th>Id</th>')
        html.write('<th>Titol</th>')
        html.write('<th>Any</th>')
        html.write('<th>Punts</th>')
        html.write('<th>Vots</th>')
        html.write('</tr>')
        for pelicula in pelis:
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
    document = """<cataleg>
    <pelicula id="1">
        <titol>'Star Wars'</titol>
        <any>1977</any>
        <puntuacio>8.9</puntuacio>
        <vots>8789</vots>
    </pelicula>
    <pelicula id="2">
        <titol>'Pulp Fiction'</titol>
        <any>1994</any>
        <puntuacio>8.4</puntuacio>
        <vots>8878</vots>
    </pelicula>
</cataleg>"""

with open('movies.xml', 'rb') as inf:
    documentD = inf.read()

    peliculas = xml.dom.minidom.parseString(documentD)
    peliculas_array = get_peliculas(peliculas)
    # print(peliculas_array)
    genera_taula(peliculas_array,"./movies.html")


if __name__ == "__main__":
    main()

