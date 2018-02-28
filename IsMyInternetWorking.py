from asciimatics.renderers import FigletText
from asciimatics.screen import Screen
from requests import get as getwebsite
from requests import exceptions
from time import sleep
from random import randint
import math

working = True
testing = True
try:
    st = getwebsite("https://www.google.com/humans.txt")
except exceptions.ConnectionError:
    working = False
testing = False

txt = "YES!" if working else "NO : ("
c   = 2 if working else 1
h   = 6 + int(not working)
stxt= "It's working!!" if working else "nope :("

ftxt = FigletText(txt, font='big')


def demo(screen):
    global testing
    global working
    global txt
    global c
    global h
    global stxt
    global ftxt
    global curr
    off = int(screen.height/2)
    while True:
##        for y in range(screen.height):
##            for x in range(screen.width):
##                if y < 5 and y >= 0:
##                    screen.print_at(" ",x,y,bg=7)
##                elif y < 10 and y >= 5:
##                    screen.print_at("\N{Dark Shade}",x,y)
##                elif y < 15 and y >= 10:
##                    screen.print_at("\N{Medium Shade}",x,y)
##                elif y < 20 and y >= 15:
##                    screen.print_at("\N{Light Shade}",x,y)
        ev = screen.get_key()
        if ev in (ord('r'),ord('R')):
            testing = True
            y = 0
            f = FigletText("MAYBE", font='big')
            for i in str(f).split('\n'):
                if y == h: break
                screen.print_at(i,int(screen.width/2)-int(f.max_width/2),y+off-int(f.max_height/2),colour=3,attr=1)                
                y += 1
            screen.print_at("just checking...",int(screen.width/2)-int(len("just checking...")/2),y+1+off-int(f.max_height/2))
            screen.refresh()
            try:
                st = getwebsite("https://www.google.com/humans.txt")
                working = True
            except exceptions.ConnectionError:
                working = False
            txt = "YES!" if working else "NO : ("
            c   = 2 if working else 1
            h   = 6 + int(not working)
            stxt= "It is working!!" if working else "nope :("

            ftxt = FigletText(txt, font='big')

        elif ev in (ord('e'),ord('E')):
            return
              
        if not testing:
            y = 0
            for i in str(ftxt).split('\n'):
                if y == h: break
                screen.print_at(i,int(screen.width/2)-int(ftxt.max_width/2),y+off-int(ftxt.max_height/2),colour=c,attr=1)                
                y += 1
            screen.print_at(stxt,int(screen.width/2)-int(len(stxt)/2),y+1+off-int(ftxt.max_height/2))
        else:
            testing = False
            screen.clear()
        screen.refresh()
        
        
Screen.wrapper(demo)
