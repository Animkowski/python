from turtle import *

def kw():
    fillcolor('yellow')
    begin_fill()
    for i in range(4):
        fd(80)
        rt(90)
    end_fill()
def wiez():
    fillcolor('turquoise')
    begin_fill()
    for i in range(4):
        fd(80)
        rt(90)
    end_fill()
    bok=60
    for i in range(3):
        pu()
        fd(10)
        rt(90)
        fd(10)
        lt(90)
        pd()
        for j in range(4):
            fd(bok)
            rt(90)
        bok-=20

def posa():
    for i in range(2):
        wiez()
        pu()
        lt(90)
        fd(30)
        rt(90)
        fd(50)
        pd()
        kw()
        fd(80)
    wiez()
    pu()
    lt(90)
    fd(30)
    rt(90)
    fd(50)
    pd()
def dzka():
    for i in range(2):
        kw()
        fd(80)
        wiez()
        pu()
        lt(90)
        fd(30)
        rt(90)
        fd(50)
        pd()        
    kw()
    fd(80)

def posadzka():    
    pu()
    bk(200)
    lt(90)
    fd(200)
    rt(90)
    pd()
    for i in range(2):
        posa()
        bk(400)
        pu()
        rt(90)
        fd(80)
        lt(90)
        pd()
        dzka()
        pu()
        bk(400)
        rt(90)
        fd(80)
        lt(90)
        pd()
    posa()


speed(0)
posadzka()
