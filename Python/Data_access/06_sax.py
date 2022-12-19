#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.sax

class AlumnesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.llistat_alumnes = []
        self.llistat_etiquetes = []
        self.etiqueta_actual = ""
        self.nom = ""
        self.cognom = ""
        self.grup = ""

    
    def startElement(self, name, attrs):
        self.llistat_etiquetes.append(name)
        self.etiqueta_actual = name
        if name == "alumne":
            print("[v] Acabem d'entrar a un alumne nou.")
            self.nom = ""
            self.cognom = ""
            self.grup = ""

    def endElement(self, name):
        sortim_de = self.llistat_etiquetes.pop()
        if len(self.llistat_etiquetes) > 0:
            self.etiqueta_actual = self.llistat_etiquetes[-1]
        else:
            self.etiqueta_actual = ""
        if name == "alumne":
            print("[v] Acabem de sortir de l'alumne: ", self.nom, self.cognom)
            self.llistat_alumnes.append({
                "nom": self.nom,
                "cognom": self.cognom,
                "grup": self.grup
            })

    def characters(self, content):
        if self.etiqueta_actual == "nom":
            self.nom = content
        elif self.etiqueta_actual == "cognom":
            self.cognom = content
        elif self.etiqueta_actual == "grup":
            self.grup = content
        

def main():
    content = """<class>
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
    with open("./class_dam2.xml","w") as dam2:
        dam2.write(content)
    

if __name__ == "__main__":
    main()
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = AlumnesHandler()
    parser.setContentHandler(handler)
    parser.parse("./class_dam2.xml")
    print("Hem acabat de processar el fitxer XML.")
    print(handler.llistat_alumnes)