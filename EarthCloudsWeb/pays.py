import sqlite3


conn = sqlite3.connect('basedePays.db')
curseur = conn.execute("SELECT nomPays,capitale from Pays ")

tableau2 = '''<div class='video'><table class='tab' id="style2" border='1'>'''
tableau2 += "<tr><th colspan='3'>Video :</th></tr></div></div>"


conn.close()


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
    <div>
    <p class="entrez">Entrez le nom d'un pays</p>
    <form action="recherchePays.py" method="get" class="nomPays">
        <input type="text" name="nomPays" placeholder="Pays"/> 
        <input class="btn" style="margin-top:0px; font-size: 20px;" id="recherche" type="submit" value="Rechercher">
    </form>
    </div>
'''

print(pagedebut + "</body></html>")
