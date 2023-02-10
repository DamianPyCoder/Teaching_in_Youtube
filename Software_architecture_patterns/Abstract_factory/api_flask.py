#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, Response, make_response, render_template, request
import App_llista_compra

app = Flask(__name__,
                static_url_path='/html/', 
                static_folder='html'
            )
app_llista_compra = App_llista_compra.App_llista_compra()


@app.route("/")
def hello():
    return jsonify({"missatge": "Benvingut a la llista de la compra!"}), 200


@app.route("/registre/<nom_usuari>/<password>")
def registre(nom_usuari, password):
    resultat = app_llista_compra.registre_usuari(nom_usuari, password)
    return jsonify(resultat), resultat["estatus"]


@app.route("/login/<nom_usuari>/<password>")
def login(nom_usuari, password):
    resultat = app_llista_compra.login_usuari(nom_usuari, password)
    response = make_response(jsonify(resultat), resultat["estatus"])
    if resultat["estatus"] == 200:
        response.headers['X-API-KEY'] = resultat["api_key"]
    return response


@app.route("/restricted/<recurs>")
def restricted(recurs):

    return render_template(recurs)


@app.route("/llista")
def llista():
    api_key = request.headers['X-API-KEY']
    usuari_from_api_key = app_llista_compra.get_usuari_from_api_key(api_key)
    if usuari_from_api_key:
        return jsonify(usuari_from_api_key.get_llista())
    return jsonify({"missatge": "NO autoritzat!", "estatus": 401}), 401

if __name__ == "__main__":
    app.run()