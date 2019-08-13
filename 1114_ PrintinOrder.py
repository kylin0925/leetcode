import threading
class Foo:
    lock1 = None
    lock2 = None

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock1.acquire()
        printSecond()
        self.lock1.release()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.lock2.acquire()
        printThird()
        self.lock2.release()

def printStr():
    print("1111")

def printStr2():
    print("2222")
def printStr3():
    print("3333")
foo = Foo()
funarr = [foo.first,foo.first,
            foo.second,
            foo.third]
funarr2 = [printStr,printStr,
          printStr2,
          printStr3]
test_data = [3,2,1]
for f in test_data:
    #print(f)
    t = threading.Thread(target = funarr[f], args =(funarr2[f],))
    t.start()

