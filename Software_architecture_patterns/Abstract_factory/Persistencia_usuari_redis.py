#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari, Usuari
import redis

class Persistencia_usuari_redis(Persistencia_usuari.Persistencia_usuari):
    def __init__(self, host, configurador):
        self.host = host
        self.configurador = configurador

    def get(self, id):
        id = id if type(id) is str else id.decode()
        db = self.__get_db_connection()
        key = 'usuari:' + id

        
        usuari_nom = db.hget(key, 'nom')
        usuari_nom = usuari_nom.decode() if usuari_nom else None
        if usuari_nom:
            usuari_password_hash = db.hget(key, 'password_hash').decode()
            resultat = Usuari.Usuari(
                self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory(), 
                id, 
                usuari_nom, 
                usuari_password_hash)
            return resultat
        db.quit()
        return None

    def get_from_apikey(self, id_sessio):
        db = self.__get_db_connection()
        id_usuari = db.get('sessio:' + id_sessio)

        if id_usuari:
            resultat = self.get(id_usuari)
            return resultat
        return None

    def desa(self, usuari):
        db = self.__get_db_connection()
        id = usuari.get_nom()
        key = 'usuari:'+id
        db.hset(key, 'id',  id)
        db.hset(key, 'nom',  usuari.get_nom())
        db.hset(key, 'password_hash',  usuari.get_password_hash())
        db.sadd('usuaris', id)
        db.quit()
        return id

    def get_llista(self):
        llista = []
        db = self.__get_db_connection()

        registres = db.smembers('usuaris')
        db.quit()
        for id in registres:
            llista.append(self.get(id))
        return llista

    def delete(self, id):
        db = self.__get_db_connection()
        db.srem('usuaris', id)
        db.delete('usuari:' + id)
        resultat = True
        db.quit()
        return resultat


    def __get_db_connection(self):
        return redis.Redis(
          host = self.host
          )

    def set_sessio(self, id_sessio, usuari):
        db = self.__get_db_connection()

        db.set('sessio:' + id_sessio, usuari.get_id())
        db.quit()
        return id_sessio