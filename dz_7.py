class TrafficLight:
    self.__color = "color"

import turtle
import time

def running(self):
  pen = turtle.Turtle()
  pen.color("black")
  pen.width(3)
  pen.hideturtle()

  pen.penup()
  pen.setposition(-30, 60)
  pen.pendown()
  pen.forward(60)
  pen.right(90)
  pen.forward(120)
  pen.right(90)
  pen.forward(60)
  pen.right(90)
  pen.forward(120)
  pen.right(90)

  red_light = turtle.Turtle()
  red_light.shape('circle')
  red_light.color('grey')
  red_light.penup()
  red_light.setposition(0, 40)

  yellow_light = turtle.Turtle()
  yellow_light.shape('circle')
  yellow_light.color('grey')
  yellow_light.penup()
  yellow_light.setposition(0, 0)

  green_light = turtle.Turtle()
  green_light.shape('circle')
  green_light.color('grey')
  green_light.penup()
  green_light.setposition(0, -40)

  while True:
    red_light.color('red')
    time.sleep(7)
    red_light.color('grey')
    yellow_light.color('yellow')
    time.sleep(2)
    yellow_light.color('grey')
    green_light.color('green')
    time.sleep(5)
    green_light.color('grey')


a = TrafficLight()
a.running()