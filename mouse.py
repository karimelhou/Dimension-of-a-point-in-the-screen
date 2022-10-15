import pyautogui as pg
from time import sleep

while True:
 pos = pg.position()

 # for x pos
 print("x =" ,pos[0])

 # for y pos
 print("y =",pos[1])
 print("done")
 sleep(2)


