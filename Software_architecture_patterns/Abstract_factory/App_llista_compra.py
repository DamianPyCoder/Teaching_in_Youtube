#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Configurador, Usuari
import os
import bcrypt
import uuid


"""
    Punt únic d'entrada a la nostra aplicació de la llista de la compra.
"""

FITXER_CONFIGURACIO = "configuracio.yml"
class App_llista_compra:
    def __init__(self):
        self.configurador = Configurador.Configurador(
            os.path.join(
                os.path.dirname(__file__), 
                FITXER_CONFIGURACIO
                )
            )
        self.usuaris = []

    def get_configurador(self):
        return self.configurador

    def create_usuari(self, user, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        nou_usuari = Usuari.Usuari(self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory(), None, user, password_hash)
        nou_usuari = nou_usuari.desa()
        self.usuaris.append(nou_usuari)
        return nou_usuari

    def registre_usuari(self, nom, password):
        if nom in [x.get_nom() for x in self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory().get_llista()]:
            return {"estatus": 409, "missatge": "L'usuari ja existeix!"}
        usuari = self.create_usuari(nom, password)
        if usuari is None:
            return {"estatus": 204, "missatge": "L'usuari no s'ha creat"}
        return {
            "estatus": 201, 
            "missatge": "Usuari creat!", 
            "usuari": {
                "id": usuari.get_id(),
                "nom": usuari.get_nom() 
                }
            }

    def login_usuari(self, nom, password):
        llista_usuari = [x for x in self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory().get_llista() if x.get_nom() == nom]
        if len(llista_usuari) > 0:
            usuari = llista_usuari[0]
            if bcrypt.checkpw(password.encode(), usuari.get_password_hash().encode()):
                return {"estatus": 200, "missatge": "OK", "api_key": self.__crea_sessio(usuari)}
        return {"estatus": 404, "missatge": "L'usuari no existeix o la paraula de pas no és correcta."}

    def get_usuari_from_api_key(self, api_key):
        usuari = self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory().get_from_apikey(api_key)
        return usuari

    def __crea_sessio(self, usuari):
        session_uuid = str(uuid.uuid4())
        usuari.set_sessio(session_uuid)
        return session_uuid


if __name__ == "__main__":
    # proves locals
    app = App_llista_compra()
    print("[config] Base de dades:\n\t", app.get_configurador().get_config()["base de dades"])
    nou_usuari = app.create_usuari('Alex', '1234')
    print(nou_usuari.get_id())
    print(nou_usuari.get_nom())
    print(nou_usuari.get_password_hash())
    print("Llista d'usuaris:")
    print("-----")
    for usuari in app.get_configurador().get_Persistencia_factory().get_Persistencia_usuari_factory().get_llista():
        print(usuari.get_id(), usuari.get_nom())