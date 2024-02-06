from math import *
"""Bon on peut soit fonctionner en tableau on en coordonnées (Xa Xb Xc Ya Yb...) il faut faire plein de tests pour éviter un manque de cas de figure
pour ce qu'on pourra faire: 
- faire courir quelqu'un avec le telephone sur le torse pour faire une analyse frame par frame et trouver tous les cas
- faire des test de calculs sur les cas extrêmes pour voir si la méthode de détermination de la position horizontale est satisfaisante
- éssayer de faire fonctionner le programme avec un max de fps pour assurer une stabilité des moteurs
- mettre en place une moyenne (ez)
- utilisation de la ligne d'arrivée ?
- faire gaffe si le circuit tourne (en gros un virage derrière la ligne d'arrivée) lors des calculs (normalement c'est pas un problème)"""


milieu=540
#lignes_recues={"droite":[xa,ya,xb,yb],
#               "gauche":[xa,ya,xb,yb]} #forme prise pour le code (voir les valeurs de sortie de Gab pour de potentiels changements) {}

while True:
    while lignes_recues!=oldlignes:
        oldlignes=lignes_recues #système pour faire fonctionner le coed une fois par coords [xa ya xb yb]
        def calcul(lignes,milieu):
            """Fonction principale dans laquelle on traite les coordonnées reçues et on revoie des valeurs pour mettre en route les moteurs 
            Entrée: un tableau de coordonnées entiers
            Sortie: un tableau de float"""
            if len(lignes)==1: #cas ou il n'y a qu'une seule ligne qui apparait (on part du principe que le y faible est le y du bas)
                if lignes[0][1]>lignes[0][3]:
                    if lignes[0][2]>lignes[0][0]:
                        return [0,100] #poucentage moteur ([gauche,droite])
                    else:
                        return [100,0]
                else:
                    if lignes[0][0]>lignes[0][2]:
                        return [0,100]
                    else:
                        return [100,0]
            elif len(lignes)==0: #cas où le coureur naruto run comme un tardos et on voit rien bah il n'est pas proche d'un côté (ou bug de recherche)
                return [0,0] 
            else: #on voit les deux lignes comme prévu
                if len(lignes)==2:
                    if lignes["droite"][1]>=lignes["droite"][3]:#on récupère la coords x du point du bas de la ligne de droite
                        minD=lignes["droite"][2]
                    else:
                        minD=lignes["droite"][0] 
                    if lignes["gauche"][1]>=lignes["gauche"][3]:#puis celui de gauche
                        minG=lignes["gauche"][2]
                    else:
                        minG=lignes["gauche"][0]  
                    GD=(minD+minG)/2#milieu des deux points
                    if GD-milieu>=0:
                        return [0,round((GD-milieu)/minD-GD,2)]#revoi des valeurs en pourcentage (round à check pour la précision)
                    return [round((GD-milieu)/minG-GD,2),0]
                    #if lignes["droite"] and lignes[1][0][1]==0: #on prends Ya et Yc valeurs du abs(help ya trop de variations) #cas ou les deux lignes touchent la partie du bas
                        #pass #bon flemme de coder ds le vent je vais écrire le reste en pseudo code
                        #on prends la moyenne des deux coords du bas puis on la compare à l'écran=> si on est ds les 25% externe on envoie un signal 50-100 100 atteint à 12,5% (13% si besoin)externe (valeurs modifiables)
                    #elif si ya une ligne qui touche alors ya trois moyens de procéder:
                        #-soit on fait le milieu des deux coords les plus bas
                        #-soit on fait la moyenne entre la coord la plus faible de la ligne incomplète et la coord de la ligne complete à la meme hauteur
                        #-soit on traite les deux cas du dessus avec une moyenne ou angle on verra
                    #elif si aucune ligne ne touche :
                        #probablement calculer le milieu des deux coords du bas et faire une ligne à partir du milieu de l'écran du haut et envoyer un signal de la même manière
                    




















#si besoin
"""if len(lignes_recues)>2:
    if sqrt((lignes_recues[0][0]-lignes_recues[0][2])**2+(lignes_recues[0][1]+lignes_recues[0][3])**2)>=sqrt((lignes_recues[1][0]-lignes_recues[1][2])**2+(lignes_recues[1][1]+lignes_recues[1][3])**2):
        imax=lignes_recues[0]
        imax2=lignes_recues[1]
    else:
        imax=lignes_recues[1]
        imax2=lignes_recues[0]
    for i in lignes_recues[:2]:
        longueur_ligne_i=sqrt((i[0]-i[2])**2+(i[1]+i[3])**2)
        if longueur_ligne_i>imax:
            imax2=imax
            imax=longueur_ligne_i
        elif longueur_ligne_i>imax2:
            imax2=longueur_ligne_i
    lignes=[imax,imax2]

"""
