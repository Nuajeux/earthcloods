import sqlite3

# Ouverture de la base de donnée
conn = sqlite3.connect('baseDePays.db')

# c "représente" les lignes de commandes
c = conn.cursor()

# Si la table existe on l'efface
c.execute('DROP TABLE IF EXISTS Pays')

# Création de la table
c.execute('''CREATE TABLE Pays (
     idPays int primary key,
     nomPays text,
     capitale text,
     image text,
     drapo text,
     continent text,
     pop text,
     surface text,
     gouv text,
     chef text,
     devise text)''')

# Insertion 1 à 1
c.execute('''INSERT INTO Pays
              values(1, 'France', 'Paris','https://images.hdqwalls.com/download/paris-france-eiffel-tower-night-m2-1920x1080.jpg','https://cdn.discordapp.com/attachments/819980725616246785/820073093510332456/fr-flag.png','Europe','66.999.000 habitants','643.801km²','République','Président: Emmanuel Macron','Euro (EUR)')''')

# Insertion groupée
liste = [(2, 'Espagne', 'Madrid',"https://images2.alphacoders.com/692/692059.jpg","https://cdn.discordapp.com/attachments/819980725616246785/820281227549343764/xqBQCAQCAQCgUAgEAgEAoFAIBAIBAKBQCAQCAQC8avxbxfPxApYDdp3AAAAAElFTkSuQmCC.png","Europe","49.940.000 habitants","505.990km²","Monarchie","Roi: Felipe V","Euro (EUR)"),
         (3, 'Italie', 'Rome',"https://s1.1zoom.me/b5050/857/Coast_Italy_Houses_Sea_482252_1920x1080.jpg","https://cdn.discordapp.com/attachments/819980725616246785/820286431221121074/0IZwJzQg6Zme7SkGDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0N.png","Europe","60.360.000 habitants","301.338km²","République","Président: Sergio Mattarella","Euro (EUR)"),
         (4, 'Allemagne', 'Berlin',"https://w.wallhaven.cc/full/vg/wallhaven-vgv2zm.jpg","https://cdn.discordapp.com/attachments/819980725616246785/820281781168898068/udoZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9D2gCdqjUNiUlAAAAAElFTkSuQmCC.png","Europe","83.000.000 habitants","357.386km²","République","Chancelière: Angela Merkel","Euro (EUR)"),
         (5, 'Royaume-Uni', 'Londres',"https://allegra.flowersetcfresno.com/pic/3616770_full-fondos-de-pantalla-1920x1080-londres-best-37-england-wallpaper-on-hipwallpaper-six-flags-new-england.jpg","https://cdn.discordapp.com/attachments/819980725616246785/820283211762106378/sNKCkISA2F1h23YICQSP7D1SQfrz3aslKAAAAAElFTkSuQmCC.png","Europe","66.660.000 habitants","242.495km²","Monarchie","Reine: Elisabeth II","Livre sterling(GBP)"),
         (6, 'Suisse','Berne','http://s1.1zoom.me/b5050/159/Switzerland_Mountains_Houses_Winter_Evening_Davos_540309_1920x1080.jpg','https://cdn.discordapp.com/attachments/819980725616246785/820284130909749298/9yAwAAAAAAAAAAfNsbgg8rFsORGy8AAAAASUVORK5CYII.png',"Europe","8.570.000 habitants","41.285km²","Etat Fédéral","Président du conseil: Guy Parmelin","Franc suisse(CHF)"),
         (7, 'Autriche','Vienne','https://get.wallhere.com/photo/village-road-trees-snow-hairpin-turns-lights-night-long-exposure-mountain-pass-Austria-1919045.jpg','https://cdn.discordapp.com/attachments/819980725616246785/820325163580784700/9O8W3fAAAAZElEQVR4nO3PAQEAMAjAIO1fjnmoQEzAAAAAAAAAAAAAMApe51hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9hn2GfYZ9.png','Europe','8.859.000 habitants','83.879km²','République','Chancelier: Sebastian Kurz','Euro (EUR)'),
         (8, 'Pays-Bas','Amsterdam','https://tse1.mm.bing.net/th?id=OIP.VIahM5lobXPmxHCIdgHsVQHaEK&pid=Api','https://cdn.discordapp.com/attachments/819980725616246785/820284879706521600/0ObYhQbMAAAAAAAAAAAAAACrnO0Mwz7DPsMwz7DPsMwz7DPsMwz7DPsMwz7DPsMwz7DPsMwz7DPsMwz7DPsGN7tDPsMwz7DPsMwz.png','Europe','17.740.000 habitants','41.543km²','Monarchie',"Roi: Guillaume-Alexandre","Euro (EUR)"),
         (9, 'Tchequie','Prague','https://images7.alphacoders.com/102/thumb-1920-1027699.jpg','https://cdn.discordapp.com/attachments/819980725616246785/820325400588320777/7BYjUeXyuoRQdAAAAAElFTkSuQmCC.png',"Europe","10.710.000 habitants","78.866km²",'République',"Président: Milos Zeman","Couronne tchèque(CZK)"),
         (10, 'Vatican','Vatican','https://cdn.wallpapersafari.com/92/36/e6IXYz.jpg','https://cdn.discordapp.com/attachments/819980725616246785/820339883721359370/0oiTISJMBEmwkSYCBNhIkyEiTARJsJEmAgTYSJMhIkwESbCRJgIE2EiTISJMBEmwkSYCBNhIkyEiTARJsJEmAgTYSJMhIkwESbCR.png','Europe','825 habitants','44ha','Monarchie',"Pape: François","Euro (EUR)"),]
c.executemany("INSERT INTO Pays values(?,?,?,?,?,?,?,?,?,?,?)", liste)

# On applique les changements
conn.commit()

# On ferme la base
conn.close()
       
