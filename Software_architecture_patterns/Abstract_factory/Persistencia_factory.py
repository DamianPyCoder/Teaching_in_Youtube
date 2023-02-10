#!/usr/bin/python3
# -*- coding: utf-8 -*-

import abc

"""
    Persistencia_factory.py
    Classe abstracta que defineix la interficie amb les fàbriques concretes de persistència.
"""

class Persistencia_factory(abc.ABC):
    @abc.abstractmethod
    def get_Persistencia_usuari_factory(self):
        pass

