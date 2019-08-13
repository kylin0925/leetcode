import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)
        self.flag = True


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.condition.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            self.condition.wait_for(lambda: self.flag)
            printFoo()
            self.flag = False
            self.condition.notify()

            self.condition.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.condition.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            self.condition.wait_for( lambda : not self.flag)
            printBar()
            self.flag = True
            self.condition.notify()
            self.condition.release()

def printFoo():
    print("foo")

def printBar():
    print("bar")

fun = FooBar(3)

A = threading.Thread(target=fun.foo, args=(printFoo,))
B = threading.Thread(target=fun.bar, args=(printBar,))
A.start()
B.start()