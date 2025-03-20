import config as c
import pygame




# Helper function to check if mouse click is inside circle
def is_circle_clicked(circle_x, circle_y, radius, mouse_x, mouse_y):

    distance = ((circle_x - mouse_x) ** 2 + (circle_y - mouse_y) ** 2) ** 0.5

    return distance <= radius

# Draws the game board triangles and lines
def drawTris():
    start= [0, 0]
    end= [c.spacing1/2, c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             
             c.triLines.append([start.copy(),end.copy()])
             if j+1<NOL:
                start = end.copy()
                if j%2 == 0:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2
                else:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2
        
        c.triLines.append([end.copy(),(end.copy()[0],c.height)])

        c.triLines.append([(end.copy()[0]+c.spacing1,end.copy()[1]),(end.copy()[0]+c.spacing1,c.height)])

        start = end.copy()
        start[0] += c.spacing1*2
        end = start.copy()
        end[0] += c.spacing1/2
        end[1] += c.spacing2

        c.triLines.append([start.copy(),(start.copy()[0],c.height)])
        
        for j in range(NOL):
             
             c.triLines.append([start.copy(),end.copy()])
             if j+1<NOL:
                start = end.copy()
                if j%2 == 0:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2
                else:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2

    start= [0, c.height]
    end= [c.spacing1/2, c.height - c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             c.triLines.append([start.copy(),end.copy()])
             if j+1<NOL:
                start = end.copy()
                if j%2 == 0:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2
                else:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2


        start = end.copy()
        start[0] += c.spacing1*2
        end = start.copy()
        end[0] += c.spacing1/2
        end[1] -= c.spacing2
        
        for j in range(NOL):
             
             c.triLines.append([start.copy(),end.copy()])
             if j+1<NOL:
                start = end.copy()
                if j%2 == 0:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2
                else:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2

#Adds all the starting black and white pieces
def createPieces():
    #drawing leftmost black pieces
    diameter = 2*c.radius
    center = [c.spacing1/2,1.3*c.radius]
    c.blackPieces.append((center,c.radius))
    newY = 1.3*c.radius + diameter
    newCenter = [c.spacing1/2,newY]
    for i in range (4):
            c.blackPieces.append([newCenter, c.radius])
            newY = 1.3*c.radius+diameter*(i+2)
            newCenter = [c.spacing1/2,newY]

    #drawing middle left black pieces
    center = [c.spacing1*4.5, c.height - 1.3*c.radius]
    c.blackPieces.append((center,c.radius))
    newY = c.height - 1.3*c.radius - diameter
    newCenter = [c.spacing1*4.5,newY]
    for i in range (2):
            c.blackPieces.append([newCenter, c.radius])
            newY = c.height - 1.3*c.radius - diameter*(i+2)
            newCenter = [c.spacing1*4.5,newY]

    #drawing middle right black pieces
    center = [c.spacing1*8.5, c.height - 1.3*c.radius]
    c.blackPieces.append((center,c.radius))
    newY = c.height - 1.3*c.radius - diameter
    newCenter = [c.spacing1*8.5,newY]
    for i in range (4):
            c.blackPieces.append([newCenter, c.radius])
            newY = c.height - 1.3*c.radius - diameter*(i+2)
            newCenter = [c.spacing1*8.5,newY]

    #drawing rightmost black pieces
    diameter = 2*c.radius
    center = [c.width-c.spacing1/2,1.3*c.radius]
    c.blackPieces.append((center,c.radius))
    newY = 1.3*c.radius + diameter
    newCenter = [c.width-c.spacing1/2,newY]
    c.blackPieces.append([newCenter, c.radius])
    newY = 1.3*c.radius+diameter*(3)
    newCenter = [c.width-c.spacing1/2,newY]



    #drawing leftmost white pieces
    diameter = 2*c.radius
    center = [c.spacing1/2,c.height - 1.3*c.radius]
    c.whitePieces.append((center,c.radius))
    newY = c.height - 1.3*c.radius - diameter
    newCenter = [c.spacing1/2,newY]
    for i in range (4):
            c.whitePieces.append([newCenter, c.radius])
            newY = c.height - 1.3*c.radius-diameter*(i+2)
            newCenter = [c.spacing1/2,newY]

            

    #drawing middle left white pieces
    center = [c.spacing1*4.5, 1.3*c.radius]
    c.whitePieces.append((center,c.radius))
    newY =  1.3*c.radius + diameter
    newCenter = [c.spacing1*4.5,newY]
    for i in range (2):
            c.whitePieces.append([newCenter, c.radius])
            newY =  1.3*c.radius + diameter*(i+2)
            newCenter = [c.spacing1*4.5,newY]

    
    #drawing middle right white pieces
    center = [c.spacing1*8.5, 1.3*c.radius]
    c.whitePieces.append((center,c.radius))
    newY =  1.3*c.radius + diameter
    newCenter = [c.spacing1*8.5,newY]
    for i in range (4):
            c.whitePieces.append([newCenter, c.radius])
            newY =  1.3*c.radius + diameter*(i+2)
            newCenter = [c.spacing1*8.5,newY]
    
    #drawing rightmost white pieces
    diameter = 2*c.radius
    center = [c.width-c.spacing1/2, c.height -  1.3*c.radius]
    c.whitePieces.append((center,c.radius))
    newY = c.height - 1.3*c.radius - diameter
    newCenter = [c.width-c.spacing1/2,newY]
    c.whitePieces.append([newCenter, c.radius])
    newY = c.height - 1.3*c.radius-diameter*(3)
    newCenter = [c.width-c.spacing1/2,newY]
    
#Draws each piece, called every frame
def drawEverything():
    drawTris()
    pygame.draw.rect(c.myScreen, (0,0,0), pygame.Rect((0,0),(c.width,c.height)), 5)
    for line in c.triLines:
        pygame.draw.line(c.myScreen,c.color,line[0], line[1], 3 )

    for piece in c.blackPieces:
        pygame.draw.circle(c.myScreen,c.color,piece[0], piece[1])

    for piece in c.whitePieces:
         pygame.draw.circle(c.myScreen,c.gray,piece[0], piece[1])
        
    for piece in c.drag_pieces:
        pygame.draw.circle(c.myScreen,piece[0],piece[1],piece[2])
