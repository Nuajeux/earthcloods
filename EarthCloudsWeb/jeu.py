import sqlite3
import random


prop = [['nomPays', 'capitale'], ['capitale', 'nomPays'], ['drapo', 'nomPays'], ['drapo', 'capitale'], ['chef', 'nomPays']]

conn = sqlite3.connect('baseDePays.db')
conn.row_factory = lambda cursor, row: row[0]
cursor = conn.cursor()

def randint():
    return random.randint(1, 10)

for element in range(len(prop)):
    nb = randint()
    cursor.execute("SELECT " + prop[element][0] + " FROM Pays WHERE idPays = " + str(nb))
    for e in cursor:
        temp = [e]
    cursor.execute("SELECT " + prop[element][1] + " FROM Pays WHERE idPays = " + str(nb))
    for e in cursor:
        temp1 = [e]
    prop[element] = [temp, temp1]
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
   
    <!remplacer>
</body>
</html>
'''

pagemil= '''
    <div style="margin-top: 75px;" class="back">
        <img class="fondd" src="css/images/gamefond.jpg" alt='capachpa'>
        <div class="info" style=" margin-top: 12px; width: 340px; padding-bottom: 4px;">
        <form action="game.js" method="get">
            <div class="tete">
            <p class='imgPP' style="margin-bottom: 0px; margin-left:26px; margin-top: 0px;">A vous de jouer !</p>
            </div>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <div style="display: flex;"><img style="margin-top: 10px; height: 22px;"src="css/images/world.png"><p style="font-weight: bold; margin-top: 10px; margin-bottom: 0px;">Devinez le pays !</p></div>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold; float: left; margin-right: 10px;">Quel pays a pour drapeau</span></p><img style='width: 25px;' src="drapp" alt='marchpo'/>
            </form>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <input id="qu1" type="text" list="hidden" name="nomPays" placeholder="Pays"/>
            <div style = "transform: translateY(-120%);" class="pass-icon">
                    <img id="yes1" style="visibility: hidden;"  src="css/images/check.svg " alt="pouf">
                    <img id="nop1" style="visibility: hidden;" src="css/images/x.svg" alt="pouf">
            </div>
            <input id="solu1" type="hidden" value="Pdsolu" name="sPaysDrap"/>
            </form>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Quel pays a pour capitale <span style="background-color: #2F3136; border-radius: 6px; padding: 2px;">capp</span> ?</span></p>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <input id="qu2" type="text" list="hidden" name="nomPays" placeholder="Pays"/>
            <div style=" transform: translateY(-120%);" class="pass-icon">
                    <img id="yes2" style="visibility: hidden;" src="css/images/check.svg " alt="pouf">
                    <img id="nop2" style="visibility: hidden;" src="css/images/x.svg" alt="pouf">
            </div>
            <input id="solu2" type="hidden" value="Pcsolu" name="sPaysCap"/>
            </form>
            <p style="margin-top: 4px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Quel pays a pour gouverneur/s <span style="background-color: #2F3136; border-radius: 6px; padding: 2px;">gouvv</span> ?</span></p>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <input id="qu3" type="text" list="hidden" name="nomPays" placeholder="Pays"/>
            <div style = "transform: translateY(-120%);" class="pass-icon">
                    <img id="yes3" style="visibility: hidden; " src="css/images/check.svg " alt="pouf">
                    <img id="nop3" style="visibility: hidden; " src="css/images/x.svg" alt="pouf">
            </div>
            <input id="solu3" type="hidden" value="Pchefsolu" name="sPaysChef"/>
            </form>
            <div style="display: flex;"><img style="margin-top: 0px; height: 22px;"src="css/images/golded.png"><p style="font-weight: bold; margin-top: 0px; margin-bottom: 0px;">Devinez la capitale !</p></div>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold;">Quelle capitale correspond au pays <span style="background-color: #2F3136; border-radius: 6px; padding: 2px;">payss</span> ?</span></p>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <input id="qu4" type="text" list="hidden" name="nomPays" placeholder="Capitale"/>
            <div style = "transform: translateY(-120%);" class="pass-icon">
                    <img id="yes4" style="visibility: hidden;" src="css/images/check.svg " alt="pouf">
                    <img id="nop4" style="visibility: hidden;" src="css/images/x.svg" alt="pouf">
            </div>
            <input id="solu4" type="hidden" value="Cpsolu" name="sCapitalePays"/>
            </form>
            <p style="margin-top: 0px; margin-bottom: 0px; font-size: 14px;"><span style="color: #DCDDDE; font-weight: bold; float: left; margin-right: 10px;">Quelle capitale correspond au drapeau</span></p><img style='width: 25px;' src="drawzp2" alt='marchpo'/>
            <form class="nomPays" style="margin-top: 10px;margin-bottom: 10px;padding-bottom: 0px; border:0;">
            <input id="qu5" type="text" list="hidden" name="nomPays" placeholder="Capitale"/>
            <div style = "transform: translateY(-120%);" class="pass-icon">
                    <img id="yes5" style="visibility: hidden;" src="css/images/check.svg " alt="pouf">
                    <img id="nop5" style="visibility: hidden;" src="css/images/x.svg" alt="pouf">
            </div>
            <input id="solu5" type="hidden" value="Cdsolu" name="sCapitaleDrap"/>
            </form>
            <p class="resu" style="hidden; margin-bottom:0"></p>
            <button class="btn" style="margin-top:0; margin-bottom:0; margin-left:114px;">Valider</button>
            <p class="com" style="hidden; margin-bottom:0"></p>
        </form>
        </div>
    </div>

    <script type="text/javascript" src="https://unpkg.com/feather-icons"></script>
    <script src="js/game.js"></script> 
'''

pagemil = pagemil.replace("drapp",str(prop[2][0][0]))
pagemil = pagemil.replace("capp",str(prop[1][0][0]))
pagemil = pagemil.replace("gouvv",str(prop[4][0][0]))
pagemil = pagemil.replace("payss",str(prop[0][0][0]))
pagemil = pagemil.replace("drawzp2",str(prop[3][0][0]))
pagemil = pagemil.replace("Cdsolu",str(prop[3][1][0]))
pagemil = pagemil.replace("Cpsolu",str(prop[0][1][0]))
pagemil = pagemil.replace("Pdsolu",str(prop[2][1][0]))
pagemil = pagemil.replace("Pcsolu",str(prop[1][1][0]))
pagemil = pagemil.replace("Pchefsolu",str(prop[4][1][0]))
pagedebut = pagedebut.replace("<!remplacer>",pagemil)

print(pagedebut)