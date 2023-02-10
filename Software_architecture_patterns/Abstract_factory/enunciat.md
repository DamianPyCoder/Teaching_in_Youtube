---
title: M06 Accés a dades. Projecte Llista de la compra.
tags: DAM, M6
---

[Link en MarkDown](https://hackmd.io/@JdaXaviQ/HJ283-zPs)

# M06 Accés a dades. Projecte llista de la compra.
![](https://i.imgur.com/hythnPM.png)

## Introducció:
Segur que has anat alguna vegada a comprar i quan has tornat a casa te n’has adonat que se t’ha oblidat alguna cosa. 
Ens passa a tots. Però hem pensat en solucionar-ho per tal que no ens passi més. Així el que us demanem és el disseny d’una aplicació que ens ajudi amb la llista de la compra.
Evidentment la llista de la compra està formada per diferents articles que haurien d’estar organitzats per categories (com per exemple, fleca, peix, carn...) i de cada article en voldrem una determinada quantitat. Per posar un exemple, de la categoria begudes, voldria comprar llaunes de “cola loca”, en concret 12 llaunes.
D’aquesta manera quan anem a comprar i estiguem en un passadís o secció del
supermercat, a part de consultar tota la llista de la compra, podrem demanar a la aplicació que ens mostri només els articles que siguin de la categoria concreta (amb l’exemple anterior, podria consultar els articles de la categoria begudes).

## Descripció:
De moment començarem per realitzar el backend en forma d'API-RESTfull que podrà servir per a qualsevol tipus d'aplicació client, ja sigui una aplicació mòbil, una aplicació d'escriptori o una aplicació web.
La aplicació comença amb les següents categories precaarregades, però l'usuari podrà afegir, modificar o eliminar les categories que vulgui:
* Frescos
* Begudes
* Làctis
* Neteja
* Fruita i verdures

## Històries d'usuari:
id | Descripció | Importància | Cost
---|---|:---:|---:
1 | **[Tècnica]** Abans de començar necessitem  el diagrama de classes UML | 1000000 | 2h
2 | Com a usuari no registrat vull poder registrarme a la aplicació. | 1000 | 5h
3 | Com a usuari registrat vull poder identificar-me a la aplicació. | 1000 | 2h
4 | Com a usuari identificat vull poder afegir articles a qualsevol categoria existent | 900 | 0,5h
5 | Com a usuari identificat vull poder afegir registres d'articles existents a la meva llista | 800 | 0,5h
6 | Com a usuari identificat vull poder veure el contingut de la meva llista | 800 | 0,5h
7 | Com a usuari identificat vull poder veure el contingut de la meva llista filtrant per categoria | 800 | 0,5h

## Tecnologies a utilitzar:
En la primera verssió utilitzarem:
* Python com a llenguatge de programació
* Flask com a framework per a que sigui més fàcil generar una API REST.
* MariaDB o MySQL com a SGBD.

## Diagrama de classes:
```mermaid
classDiagram
    class App_llista_compra{
        - Configurador configuracio
        - Usuari usuaris[]
        + Usuari create_usuari(user, password)
        + Dictionary registre_usuari(nom, password)
        + Dictionary login_usuari(nom, password)
        + Usuari get_usuari_from_api_key(api_key):
    }

    class Configurador{
        Connexio_persistencia get_connexio_persistencia()
        Persistencia_usuari get_usuari_persistencia()
        Persistencia_llista get_persistencia_llista()
        Persistencia_registre get_persistencia_registre()
        Persistencia_article  get_persistencia_article()
        Persistencia_categoria get_persistencia_categoria()
    }

    class Usuari{
        - Configurador configurador
        - id
        - str user
        - str password_hash
        - Llista llista
        - Persistencia_usuari persistencia
        - Usuari desa()
        - delete()
        - str set_sessio()
        - Llista get_llista()
    }

    class Llista{
        - Configurador configurador
        - id
        - registres[] Registre
        - Persistencia_llista persistenci
    }

    class Registre{
        - Configurador configurador
        - id
        - int qty
        - Article article
        - Persistencia_registre persistencia
    }

    class Article{
        - Configurador configurador
        - id
        - str nom
        - Categoria categoria
        - Persistencia_article persistencia
    }

    class Categoria{
        - Configurador configurador
        - id
        - str nom
        - Persistencia_categoria persistencia
    }

    class Persistencia_usuari{
        <<interface>>
        + desa(usuari) 
        + Usuari get(id)
        + Usuari[] get_llista()
        + delete(id) 
        + str set_sessio(id_sessio, usuari)
        + Usuari get_from_apikey(id_sessio)
    }

    class Persistencia_llista{
        <<interface>>
        + desa(llista) 
        + Llista get(id)
    }

    class Persistencia_registre{
        <<interface>>
        + desa(registre) 
        + Registre get(id)
        + Registre[] get_llista(Llista)
        + delete_registre(id) 
    }

    class Persistencia_article{
        <<interface>>
        + desa(article) 
        + Article get(id)
        + Article[] get_llista(Usuari)
        + delete_article(id) 
    }

    class Persistencia_categoria{
        <<interface>>
        + desa(categoria) 
        + Categoria get(id)
        + Categoria[] get_llista(Usuari)
        + delete_categoria(id) 
    }

    class Persistencia_usuari_mySql
    class Persistencia_llista_mySql
    class Persistencia_registre_mySql
    class Persistencia_article_mySql
    class Persistencia_categoria_mySql

    App_llista_compra --> Usuari
    App_llista_compra --> Configurador
    Usuari --> Llista
    Usuari --> Persistencia_usuari
    Persistencia_usuari <|.. Persistencia_usuari_mySql
    Persistencia_usuari <|.. Persistencia_usuari_redis
    Persistencia_usuari <|.. Persistencia_usuari_sqlite
    Llista *-- Registre
    Llista --> Persistencia_llista
    Persistencia_llista <|.. Persistencia_llista_mySql
    Registre --> Article
    Registre --> Persistencia_registre
    Persistencia_registre <|.. Persistencia_registre_mySql
    Article --o Categoria
    Article --> Persistencia_article
    Persistencia_article <|.. Persistencia_article_mySql
    Categoria --> Persistencia_categoria
    Persistencia_categoria <|.. Persistencia_categoria_mySql
    Configurador --> Persistencia_Factory

```