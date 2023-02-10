#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_factory, Persistencia_usuari_mySql

"""
    Persistencia_factory_mySql.py
    Classe que defineix la interficie amb la fàbrica de persistencia per a mySql.
"""

class Persistencia_factory_mySql(Persistencia_factory.Persistencia_factory):
    def __init__(self, host, usuari, paraula_pas, base_dades, configurador):
        self.host = host
        self.usuari = usuari
        self.paraula_pas = paraula_pas
        self.base_dades = base_dades
        self.configurador = configurador

    def get_Persistencia_usuari_factory(self):
        return Persistencia_usuari_mySql.Persistencia_usuari_mySql(
            self.host, 
            self.usuari, 
            self.paraula_pas, 
            self.base_dades, 
            self.configurador
            )

    