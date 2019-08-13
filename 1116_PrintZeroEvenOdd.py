import threading
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.condition = threading.Condition()
        self.turn = 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        i = 1
        while i <= self.n:
            with self.condition:
                self.condition.wait_for(lambda :self.turn == 0)
                printNumber(0)
                self.turn = 1 if i % 2 == 1 else 2
                self.condition.notify_all()
                i+=1

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        i = 2
        while i <= self.n:
            with self.condition:
                self.condition.wait_for(lambda : self.turn == 2)
                printNumber(i)
                i +=2
                self.turn = 0
                self.condition.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        i = 1
        while i <= self.n:
            with self.condition:
                self.condition.wait_for(lambda : self.turn == 1)
                printNumber(i)
                i += 2
                self.turn = 0
                self.condition.notify_all()

sol = ZeroEvenOdd(5)

def printZero(n):
    print(0)

def printEven(n):
    print(n)

def printOdd(n):
    print(n)
ta =  threading.Thread(target=sol.zero, args=(printZero,))
tb =  threading.Thread(target=sol.even, args=(printEven,))
tc =  threading.Thread(target=sol.odd, args=(printOdd,))

ta.start()
tb.start()
tc.start()