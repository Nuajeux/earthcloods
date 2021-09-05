#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:05:44 2020

@author: mathsoluce
"""
import sqlite3



#Pour les jeux affichage
conn = sqlite3.connect('basedePays.db')
curseur = conn.execute("SELECT nomPays,capitale from Pays ")

tableau2 = '''<div class='video'><table class='tab' id="style2" border='1'>'''
tableau2 += "<tr><th colspan='3'>Video :</th></tr></div></div>"


conn.close()

#affichage

pagedebut= '''
<html>
    <head>
        <title>EarthClouds</title>
        <link rel="stylesheet" href="css/main.css"/>
        <link rel = "icon" href = "images/geography.png"  type = "image/x-icon"/>
        <link rel="preconnect" href="https://fonts.gstatic.com"/>
        <link href="https://fonts.googleapis.com/css2?family=Londrina+Solid:wght@300&display=swap" rel="stylesheet"/>
        <link rel="preconnect" href="https://fonts.gstatic.com"/>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap" rel="stylesheet"/> 
    </head>
<body>
    <div class="banner">
        <div class='titre'>
        <img class="logo "src="images/geography.png" alt="logo">
        <h1>EarthClouds</h1>
        </div>
        <nav>
            <ul class="navRight">
                <li onclick="window.location='index.py'">Présentation</li>
                <li onclick="window.location='pays.py'">Pays</li>
                <li onclick="window.location='jeu.py'">Jouer</li>
            </ul>
        </nav>
    </div>
    <div class="back">
        <div class="imgBack"></div>
        <p class='imgP'>La source de découvertes de différents pays</p>
    </div>
    <img class="inspi" src="images/try.png" alt="inspi">
    <p class="inspiP">Inspiré par le bot Discord 'EarthClouds', créé par cette personne   - -- --></p>
    <img class="profile" src='images/prof1.jpg' alt="marchpo">
    <p class='trol'> (cfo c moi enfète)</p>
    <div class="enfin"><p> C'est bon ? Vous <span class="trait">souhaitez devenir le Einstein d</span>e la géographie ?  v</p></div>
    <button class="btn" onclick="window.location='pays.py'">Commencer</button>

    

'''

print(pagedebut + "</body></html>")

