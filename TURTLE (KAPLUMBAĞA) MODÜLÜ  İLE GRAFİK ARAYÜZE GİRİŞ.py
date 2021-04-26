
                 #TURTLE (KAPLUMBAĞA) MODÜLÜ İLE GRAFİK ARAYÜZE GİRİŞ#


"""

import turtle

yıldız = turtle.Turtle()

for i in range(5):
    yıldız.forward(100)
    yıldız.right(144)

turtle.done()

"""

"""
import  turtle
yıldız = turtle.Turtle()

for i in range(50):
    yıldız.forward(100)
    yıldız.right(123)

turtle.done()
"""

"""
import turtle
kalem=turtle.Turtle()
kalem.color("red")
for i in range (6):
  for j in range (6):

     kalem.forward(50)
kalem.left(60) # iç döngü
kalem.left(60)# dış döngü
turtle.done()

"""

"""
import turtle
kalem = turtle.Turtle()
kalem.color("blue")
for k in range(5,106,25):
    print(k)
    for i in range(4):
        kalem.forward(k)
        kalem.left(90)
turtle.done()

"""

"""

import turtle
kalem=turtle.Turtle()
kalem.pencolor("orange")
kalem.pensize(2)
kalem.circle(20)
kalem.pencolor("red")
kalem.circle(30)
kalem.pencolor("blue")
kalem.circle(40)
turtle.done()

"""

"""
import turtle
kalem=turtle.Turtle()
kalem.pencolor("red")
kalem.pensize(3)

kenar_sayısı=int(input(" çizmek istediğiniz çokgenin kenar sayısını giriniz"))
for i in range(kenar_sayısı):
    kalem.forward(50)
    kalem.left(360 / kenar_sayısı)
turtle.done()

"""


"""
import turtle
kalem=turtle.Turtle()
kalem.pencolor("red")
kalem.pensize(3)
kalem.forward(100)
kalem.left(90)
kalem.color("#ACE515")
kalem.pensize(8)
kalem.forward(100)
kalem.left(90)
kalem.pencolor("yellow")
kalem.pensize(6)
kalem.forward(100)
kalem.left(90)
kalem.color("#2259C1")
kalem.pensize(1)
kalem.forward(100)
kalem.left (90)
turtle.done()

"""

"""


import turtle
def desen_çiz (kenar_uzunluğu=50,iç_kenar=3,tur_sayısı=3):
    if(tur_sayısı <1 or iç_kenar<3):
        print("hatalı veri girdiniz")

    else:
        kalem = turtle.Turtle()
        for i in range(tur_sayısı):
            for j in range(iç_kenar):
                kalem.forward(kenar_uzunluğu)
                kalem.left(360 / iç_kenar)
            kalem.left(360 / tur_sayısı)
desen_çiz()
desen_çiz(60,4,5)
desen_çiz(70,6,10)
turtle.done()


"""