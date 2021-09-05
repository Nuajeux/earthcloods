#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:05:44 2020

@author: mathsoluce
"""
import sqlite3
import cgi

formulaire = cgi.FieldStorage()



nomPays = formulaire.getvalue('nomPays')


conn = sqlite3.connect('baseDePays.db')
curseur = conn.execute("SELECT nomPays,capitale,image,drapo,continent,pop,surface,gouv,chef,devise from Pays WHERE nomPays = (?)",(nomPays,))


for line in curseur:
    if nomPays == line[0]:
        nomPays = line[0]
        image = line[2]
        capitale = line[1]
        drapo = line[3]
        continent = line[4]
        pop = line[5]
        surface = line[6]
        gouv = line[7]
        chef = line[8]
        devise = line[9]
    else:
        pagedebut = pagedebut.replace("<!error>",erreur)



conn.close()

#affichage

pagedebut= '''
<html>
    <head>
        <title>EarthClouds</title>
        <link rel = "icon" href = "images/geography.png"  type = "image/x-icon">
        <link rel="stylesheet" type="text/css" href="css/main.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Londrina+Solid:wght@300&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz&display=swap" rel="stylesheet"> 
    </head>
    <body>
        <div class="banner">
            <div class='titre'>
            <img class="logo "src="images/geography.png" alt="logo">
            <h1>EarthClouds</h1>
            </div>
            <nav>
                <ul class="navRight" >
                    <li onclick="window.location='index.py'">Présentation</li>
                    <li onclick="window.location='pays.py'">Pays</li>
                    <li onclick="window.location='jeu.py'">Jouer</li>
                </ul>
            </nav>
        </div>
        <div class="quoi">
        <p class="entrez"> Entrez le nom d'un pays</p>
        <form action="recherchePays.py" method='get' class="nomPays">
            <input type="text" name="nomPays" placeholder="Pays"/>
            <input class="btn" style="margin-top:0px; font-size: 20px;" id="recherche" value="Rechercher" type="submit">
        </form>
        <!error>
        </div>
        <!remplacer>
    </body>
</html>
'''

pagemil= '''
    <div style="margin-top: -16;" class="back">
        <img class="fondd" src="imig" alt='capachpa'>
        <div class="info">
            <div class="tete">
            <img class='drapo' src="drapos" alt="drapomachpo">
            <p class='imgPP' style="margin-bottom: 0px;">•nomPays</p>
            </div>
            <div style="display: flex;"><img style="margin-top: 14px; height: 22px;"src="css/images/world.png"><p style="font-weight: bold; margin-bottom: 0px;">•Informations géographiques:</p></div>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Capitale:</span> capitale</p>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Continent:</span> continent</p>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Population:</span> pop</p>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Surface:</span> surface</p>
            <div style="display: flex;"><img style="margin-top: 0px; height: 22px;"src="css/images/golded.png"><p style="font-weight: bold; margin-bottom: 0px; margin-top: 0px;">•Informations gouvernementales:</p></div>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Gouvernement:</span> guv</p>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Gouverneur:</span> chef</p>
            <p style="margin-top: 0px; margin-bottom: 4px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Devise:</span> devise</p>
        </div>
    </div>
'''

erreur ='''
    <p>Ce pays n'est pas encore disponible. (Pays européens seulement),(ce site étant codé avec certaines contraintes, les pays doivent être entrés sans accents)</p>
'''
pagemil = pagemil.replace("imig",image)
pagemil = pagemil.replace("nomPays",nomPays)
pagemil = pagemil.replace("drapos",drapo)
pagemil = pagemil.replace("capitale",capitale)
pagemil = pagemil.replace("continent",continent)
pagemil = pagemil.replace("pop",pop)
pagemil = pagemil.replace("surface",str(surface))
pagemil = pagemil.replace("guv",gouv)
pagemil = pagemil.replace("chef",chef)
pagemil = pagemil.replace("devise",devise)
pagedebut = pagedebut.replace("<!remplacer>",pagemil)

#str.encode("utf-8")



print(pagedebut)
