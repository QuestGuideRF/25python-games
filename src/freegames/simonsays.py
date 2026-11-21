from random import choice
from time import sleep
from turtle import *
from freegames import floor ,square ,vector
pattern =[]
guesses =[]
tiles ={
vector (0 ,0 ):('red','темно-красный'),
vector (0 ,-200 ):('blue','темно-синий'),
vector (-200 ,0 ):('green','темно-зеленый'),
vector (-200 ,-200 ):('yellow','khaki'),
}
def grid ():
    square (0 ,0 ,200 ,'темно-красный')
    square (0 ,-200 ,200 ,'темно-синий')
    square (-200 ,0 ,200 ,'темно-зеленый')
    square (-200 ,-200 ,200 ,'khaki')
    update ()
def flash (tile ):
    glow ,dark =tiles [tile ]
    square (tile .x ,tile .y ,200 ,glow )
    update ()
    sleep (0.5 )
    square (tile .x ,tile .y ,200 ,dark )
    update ()
    sleep (0.5 )
def grow ():
    tile =choice (list (tiles ))
    pattern .append (tile )
    for tile in pattern :
        flash (tile )
    print ('Длина паттерна:',len (pattern ))
    guesses .clear ()
def tap (x ,y ):
    onscreenclick (None )
    x =floor (x ,200 )
    y =floor (y ,200 )
    tile =vector (x ,y )
    index =len (guesses )
    if tile !=pattern [index ]:
        exit ()
    guesses .append (tile )
    flash (tile )
    if len (guesses )==len (pattern ):
        grow ()
    onscreenclick (tap )
def start (x ,y ):
    grow ()
    onscreenclick (tap )
setup (420 ,420 ,370 ,0 )
hideturtle ()
tracer (False )
grid ()
onscreenclick (start )
done ()