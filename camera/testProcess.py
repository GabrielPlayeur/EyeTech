import multiprocessing as mp
import time
import random

class Temps:
    def __init__(self) -> None:
        self.createTime = time.time()

    def isOver(self):
        return self.time()-self.createTime > 1

    def time(self):
        return time.time()

class MultiProcess:
    i = mp.Value('i',0)

    def __init__(self, temps: Temps) -> None:
        self.temps = temps

    def run(self):
        print(f"Process {mp.current_process().name}: i = {MultiProcess.i.value}")
        with MultiProcess.i.get_lock():
            MultiProcess.i.value += 1
        time.sleep(random.random())

    def start(self) -> None:
        with mp.Pool(processes=4) as pool:
            while not self.temps.isOver():
                pool.apply_async(self.run)

if __name__ == "__main__":
    m = MultiProcess(Temps())
    m.start()
