#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari

class Usuari:
    def __init__(self, persistencia, id, user, password_hash):
        self.id = id
        self.user = user
        self.password_hash = password_hash
        assert issubclass(type(persistencia), Persistencia_usuari.Persistencia_usuari)
        self.persistencia = persistencia


    def get_nom(self):
        return self.user
    
    def get_password_hash(self):
        return self.password_hash

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def desa(self):
        self.id = self.persistencia.desa(self)
        return self

    def delete(self):
        return self.persistencia.delete(self.get_id())

    def set_sessio(self, id_sessio):
        return self.persistencia.set_sessio(id_sessio, self)

    def get_llista(self):
        # TODO implement get_llista()
        # TODO tractar la llista de veritat, això és MOCK
        return [
            {"qty": 3, "article": {"categoria": "begudes", "nom": "Aigua amb gas"}},
            {"qty": 6, "article": {"categoria": "frescos", "nom": "Síndries"}},
            {"qty": 2, "article": {"categoria": "refrigerats", "nom": "Yogurt de llet de cabra"}},
            {"qty": 1, "article": {"categoria": "hogar", "nom": "Coixí"}}
        ]
