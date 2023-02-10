#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import os
import Persistencia_factory_mySql, Persistencia_factory_redis

"""
    Configurador.py
    És la classe encarregada de llegir el fitxer
    de configuració i obtenir les classes concretes
    adients a la nostra aplicació.
"""
class Configurador:
    def __init__(self, path_fitxer_configuracio):
        self.yaml_config = path_fitxer_configuracio
        self.config = {}
        with open(path_fitxer_configuracio, 'r') as conf:
            self.config = yaml.safe_load(conf)
    
    def get_config(self):
        return self.config

    def get_Persistencia_factory(self):
        motor = self.config["base de dades"]["motor"].lower().strip()
        if motor == "mysql":
            host = self.config["base de dades"]["host"]
            usuari = self.config["base de dades"]["user"]
            paraula_pas = self.config["base de dades"]["password"]
            base_dades = self.config["base de dades"]["base_dades"]
            return Persistencia_factory_mySql.Persistencia_factory_mySql(
                host,
                usuari,
                paraula_pas,
                base_dades,
                self
            )
        elif motor == "redis":
            host = self.config["base de dades"]["host"]
            return Persistencia_factory_redis.Persistencia_factory_redis(
                host,
                self
            )
