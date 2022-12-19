import xml.dom.minidom


def get_alumnes(info_dom):
    alumnes = []
    classe = info_dom.getElementsByTagName("alumne")
    for alumne in classe:
        nom = alumne.getElementsByTagName("nom")[0]
        cognom = alumne.getElementsByTagName("cognom")[0]
        grup = alumne.getElementsByTagName("grup")[0]
        alumnes.append({
            "nom": getText(nom.childNodes),
            "cognom": getText(cognom.childNodes),
            "grup": getText(grup.childNodes)
        })
    return alumnes


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def main():
    document = """<class>
    <alumne>
      <nom>Xavi</nom>
      <cognom>Quesada</cognom>
      <grup>DAM 2</grup>
    </alumne>
    <alumne>
      <nom>Pere</nom>
      <cognom>Llull</cognom>
      <grup>DAM 2</grup>
    </alumne>
    <alumne>
      <nom>Alicia</nom>
      <cognom>Galan</cognom>
      <grup>DAM 2</grup>
    </alumne>
</class>
    """

    alumnes = xml.dom.minidom.parseString(document)
    alumnes_array = get_alumnes(alumnes)
    print(alumnes_array)


if __name__ == "__main__":
    main()

