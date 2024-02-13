from time import time
from functools import reduce

class LinesProcess:
    def __init__(self, milieu: int) -> None:
        self.milieu = milieu
        self.queue = []
        self.delay = 0.5

    def calcul(self, lignes: tuple[tuple[int, int]]) -> list:
        """Fonction principale dans laquelle on traite les coordonnées reçues et on revoie des valeurs pour mettre en route les moteurs"""
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
                    return [0,abs(round((GD-milieu)/(GD-minD+0.001),2))]#revoi des valeurs en pourcentage (round à check pour la précision)
                return [abs(round((GD-milieu)/(GD-minG+0.001),2)),0]

    def updateQueue(self, value: list) -> None:
        newTime = time()
        self.queue.append((newTime, value)) #on ajoute la valeur actuel
        while len(self.queue) > 0 or newTime - self.queue[0][0] >= self.delay:
            self.queue.pop(0)

    def moyenne(self, newValue: list) -> list:
        self.updateQueue(newValue)
        return [reduce(lambda x,y: x[1][0]+y[1][0], self.queue)/len(self.queue), 
                reduce(lambda x,y: x[1][1]+y[1][1], self.queue)/len(self.queue)]

    def linePosition(self, moy: list) -> int:
        value=0
        for i in range(len(moy)):
            if moy[i]<0.33:
                value+=0
            elif moy[i]<0.66:
                value+=(-1)**(i+1)
            else :
                value+=2*(-1)**(i+1)
        return value

    def output(self, lignes: list) -> int:
        return self.linePosition(self.moyenne(self.calcul(lignes)))

if __name__ == "__main__":
    milieu=400 
    qqch={"droite":[400,100,500,750],
        "gauche":[400,0,0,200]
        }
    print(calcul(qqch,400))