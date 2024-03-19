from time import time
from functools import reduce

class LinesProcess:
    def __init__(self, milieu: int) -> None:
        self.milieu = milieu #404
        self.queue = []
        self.delay = 0.5

    def calcul(self, lignes: dict) -> list:
        """fonction permettant de calculer la position relative du coureur par rapport au centre du couloir
        entrée : dict de listes (coordonnées)
        sortie : liste de float (pourcentage de déviation par rapport au centre [ % gauche, % droite])"""
        try:
            lignes["right"][3]
            lignes["left"][3]
        except Exception as error:
            print(error)
            return [0,0]

        if lignes["right"][1] >= lignes["right"][3]:
            minXRight = lignes["right"][2]
        else:
            minXRight = lignes["right"][0]

        if lignes["left"][1]>=lignes["left"][3]:
            minXLeft = lignes["left"][2]
        else:
            minXLeft = lignes["left"][0]

        center = (minXRight+minXLeft)/2
        if center >= self.milieu:
            return [0,abs(round((center-self.milieu)/(center-minXRight+0.001),2))] #Right
        return [abs(round((center-self.milieu)/(center-minXLeft+0.001),2)),0] #Left

    def updateQueue(self, value: list) -> None:
        """fonction permettant d'ajouter la déviation actuelle associé au temps à une liste et de retirer les tuples obsolètes
        entrée: un tuple 
        sortie : une liste de tuple"""
        newTime = time()
        self.queue.append((newTime, value))
        while len(self.queue) > 0 and newTime - self.queue[0][0] >= self.delay:
            self.queue.pop(0)

    def moyenne(self, newValue: list,a=0,b=0) -> list:
        """fonction permettant de faire la moyenne des deuxiemes valeurs de tuples
        entrée: liste de tuple
        sorite: liste de float"""
        self.updateQueue(newValue)
        for i in self.queue:
            a+=i[1][0]
            b+=i[1][1]
        return [a/len(self.queue),b/len(self.queue)]

    def linePosition(self, moy: list) -> int:
        """fonction revoyant le signal à envoyer aux moteurs basée sur la moyenne
        entrée: liste de float
        sortie: un entier"""
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
        """fonction utilisant les fonctions ci-dessus
        entrée: dict de listes
        sortie: un entier"""
        return self.linePosition(self.moyenne(self.calcul(lignes)))