__author__ = 'Jason'


class hello:
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print("hello {0}".format(self.name))

    def sayhi(self):
        print("hi {0}".format(self.name))


class dear(hello):
    def __init__(self, name):
        hello.__init__(self, name)

    def saydear(self):
        print("dear {0}".format(self.name))

h = hello("jason")
h.sayhello()
h.sayhi()
d= dear("peterson")
d.sayhello()
d.sayhi()
d.saydear()