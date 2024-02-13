from math import *
from time import *
"""Bon on peut soit fonctionner en tableau on en coordonnées (Xa Xb Xc Ya Yb...) il faut faire plein de tests pour éviter un manque de cas de figure
pour ce qu'on pourra faire: 
- faire courir quelqu'un avec le telephone sur le torse pour faire une analyse frame par frame et trouver tous les cas
- faire des test de calculs sur les cas extrêmes pour voir si la méthode de détermination de la position horizontale est satisfaisante
- éssayer de faire fonctionner le programme avec un max de fps pour assurer une stabilité des moteurs
- mettre en place une moyenne (ez)
- utilisation de la ligne d'arrivée ?
- faire gaffe si le circuit tourne (en gros un virage derrière la ligne d'arrivée) lors des calculs (normalement c'est pas un problème)"""
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
                print("valeur 2: ", minD)
            else:
                minD=lignes["droite"][0] 
                print("valeur 0: ", minD)
            if lignes["gauche"][1]>=lignes["gauche"][3]:#puis celui de gauche
                minG=lignes["gauche"][2]
                print("valeur 2: ", minG)
            else:
                minG=lignes["gauche"][0]  
                print("valeur 0: ", minD)
            GD=(minD+minG)/2#milieu des deux points
            print('gd', GD)
            print(GD-milieu)
            if GD-milieu>=0:
                return [0,abs(round((GD-milieu)/(GD-minD+0.001),2))]#revoi des valeurs en pourcentage (round à check pour la précision)
            return [abs(round((GD-milieu)/(GD-minG+0.001),2)),0]
def moyenne(tab,new_value):
    tab.append((time(),new_value))#on ajoute la valeur actuel
    tab2=tab+[]
    for i in tab2:#on dégage les valeurs qui datent de plus de 0.5s
        if time()-i[0]>=0.5:
            tab.pop(0)
    moyenne=[0,0]
    for i in tab: #on calcule la moyenne
        moyenne[0]+=tab[i][0]
        moyenne[1]+=tab[i][1]
    moyenne[0]/=len(tab)
    moyenne[1]/=len(tab)
    return moyenne
        

def output(tab):
    value=0
    for i in range(len(tab)):
        if tab[i]<0.33:
            value+=0
        elif tab[i]<0.66:
            value+=(-1)**(i+1)
        else :
            value+=2*(-1)**(i+1)
    return value

milieu=400 
qqch={"droite":[400,100,500,750],
      "gauche":[400,0,0,200]
      }
print(calcul(qqch,400))
