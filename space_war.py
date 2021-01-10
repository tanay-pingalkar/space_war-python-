# space war
#set screen
import turtle
import os
import math
import tkinter
k='notbreak'
u=0
a=10
def isCollision(t1,t2):
  distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
  if distance < 15:
    return True
  else:
    return False 
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('space invader')
#draw border
bb=turtle.Turtle()
bb.speed(0)
bb.color('white')
bb.penup()
bb.setposition(-180,-180)
bb.pendown()
for i in range(4):
  bb.fd(350)
  bb.left(90)
bb.hideturtle()
#player 1 by turtle
player=turtle.Turtle()
player.penup()
player.speed(0)
player.setposition(0,-150)

player.pencolor('blue')
player.setheading(90)
ps=15
#have enemy
e=turtle.Turtle()
e.penup()
e.setposition(-150,150)
e.shape('circle')
e.color('red')
es=4
e.speed(0)
#have weapon to enemy
ev=turtle.Turtle()
ev.color('green')
ev.shapesize(0.5,0.2)
ev.shape('square')
ev.speed(0)
evs=5
ev.hideturtle()
ev.penup() 
#work with enemy weapon
def enemy_curse():
  
 x = e.xcor()
 y = e.ycor()+10
 ev.showturtle()
 ev.setposition(x,y)
 return(True)
    

  
 
#have bullet
bullet=turtle.Turtle()
bullet.color('yellow')
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
bullets=5
#let work with bullet
bulletstate='ready'
def bullet_fire():
  global bulletstate
  if bulletstate=='ready':
   x=player.xcor()
   y=player.ycor()+10
   bullet.setposition(x,y)
   bullet.showturtle()
   bulletstate='fire'

#lets moe player
def move_left():
  v=player.xcor()
  v-=ps
  if v<-170:
    v=-169
  player.setx(v)
def move_right():
  v=player.xcor()
  v+=ps
  if v>170:
    v=160
  player.setx(v)
turtle.listen()
turtle.onkey(move_left,'Left')
turtle.onkey(move_right,'Right')
turtle.onkey(bullet_fire,'space')
i=0
#this is our main loop
while i == i:
  x=e.xcor()
  x+=es
  e.setx(x)
  if e.xcor()>165: 
    y=e.ycor()
    y-=10
    es*=-1
    e.sety(y)

  if e.xcor()<-165:
    y=e.ycor()
    y-=4
    es*=-1
    e.sety(y)
  #firekey
  y=bullet.ycor()
  y+=bullets
  bullet.sety(y)
  if bullet.ycor()>165:
    bullet.hideturtle()
    bulletstate='ready'
  if u/a==1 :
    if enemy_curse()== True:
      while ev.ycor()>-165:
        #enemy attack
        y=ev.ycor()
        y-=evs
        ev.sety(y)
        #bullet attack

        y=bullet.ycor()
        y+=bullets
        bullet.sety(y)
        if bullet.ycor()>165:
         bullet.hideturtle()
         bulletstate='ready'
        #move enemy still firing
        x=e.xcor()
        x+=es
        e.setx(x)
        if e.xcor()>165: 
         y=e.ycor()
         y-=10
         es*=-1
         e.sety(y)

        if e.xcor()<-165:
         y=e.ycor()
         y-=30
         es*=-1
         e.sety(y)
        if isCollision(ev,player)==True:
          ev.hideturtle()
          player.hideturtle()
          k='break'
          break
          
        if isCollision(e,bullet)==True :
         #bullet after collision
         bulletstate=='ready'
         bullet.hideturtle()
         e.hideturtle()
         k='break'
         break
        if isCollision(e,player)==True :
         k='break'
         break
         ev.hideturtle()
    a+=5
    
      
      
  if isCollision(e,bullet)==True :
    #bullet after collision
    bulletstate=='ready'
    bullet.hideturtle()
    e.hideturtle()
    break
  if isCollision(e,player)==True :
    break
  if k=='break':
    break

  u+=1
