speedy=0
rocketW=63
rocketH=161
x=1000
aster=[]
Images=[]
ImageW=[]
ImageH=[]
score=0
colliderW=40
colliderH=70
game=True
speed=1
menu=True
scoreClr=100
record=-1
class Asteroid:
    def __init__(self, asterx,y,w,h,img,spd):
        self.x=asterx
        self.y=y
        self.w=w
        self.h=h
        self.img=img
        self.star=False
        self.spd=spd
def setup():
    size(1820,980)
    global background1,rocketImg,aster,Images,ImageH,ImageW
    noCursor()
    for i in range (15):
        aster.append(Asteroid(random(100 ,width-100),2000,328,257,loadImage("aster.png"),5))
    background1=loadImage("background.jpg")
    rocketImg=loadImage("letalo.png")
    Images.append(loadImage("aster.png"))
    Images.append(loadImage("asterr.png"))
    Images.append(loadImage("astero.png"))
    Images.append(loadImage("zezda.png"))
    ImageW.append(328)
    ImageH.append(257)
    ImageW.append(84)
    ImageH.append(81)
    ImageW.append(165)
    ImageH.append(128)
    ImageW.append(82)
    ImageH.append(78)
    textSize(60)
def saveRecord(s):
    file=open("record.txt","r+")
    file.seek(0)
    file.writelines(str(s)+"   ")
    file.close()
def loadRecord():
    file=open("record.txt","r+")
    file.seek(0)
    s=file.read(10)
    return int(s)
    

        
def draw():
    global aster,speedy,rocketImg,Images,ImageH,ImageW,score,colliderW,colliderH,game,speed,menu,scoreClr,record
    image(background1,0,0)
    if menu==False:
        textSize(100)
        if game==True:
            speedy=speedy+0.0015
        else:
            if keyPressed:
                if key==" ":
                    game=True
                    speedy=0
                    speed=1
                    score=0
                    for i in range (len(aster)):
                        aster[i].y=height+100
        if game==True:                    
            image(rocketImg,mouseX,mouseY,rocketW,rocketH)
        for i in range (len(aster)):
            if mouseX+10+colliderW >aster[i].x and mouseX+10 <aster[i].x+aster[i].w and mouseY+35+colliderH>aster[i].y and mouseY+35<aster[i].y+aster[i].h:
                if aster[i].star==True and game==True:
                    score=score+1
                    scoreClr=(scoreClr+random(50,400))%255
                    aster[i].y=height+100 
                else:
                    speedy=0
                    speed=0
                    game=False
                    record=loadRecord()
                    if score>record:
                        saveRecord(score)
                    
            aster[i].y=aster[i].y+(aster[i].spd+speedy)*speed
            if aster[i].y>height:
                aster[i].y=random(-2050,-300)
                aster[i].x=random(100 ,width-100)
                r=int(random(0,4))
                aster[i].img=Images[r]
                aster[i].h=ImageH[r]
                aster[i].w=ImageW[r]
                aster[i].spd=random(3,9)         
                if r==3:
                    aster[i].star=True
                else:
                    aster[i].star=False     
            image(aster[i].img,aster[i].x,aster[i].y,aster[i].w,aster[i].h)      
        
        if game==False:
            k=random(-4,4)
            l=random(-4,4)
            fill(0,0,0)
            text("Game Over",width/3,height/2)
            fill(255,255,0)
            text("Game Over",width/3+k,height/2+l)
            textSize(50)
            fill(255,255,255)
            text("Press SPACE to restart",width/2.95,height/1.1)
            fill(100,255,100)
            text("Press SPACE to restart",width/2.95+k,height/1.1+l)
            textSize(100)
            fill((scoreClr**3)%220,scoreClr,(scoreClr*scoreClr)%255)
            text("record: "+str(record),20,80)
        else:
            textSize(100)
            fill((scoreClr**3)%220,scoreClr,(scoreClr*scoreClr)%255)
            text("score: "+str(score),20,80)
            
            
    else:
        textSize(120)
        fill(255,255,255)
        text("ASTEROIDS",width/3,height/2-4)
        fill(200,0,0)
        text("ASTEROIDS",width/3,height/2)
        k=random(-4,4)
        l=random(-4,4)
        textSize(50)        
        fill(255,255,255)
        text("Press SPACE to begin",width/2.8,height/1.1)
        fill(100,255,100)
        text("Press SPACE to begin",width/2.8+k,height/1.1+l)
        if keyPressed:
            if key==" ":
                game=True
                menu=False
                speedy=0
                speed=1
                score=0
