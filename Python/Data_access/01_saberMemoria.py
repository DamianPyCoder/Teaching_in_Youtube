#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Haremos un programa que lea la información de la memoria del sistema en /proc/meminfo y modifique el archivo plantilla.html 
para mostrar los datos de la memoria total, disponible y libre. 
En lugar de sobrescribir el archivo plantilla.html haremos un nuevo archivo llamado: resultado_memoria.html
"""

def get_valor_de_linea_meminfo(linea_meminfo):
    return linea_meminfo.split(':')[1].strip()


def main():
    memoria_total = ""
    memoria_lliure = ""
    memoria_disponible = ""
    with open("/proc/meminfo") as meminfo:
        meminfo_linees = meminfo.readlines()
    for linea in meminfo_linees:
        if linea.find("MemTotal:") >= 0:
            memoria_total = get_valor_de_linea_meminfo(linea)
        elif linea.find("MemFree:") >= 0:
            memoria_lliure = get_valor_de_linea_meminfo(linea)
        elif linea.find("MemAvailable:") >= 0:
            memoria_disponible = get_valor_de_linea_meminfo(linea)
    meminfo_linees = None
    with open("plantilla.html") as descriptor_plantilla:
        linees_plantilla = descriptor_plantilla.readlines()
    with open("resultat_memoria.html", "wt") as resultat:
        for linea in linees_plantilla:
            if linea.find("{{MTotal}}") >= 0:
                linea = linea.replace("{{MTotal}}", memoria_total)
            if linea.find("{{MDisp}}") >= 0:
                linea = linea.replace("{{MDisp}}", memoria_disponible)
            if linea.find("{{MLliure}}") >= 0:
                linea = linea.replace("{{MLliure}}", memoria_lliure)
            resultat.write(linea)

if __name__ == "__main__":
    main()