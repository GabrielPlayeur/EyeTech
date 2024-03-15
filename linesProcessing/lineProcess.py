from time import time
from functools import reduce

class LinesProcess:
    def __init__(self, milieu: int) -> None:
        self.milieu = milieu
        self.queue = []
        self.delay = 0.5

    def calcul(self, lignes: dict[tuple[int, int, int, int]]) -> list:
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
        newTime = time()
        self.queue.append((newTime, value))
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