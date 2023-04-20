import math, copy, random, time, decimal
import birdClass


from cmu_112_graphics import *
# Title Screen

### Helper Functions from 112

def almostEqual(d1, d2, epsilon):
    return ((d1 - d2) < epsilon)


def appStarted(app):
  
    app.mode = 'titleScreenMode'
    app.scrollX = 0
    app.scrollCompetitor = 0
    app.hills = []
    u = 20
    app.x = 0
    app.isGameOver = False
    app.backgroundColorDay = "cadetblue1"
    app.backgroundColorNight = "dodgerblue4"
    app.hillColor = "forestgreen"
    app.timerDelay = 50
    app.numHillsSeen = 0
    app.startingFunction = trainingMode_createRandomHills(app)
    app.dayOrNight = True
    app.verticalShift = app.startingFunction[0]
    app.amplitude = app.startingFunction[1]
    app.frequency = app.startingFunction[2]
    app.period = app.startingFunction[3]
    app.newVerticalShift = 0
    app.newAmplitude = 0
    app.newFrequency = 0
    app.newPeriod = 0
    app.t = 0
    app.firstRun = True
    app.sunColor = "gold1"
    app.moonColor = "cornsilk1"
    app.dayGrass = "green"
    app.nightGrass = "darkgreen"
    app.birdColor = "orange"
    app.peck = birdClass.Bird(20,0,60,40, app.birdColor, 12)
    app.you = birdClass.Bird(20,0,60,40, "pink", 20)
    app.competitor = birdClass.Bird(20,0,60,40, "purple", 40)
    app.counter = 0
    app.howFarInAir = 0
    app.increment = 1
    app.incrementComp = 1
    app.score = 0
    app.totalLength = 0
    
    
    
    
def titleScreenMode_redrawAll(app, canvas):
    if app.dayOrNight == True:
        canvas.create_rectangle(0, 0, 800, 400, fill = app.backgroundColorDay)
        canvas.create_oval(600,0,700,100, fill = app.sunColor, outline = app.sunColor)
        
    
    elif app.dayOrNight == False:
        canvas.create_rectangle(0, 0, 800, 400, fill = app.backgroundColorNight)
        canvas.create_oval(600,0,700,100, fill = app.moonColor, outline = app.moonColor)

    for x in range(0, 800):
        y = 300 + 40*math.sin(x/(300/math.pi))
        if app.dayOrNight == True:
            canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
        elif app.dayOrNight == False:
            canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
    
    canvas.create_polygon(410,240,410,256,435,248, fill='yellow', outline = "black")
    
    canvas.create_oval(380,230,420,270, fill =  "orange")
    canvas.create_oval(405, 235, 415, 250, fill = "white")
    canvas.create_oval(409, 242, 412, 244, fill = "black")

    font = 'Arial 26 bold'

    canvas.create_text(app.width/2, 150, text='Welcome to take Flight',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 200, text='Press enter to customize your bird!',
                       font=font, fill='black')


def titleScreenMode_keyPressed(app, event):
    if event.key == "Enter":
        app.mode = 'customizeBirdMode'


def customizeBirdMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_rectangle(0,0,800,400, fill = "pink")
    #red bird
    canvas.create_polygon(150,170,160,240,210,210, fill='yellow', outline = "black")
    canvas.create_oval(20,120,180,280, fill = "red")
    canvas.create_oval(140, 160, 175, 220, fill = "white")
    canvas.create_oval(155, 170, 172, 190, fill = "black")

    #orange bird
    canvas.create_polygon(350,170,360,240,410,210, fill='yellow', outline = "black")
    canvas.create_oval(220,120,380,280, fill = "orange")
    canvas.create_oval(340, 160, 375, 220, fill = "white")
    canvas.create_oval(355, 170, 372, 190, fill = "black")


    #blue bird
    canvas.create_polygon(550,170,560,240,610,210, fill='yellow', outline = "black")
    canvas.create_oval(420,120,580,280, fill = "darkblue")
    canvas.create_oval(540, 160, 575, 220, fill = "white")
    canvas.create_oval(555, 170, 572, 190, fill = "black")

    #purple bird
    canvas.create_polygon(750,170,760,240,800,210, fill='yellow', outline = "black")
    canvas.create_oval(620,120,780,280, fill = "purple")
    canvas.create_oval(740, 160, 775, 220, fill = "white")
    canvas.create_oval(755, 170, 772, 190, fill = "black")

    canvas.create_text(app.width/2, 80, text='Choose your bird!',
                       font=font, fill='black')
    #customizeBirdMode_chooseColor(app)
    canvas.create_text(app.width/2, 350, text='Press 1 for training mode and 2 for racing mode!', 
                       font=font, fill='black')



def customizeBirdMode_mousePressed(app, event):

    if event.x >= 20 and event.x <= 180 and event.y >= 120 and event.y <= 280:
        app.peck.color = "red"
    elif event.x >= 220 and event.x <= 380 and event.y >= 120 and event.y <= 280:
        app.peck.color = "orange"
    if event.x >= 420 and event.x <= 580 and event.y >= 120 and event.y <= 280:
        app.peck.color = "darkblue"
    if event.x >= 620 and event.x <= 780 and event.y >= 120 and event.y <= 280:
        app.peck.color = "purple"
  
    


def customizeBirdMode_keyPressed(app, event):
    if event.key == "1":
        app.mode = 'trainingMode'
    elif event.key == "2":
        app.mode = 'racingMode'

        

def trainingMode_drawHills(app, canvas, transitioning):
    if transitioning == True:
        for x in range(app.scrollX, app.scrollX + (app.period-app.scrollX)):
            #y = app.verticalShift + app.amplitude*math.sin(x/(app.frequency/math.pi))
            y = app.verticalShift + (x/10000)*app.amplitude*math.sin(x/100)
            x-= app.scrollX
            if app.dayOrNight == True:
                canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
            elif app.dayOrNight == False:
                canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)

    else:
        for x in range(app.scrollX, app.scrollX+app.width):
           # y = app.verticalShift + app.amplitude*math.sin(x/(app.frequency/math.pi))
            y = app.verticalShift + (x/10000)*app.amplitude*math.sin(x/100)
            x-= app.scrollX
            if app.dayOrNight == True:
                canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
            elif app.dayOrNight == False:
                canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            

     

def trainingMode_drawBackground(app, canvas):
    if app.dayOrNight == True:
        canvas.create_rectangle(0, 0, 800, 400, fill = app.backgroundColorDay)
        canvas.create_oval(600,0,700,100, fill = app.sunColor, outline = app.sunColor)
        
    
    elif app.dayOrNight == False:
        canvas.create_rectangle(app.t*800, 0, (app.t+1)*(800), 400, fill = app.backgroundColorNight)
        canvas.create_oval(600,0,700,100, fill = app.moonColor, outline = app.moonColor)


def generatePowerUp(app, canvas):
    if app.mode == "trainingMode":
        pass
def trainingMode_createRandomHills(app):
    
    if app.numHillsSeen == 0:
        startingFunctionsList = []
        for i in range(50):
            verticalShift = random.randint(200,300)
            amplitude = random.randint(40,50)
            frequency = random.randint(300,400)
            length = random.randint(30,40)
            period = length*frequency
            functionParams = (verticalShift, amplitude, frequency, period) 
            startingFunctionsList.append(functionParams)
            randomNumber = random.randint(0, len(startingFunctionsList)-1)
            return(startingFunctionsList[randomNumber])
            
    
    elif app.numHillsSeen == 1:
        functionsList = []
        for i in range(50):
            verticalShift = random.randint(200,300)
            amplitude = random.randint(40,50)
            frequency = random.randint(300,400)
            length = random.randint(30,40)
            period = length*frequency
            functionParams = (verticalShift, amplitude, frequency, period) 
            startingFunctionsList.append(functionParams)
            randomNumber = random.randint(0, len(functionsList)-1)
            return(functionsList[randomNumber])

        
    

def trainingMode_keyPressed(app, event):
    if app.isGameOver:
        return
    if event.key == "Space": 
        app.isGameOver = True
        return
    if event.key == "Up":
        app.dayOrNight = not app.dayOrNight
    if event.key == "Right":
        app.scrollX += app.peck.baseSpeed
    if event.key == "Left":
        app.scrollX -= app.peck.baseSpeed
    if event.key == "Down":
        if app.peck.y1 +10 <= app.peck.minY:
            app.peck.y0+=10
            app.peck.y1+=10
            app.increment+=2

                
       
      


def racingMode_keyPressed(app, event):
    if app.isGameOver:
        return
    if event.key == "Space": 
        app.isGameOver = True
        return
    if event.key == "Up":
        app.dayOrNight = not app.dayOrNight
    if event.key == "Right":
        app.scrollX += 20
    if event.key == "Left":
        app.scrollX -= 20
    if event.key == "Down":
        app.you.y0+=10
        app.you.y1+=10
        app.increment+=2
        
       


    
                   
def trainingMode_timerFired(app):
    if app.scrollX == 0:
        trainingMode_createRandomHills(app)
    if app.isGameOver:
        return 
    if app.peck.isFlying() or app.peck.isTopofHill(app):
        app.increment += 1
        app.howFarInAir+=20
    if app.peck.landed:
        app.increment -= app.increment-1
        app.counter += app.howFarInAir+60
        app.howFarInAir-= app.howFarInAir

    if app.peck.grounded:
        app.counter += 20
        app.counter += app.howFarInAir
        app.howFarInAir-= app.howFarInAir
        app.increment -= app.increment-1

    app.scrollX += app.peck.baseSpeed
    
    
    
    


def racingMode_drawBackground(app, canvas):
    if app.dayOrNight == True:
        canvas.create_rectangle(app.t*800, 0, (app.t+1)*(800), 400, fill = app.backgroundColorDay)
        canvas.create_oval(600,0,700,100, fill = app.sunColor, outline = app.sunColor)
        
    
    elif app.dayOrNight == False:
        canvas.create_rectangle(app.t*800, 0, (app.t+1)*(800), 400, fill = app.backgroundColorNight)
        canvas.create_oval(600,0,700,100, fill = app.moonColor, outline = app.moonColor)

def racingMode_drawHills(app, canvas, transitioning):
    if transitioning == True:
        if app.scrollX<=4800:
            for x in range(app.scrollX, app.scrollX + (4800-app.scrollX)):
                y = 200 + 40*math.sin(x/(300/math.pi))
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            for x in range(app.scrollX+app.width, app.scrollX + (4800-app.scrollX), -1):
                y = 200 + 30*math.sin(math.pi*x/150)+ math.cos(math.pi*x/150)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
        elif app.scrollX > 4800 and app.scrollX<= 9600:
            for x in range(app.scrollX, app.scrollX + (9600-app.scrollX)):
                y = 200 + 30*math.sin(math.pi*x/150)+ math.cos(math.pi*x/150)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            for x in range(app.scrollX+app.width, app.scrollX + (9600-app.scrollX), -1):
                y = 200+30*math.sin((x+100)/150)*math.cos((x+100)/60)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
        elif app.scrollX > 9600 and app.scrollX<= 15000:
            for x in range(app.scrollX, app.scrollX + (15000-app.scrollX)):
                y = 200+30*math.sin((x+100)/150)*math.cos((x+100)/60)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            for x in range(app.scrollX+app.width, app.scrollX + (15000-app.scrollX), -1):
                y = 200
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            

            

    else:
        if app.scrollX<=4800:
            for x in range(app.scrollX, app.scrollX + app.width):
                y = 200 + 40*math.sin(x/(300/math.pi))
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
        elif app.scrollX> 4800 and app.scrollX<= 9600:
            for x in range(app.scrollX, app.scrollX + app.width):
                y = 200 + 30*math.sin(math.pi*x/150)+ math.cos(math.pi*x/150)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
        elif app.scrollX> 9600 and app.scrollX<= 15000:
            for x in range(app.scrollX, app.scrollX + app.width):
                y = 200+30*math.sin((x+100)/150)*math.cos((x+100)/60)
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
        elif app.scrollX> 15000 and app.scrollX<= 17000:
            for x in range(app.scrollX, app.scrollX + app.width):
                y = 200
                x-= app.scrollX
                if app.dayOrNight == True:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.dayGrass, outline = app.dayGrass)
                elif app.dayOrNight == False:
                    canvas.create_rectangle(x,y,x+1,400, fill = app.nightGrass, outline = app.nightGrass)
            return
        

def racingMode_timerFired(app):
    if app.scrollX == 0:
        trainingMode_createRandomHills(app)
    if app.isGameOver:
        return 
    if app.you.isFlying() or app.you.isTopofHill(app):
        app.increment += 1
        app.howFarInAir+=20
    if app.competitor.isFlying() or app.competitor.isTopofHillComp(app):
        app.incrementComp += 1
    if app.you.landed:
        app.increment -= app.increment-1
        app.counter += app.howFarInAir+60
        app.howFarInAir-= app.howFarInAir
    if app.competitor.landed:
        app.incrementComp -= app.incrementComp-1
    if app.competitor.grounded:
        app.incrementComp -= app.incrementComp-1

    if app.you.grounded:
        app.counter += 20
        app.counter += app.howFarInAir
        app.howFarInAir-= app.howFarInAir
        app.increment -= app.increment-1
    app.scrollX += app.you.baseSpeed
    app.scrollCompetitor += app.competitor.baseSpeed

    
    
      

def racingMode_redrawAll(app, canvas):
    competitorDraw = False
    transitioning = False
    
    

    

    centerX = app.width/2 - app.scrollX 
    centerY = app.height/2
    
    length = app.period
   
    racingMode_drawBackground(app, canvas)
    
    if not app.you.isTopofHill(app) and not app.you.isFlying():
        app.you.startBird(app, canvas)
    if not app.competitor.isTopofHillComp(app) and not app.competitor.isFlying():
        app.competitor.startCompetitor(app, canvas)
        competitorDraw = True

    if app.scrollX <= 4800-app.width:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)

    if app.scrollCompetitor <= 4800-app.width:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]
        if app.competitor.isTopofHillComp(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
            competitorDraw = True
        elif app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
            competitorDraw = True
        
    elif app.scrollX > 4800-app.width and app.scrollX <= 4800:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        transitioning = True
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)

    if app.scrollCompetitor > 4800-app.width and app.scrollCompetitor <= 4800:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]
        if app.competitor.isTopofHillComp(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
        elif app.you.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)

    elif app.scrollX > 4800 and app.scrollX <= 9600-app.width:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        transitioning = False
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)

    if app.scrollCompetitor > 4800 and app.scrollCompetitor <= 9600-app.width:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]
        if app.competitor.isTopofHillComp(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
        elif app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)

    elif app.scrollX > 9600-app.width and app.scrollX <= 9600:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        transitioning = True
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)

    if app.scrollCompetitor > 9600-app.width and app.scrollCompetitor <= 9600:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]
        if app.competitor.isTopofHill(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
        elif app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
    
    elif app.scrollX > 9600 and app.scrollX <= 15000-app.width:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        transitioning = False
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)

    if app.scrollCompetitor > 9600 and app.scrollCompetitor <= 15000-app.width:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1] 
        if app.competitor.isTopofHill(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
        elif app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngleCompetitor, bottomYCompetitor)
    
    elif app.scrollX > 15000-app.width and app.scrollX <= 15000:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1] 
        transitioning = True
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
    if app.scrollCompetitor > 15000-app.width and app.scrollCompetitor <= 15000:
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]  
        if app.competitor.isTopofHill(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngle, bottomY)
        elif app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngle, bottomY)
    
    elif app.scrollX > 15000 and app.scrollX <= 17000:
        maximumAngle = app.you.getMaxAngle(app, canvas)[0]
        bottomY = app.you.getMaxAngle(app, canvas)[1]
        maximumAngleCompetitor = app.competitor.getMaxAngleCompetitor(app)[0]
        bottomYCompetitor = app.competitor.getMaxAngleCompetitor(app)[1]
        transitioning = False
        racingMode_drawHills(app, canvas, transitioning)
        if app.you.isTopofHill(app) and not app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.you.fly(app, canvas, maximumAngle, bottomY)
        if app.competitor.isTopofHill(app) and not app.competitor.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngle, bottomY)
        elif app.you.isFlying():
            app.competitor.flyCompetitor(app, canvas, maximumAngle, bottomY)
    
    
   

    
    
                      





def trainingMode_redrawAll(app, canvas):
    transitioning = False
    
    
  
   
    trainingMode_drawBackground(app, canvas)
    if not app.peck.isTopofHill(app) and not app.peck.isFlying():
        app.peck.startBird(app, canvas)
    
    trainingMode_drawHills(app, canvas, transitioning)
    maximumAngle = app.peck.getMaxAngle(app, canvas)[0]
    bottomY = app.peck.getMaxAngle(app, canvas)[1]
    
    if app.peck.isTopofHill(app) and not app.peck.isFlying():
        

    
        app.peck.fly(app, canvas, maximumAngle, bottomY)
        
    elif app.peck.isFlying():

        app.peck.fly(app, canvas, maximumAngle, bottomY)
        
        

    x = app.width/2
    canvas.create_text(x, 40, text= f'Player score: {app.scrollX}',
                       fill='black')




        
            
    



        
      
        
    
distanceFlown = 0
#peck = Bird(20,0,60,40,"red", 5)
#peck.drawBird(app, canvas)
runApp(width = 800,height = 400)