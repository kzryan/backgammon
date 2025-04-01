import pygame 

#Variables
white=255,255,255
width = 800
height = 600
size = (width,height)
myScreen=pygame.display.set_mode(size)
spacing1 = width/14
spacing2 = height/6
radius = height/24
#these are the rectagles that make up spaces on the board
spaces=[]
triLines=[]
blackPieces=[]
whitePieces=[]
drag_pieces=[]

color=(0,0,0)
gray=(156, 153, 146)
running= True
is_dragging = False
drag_color = color
totalRoll = 8
initialPos = []