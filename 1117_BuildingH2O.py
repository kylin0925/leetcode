import threading
class H2O:
    def __init__(self):
        #self.condition = threading.Condition()
        #self.h =threading.Semaphore(2)
        #self.o =threading.Semaphore(0)
        self.lock = threading.Lock()
        self.hq = []
        self.oq = []
        self.h = 0
        self.o = 0

    def output(self):
        if self.h>=2 and self.o >=1:
            o = self.oq.pop()
            o()
            h = self.hq.pop()
            h()
            h = self.hq.pop()
            h()
            self.h-=2
            self.o-=1

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        #with self.condition:
        #    self.condition.wait_for(lambda : self.h<2 )
        #    self.h += 1
        #    releaseHydrogen()
        #    self.condition.notify_all()
        #self.h.acquire()
        #releaseHydrogen()
        #self.o.release()
        self.lock.acquire()
        self.hq.append(releaseHydrogen)
        self.h+=1
        self.output()
        self.lock.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        #with self.condition:
        #    self.condition.wait_for(lambda :self.h == 2)
        #    releaseOxygen()
        #    self.h=0
        #    self.condition.notify_all()
        #self.o.acquire()
        #self.o.acquire()
        #releaseOxygen()
        #self.h.release()
        #self.h.release()
        self.lock.acquire()
        self.oq.append(releaseOxygen)
        self.o+=1
        self.output()
        self.lock.release()

def releaseHydrogen():
    import time
    print("H")
    #time.sleep(.1)

def releaseOxygen():
    import time
    #time.sleep(.1)
    print("O")


obj = H2O()
test = "HHHHHHHHHHOHHHHOHHOOOHHHHHOHOHHOOHHHOOOOHHOOHOHHHHHOOHHOHOOHHHHHOOOOOOOOHOHHHHHHHHHHHHHHHH"

for c in test:
    if c == 'H':
        t = threading.Thread(target=obj.hydrogen,args=(releaseHydrogen,))
        t.start()
    else:
        t = threading.Thread(target=obj.oxygen, args=(releaseOxygen,))
        t.start()
