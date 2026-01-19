# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

""" # 1 local
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(a) # functons can't see in another function

func1()
func2()
"""

""" #2
# enclosed
def func1():
    x = 1
    print(x)

    def func2():
        x = 2
        print(x)
    func2()


func1()
"""

""" #3
# Global
def func1():
    print(x)

def func2():
    print(x)

x = 3   # this is the global version of x used by both func1 & func 2

func1()
func2()
"""

from math import e

def func1():
    print(e)

e = 3

func1()