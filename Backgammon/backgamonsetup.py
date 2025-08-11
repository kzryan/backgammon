import sys, pygame
import configbackgamon as c
import random

def diceroll():
    diceroll = random.randint(1,6)
    c.rolledNums.append(diceroll)

    if (diceroll==1):
        return [pygame.image.load("images/dice1.png"),1]

    if (diceroll==2):
        return [pygame.image.load("images/dice2.png"),2]

    if (diceroll==3):
        return [pygame.image.load("images/dice3.png"),3]

    if (diceroll==4):
        return [pygame.image.load("images/dice4.png"),4]

    if (diceroll==5):
        return [pygame.image.load("images/dice5.png"),5]

    if (diceroll==6):
        return [pygame.image.load("images/dice6.png"),6]

def reRoll():
    if(c.movesLeft==0):
        print("No moves left, switching turns")
        if(c.whiteturn):
            c.whiteturn=False
            c.blackturn=True
            font = pygame.font.Font(None, 32)
            alert_text='Black\'s Turn'
            text = font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([text, alert_text])
        elif(c.blackturn):
            c.whiteturn=True
            c.blackturn=False
            font = pygame.font.Font(None, 32)
            alert_text = 'White\'s Turn'
            text = font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([text,alert_text])

        c.roll1 = diceroll()
        c.roll2 = diceroll()
        c.totalRoll=c.roll1[1]+c.roll2[1]
        if c.roll1[1]==c.roll2[1]:
            c.totalRoll*=2
        c.movesLeft = c.totalRoll

        if(len(c.whitedeadRectangles) != 0):
            font = pygame.font.Font(None, 32)
            alert_text='Dead Piece'
            text = font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([text,alert_text])
        if(len(c.blackdeadRectangles) != 0):
            font = pygame.font.Font(None, 32)
            alert_text='Dead Piece'
            text = font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([text,alert_text])

    

def checkTurn():
     if(c.roll1[1]>c.roll2[1]):
          c.blackturn = True
          print("its black's turn")
          font = pygame.font.Font(None, 32)
          alert_text='Black\'s Turn'
          text = font.render(alert_text, True, (255,255,255), (0,0,0))
          c.alerts.append([text, alert_text])
          return c.blackturn
     elif(c.roll2[1]<c.roll1[1]):
          c.whiteturn = True
          print("its white's turn")
          font = pygame.font.Font(None, 32)
          alert_text = 'White\'s Turn'
          text = font.render(alert_text, True, (255,255,255), (0,0,0))
          c.alerts.append([text,alert_text])
          return c.whiteturn
     else:
          #tie
        c.roll1 = diceroll()
        c.roll2 = diceroll()
        c.totalRoll=c.roll1[1]+c.roll2[1]
        if c.roll1[1]==c.roll2[1]:
            c.totalRoll*=2
        c.movesLeft = c.totalRoll
        checkTurn()

def CircleClick(circle_x, circle_y, radius, mouse_x, mouse_y):
     
     distance=((circle_x-mouse_x)**2+(circle_y-mouse_y)**2)**0.5

     return distance <=radius

def drawTri():
    start= [0,0]
    end= [c.spacing1/2,c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             c.tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2
                else:
                    end[1]+=c.spacing2
                    end[0]+=c.spacing1/2

        
        #moving to the right
        c.tri.append([end.copy(),(end.copy()[0], c.height)])

        c.tri.append([(end.copy()[0]+c.spacing1,end.copy()[1]),(end.copy()[0]+c.spacing1,c.height)])

        start=end.copy()
        start[0]+=c.spacing1*2
        end=start.copy()
        end[0]+=c.spacing1/2
        end[1]+=c.spacing2
        c.tri.append([start.copy(),(start.copy()[0], c.height)])


    for j in range(NOL):
        c.tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=c.spacing1/2
                end[1]-=c.spacing2
            else:
                end[1]+=c.spacing2
                end[0]+=c.spacing1/2

    start= [0,c.height]
    end= [c.spacing1/2,c.height-c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             c.tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2
                else:
                    end[1]-=c.spacing2
                    end[0]+=c.spacing1/2

        
        #moving to the right
        start=end.copy()
        start[0]+=c.spacing1*2
        end=start.copy()
        end[0]+=c.spacing1/2
        end[1]-=c.spacing2

    for j in range(NOL):
        c.tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=c.spacing1/2
                end[1]+=c.spacing2
            else:
                end[1]-=c.spacing2
                end[0]+=c.spacing1/2


def drawBlackPieces():
   #Drawing far left black pieces
    diameter=2*c.radius
    center= [c.spacing1/2,1.3*c.radius]
    c.blackpieces.append([center,c.radius,12])
    newY=1.3*c.radius+diameter
    newCenter= [c.spacing1/2,newY]
    for i in range(4):
            c.blackpieces.append([newCenter, c.radius,12])
            newY=1.3*c.radius+diameter*(i+2)
            newCenter=[c.spacing1/2,newY]
    #drawing middle left black pieces
    Center=[c.spacing1*4.5, c.height-1.3*c.radius]
    c.blackpieces.append([Center, c.radius,7])
    newY=c.height-1.3*c.radius-diameter
    newCenter=[c.spacing1*4.5,newY]
    for i in range(2):
            c.blackpieces.append([newCenter,c.radius,7])
            newY=c.height-1.3*c.radius-diameter*(i+2)
            newCenter=[c.spacing1*4.5,newY]
   #drawing middle right black pieces
    Center=[c.spacing1*8.5, c.height-1.3*c.radius]
    c.blackpieces.append([Center, c.radius,5])
    newY=c.height-1.3*c.radius-diameter
    newCenter=[c.spacing1*8.5,newY]
    for i in range(4):
            c.blackpieces.append([newCenter,c.radius,5])
            newY=c.height-1.3*c.radius-diameter*(i+2)
            newCenter=[c.spacing1*8.5,newY]
    #drawing far right pieces
    center= [c.width-c.spacing1/2,1.3*c.radius]
    c.blackpieces.append([center,c.radius,23])
    newY=1.3*c.radius+diameter
    newCenter= [c.width-c.spacing1/2,newY]
    c.blackpieces.append([newCenter, c.radius,23])
    newY=1.3*c.radius+diameter*(3)
    newCenter=[c.width-c.spacing1/2,newY]
    '''for i in range (6):
        if i==0:
            pass
        else:
             pieces.append(((spacing1/2,i*1.972*radius), radius))
        #pieces.append(((spacing1/2,i*2*radius), radius))'''


def drawWhitePieces():
    center= [c.spacing1/2,c.height-1.3*c.radius]
    c.whitepieces.append([center,c.radius,11])
    newY=c.height-1.3*c.radius-c.diameter
    newCenter= [c.spacing1/2,newY]
    for i in range(4):
            c.whitepieces.append([newCenter, c.radius,11])
            newY=c.height-1.3*c.radius-c.diameter*(i+2)
            newCenter=[c.spacing1/2,newY]
        #drawing middle left white pieces
    Center=[c.spacing1*4.5, 1.3*c.radius]
    c.whitepieces.append([Center, c.radius,16])
    newY=1.3*c.radius+c.diameter
    newCenter=[c.spacing1*4.5,newY]
    for i in range(2):
            c.whitepieces.append([newCenter,c.radius,16])
            newY=1.3*c.radius+c.diameter*(i+2)
            newCenter=[c.spacing1*4.5,newY]
#drawing middle right white pieces
    Center=[c.spacing1*8.5, 1.3*c.radius]
    c.whitepieces.append([Center, c.radius,18])
    newY=1.3*c.radius+c.diameter
    newCenter=[c.spacing1*8.5,newY]
    for i in range(4):
            c.whitepieces.append([newCenter,c.radius,18])
            newY=1.3*c.radius+c.diameter*(i+2)
            newCenter=[c.spacing1*8.5,newY]
    #drawing far right white pieces
    center= [c.width-c.spacing1/2,c.height-1.3*c.radius]
    c.whitepieces.append([center,c.radius,0])
    newY=c.height-1.3*c.radius-c.diameter
    newCenter= [c.width-c.spacing1/2,newY]
    c.whitepieces.append([newCenter, c.radius,0])
    newY=c.height-1.3*c.radius-c.diameter*(3)
    newCenter=[c.width-c.spacing1/2,newY]

def CreateSpaces():
    y=c.height/2
    x=c.width-c.spacing1
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x-=c.spacing1

    x=c.spacing1*5
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x-=c.spacing1

    x,y=0,0
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x+=c.spacing1
    
    x=c.spacing1*8
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x+=c.spacing1

def DrawEverything():
    pygame.draw.rect(c.myScreen, c.color, pygame.Rect((0,0),(c.width,c.height)), 7)

    for line in c.tri:
        pygame.draw.line(c.myScreen,c.color,line[0], line[1], 3 )

    for piece in c.blackpieces:
        pygame.draw.circle(c.myScreen, c.color, piece[0], piece[1])

    for piece in c.whitepieces:
         pygame.draw.circle(c.myScreen, c.gray, piece[0], piece[1])
    
    for piece in c.dragPieces:
         pygame.draw.circle(c.myScreen, piece[0], piece[1], piece[2])

    drawDeadpieces()
    for rect in c.whitedeadRectangles:
         #print("Drawing dead rect")
         pygame.draw.rect(c.myScreen,c.gray,rect[0])
    for rect in c.blackdeadRectangles:
         #print("Drawing dead rect")
         pygame.draw.rect(c.myScreen,c.color,rect[0])

    for alert in c.alerts:
        alert_rect = alert[0].get_rect()

        #if it says dead piece put it in top left
        if(alert[1] == "Dead Piece"):
             alert_rect.center = (100,40)
        #if it says blac/white put it in top right
        if(alert[1] == "Black\'s Turn" or alert[1] == "White\'s Turn"):
            alert_rect.center = (c.width -100, 40)
        if(alert[1] == "Click Space to Resummon"):
             alert_rect.center = (c.width/2,c.height/2)
             
        c.myScreen.blit(alert[0],alert_rect)
    
    
    c.myScreen.blit(c.roll1[0], (6.10*c.spacing1, c.height/2.75))
    c.myScreen.blit(c.roll2[0], (7.13*c.spacing1, c.height/2.75))
    c.myScreen.blit(c.Roll, (649,649))

def drawDeadpieces():
     wleft = c.spacing1*6
     ctop = 10
     width = c.spacing1/2
     height = 20
     c.whitedeadRectangles = []
     c.blackdeadRectangles = []

     for piece in c.whitedeadpieces:
        c.whitedeadRectangles.append((pygame.Rect(wleft,ctop,width,height),piece))
        ctop+=30

     btop = 10
     bleft = wleft+width
     for piece in c.blackdeadpieces:
        c.blackdeadRectangles.append((pygame.Rect(bleft,btop,width,height),piece))
        btop+=30

    
