import math, copy, random, time, decimal


from cmu_112_graphics import *
def almostEqual(d1, d2, epsilon=1):
    return (abs(d2 - d1) < epsilon)

class Bird(object):

    def __init__(self, x0, y0, x1, y1, color, speed):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.maxAngle = 0
        self.globalMax = 1000000
        self.baseSpeed = speed
        self.minY = 0
        self.flyDistance = 0
        self.reachedTop = True
        self.grounded = True
        self.landed = False
        self.groundedComp = True
        self.landedComp = False
        
        

    def birds(self, app):
        self.name = app.birdName

    def startCompetitor(self, app, canvas):
        if app.scrollCompetitor<=4800:
            fixedX = 40
            x = 20
            self.minY = 200 + 40*math.sin((x+app.scrollCompetitor)/(300/math.pi))
            self.x0 = app.scrollCompetitor-app.scrollX
            self.y0 = self.minY-40
            self.x1 = app.scrollCompetitor-app.scrollX + 40
            self.y1 = self.minY
            canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
            canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
            canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
            canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
        elif app.scrollCompetitor > 4800 and app.scrollCompetitor < 9600:
            fixedX = 40
            x = 20
            self.minY = 200 + 30*math.sin(math.pi*(x+app.scrollCompetitor)/150)+ math.cos(math.pi*(x+app.scrollCompetitor)/150)
            self.x0 = app.scrollCompetitor-app.scrollX
            self.y0 = self.minY-40
            self.x1 = app.scrollCompetitor-app.scrollX + 40
            self.y1 = self.minY
            canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
            canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
            canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
            canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
        elif app.scrollCompetitor > 9600 and app.scrollCompetitor <= 15000:
            fixedX = 40
            x = 20
            self.minY = 200+30*math.sin((x+app.scrollCompetitor+100)/150)*math.cos((x+app.scrollCompetitor+100)/60)
            self.x0 = app.scrollCompetitor-app.scrollX
            self.y0 = self.minY-40
            self.x1 = app.scrollCompetitor-app.scrollX + 40
            self.y1 = self.minY
            canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
            canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
            canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
            canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
        else:
            fixedX = 40
            x = 20
            self.minY = 200
            self.x0 = app.scrollCompetitor-app.scrollX
            self.y0 = self.minY-40
            self.x1 = app.scrollCompetitor-app.scrollX + 40
            self.y1 = self.minY
            canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
            canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
            canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
            canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")

    def startBird(self, app, canvas):
        
        if app.mode == 'trainingMode':
            angle = self.getAngle(app)
            
            self.landed = True
            self.grounded = True
            self.landed = False
            fixedX = 60
            x = 40
        
        
                
            
            
            self.minY = app.verticalShift + ((x+app.scrollX)/10000)*app.amplitude*math.sin((x+app.scrollX)/100)
            self.x0 = fixedX-40
            self.y0 = self.minY-40
            self.x1 = fixedX
            self.y1 = self.minY
            if angle > 0:
                beak = [self.x1-10,self.y0+10,self.x1-8,self.y0+26,self.x1+15,self.y0+6]
            elif angle == 0:
                beak = [self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18]
            else:
                beak = [self.x1-10,self.y0+10,self.x1-12,self.y0+26,self.x1+15,self.y0+30]

            canvas.create_polygon(beak[0],beak[1],beak[2],beak[3],beak[4],beak[5], fill='yellow', outline = "black")
            canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color, outline = "black")
            canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
            canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
                
        elif app.mode == 'racingMode':
            if app.scrollX<=4800:
                fixedX = 60
                x = 40
                self.minY = 200 + 40*math.sin((x+app.scrollX)/(300/math.pi))
                self.x0 = fixedX-40
                self.y0 = self.minY-40
                self.x1 = fixedX
                self.y1 = self.minY
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
            elif app.scrollX > 4800 and app.scrollX < 9600:
                fixedX = 60
                x = 40
                self.minY = 200 + 30*math.sin(math.pi*(x+app.scrollX)/150)+ math.cos(math.pi*(x+app.scrollX)/150)
                self.x0 = fixedX-40
                self.y0 = self.minY-40
                self.x1 = fixedX
                self.y1 = self.minY
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
            elif app.scrollX > 9600 and app.scrollX <= 15000:
                fixedX = 60
                x = 40
                self.minY = 200+30*math.sin((x+app.scrollX+100)/150)*math.cos((x+app.scrollX+100)/60)
                self.x0 = fixedX-40
                self.y0 = self.minY-40
                self.x1 = fixedX
                self.y1 = copy.deepcopy(self.minY)
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
            else:
                fixedX = 60
                x = 40
                self.minY = 200
                self.x0 = fixedX-40
                self.y0 = self.minY-40
                self.x1 = fixedX
                self.y1 = self.minY
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")


          
                
            

        
            
    


    def getBirdCoordinates(self, app, canvas):
        return [self.x0, self.y0, self.x1, self.y1]
    
           
    def isGoodLanding(self, app, canvas):
        if self.color == "pink":
            angle = self.getAngle(app)
        elif self.color == "purple":
            angle = self.getAngleCompetitor(app)
        if angle > 0:
            if self.baseSpeed >= 10:
                self.baseSpeed-= 4
        elif angle <= 0:
            self.baseSpeed += 4

    
    def getAngle(self, app):
        x = 40
        if app.mode == 'trainingMode':
            angle = -((x+app.scrollX)*math.cos((x+app.scrollX)/100)/1000000) + (math.sin((x+app.scrollX)/100)/10000)
        elif app.mode == 'racingMode':
            if app.scrollX <= 4800:
                angle = ((40*math.pi)/300* math.cos((x+app.scrollX)/(300/math.pi)))
            elif app.scrollX <= 9600:
                angle = ((math.pi/5)*math.cos(math.pi*(x+app.scrollX)/150)-(math.pi/150)*math.sin(math.pi*(x+app.scrollX)/150))
            elif app.scrollX <= 15000:
                angle = (0.2*(math.cos(((x+app.scrollX)+100)/150)**2)-0.2*(math.sin(((x+app.scrollX)+100)/150)**2))
            else:
                angle = 0
        return angle
    
    def getAngleCompetitor(self, app):
        x = 20
        if app.scrollCompetitor <= 4800:
            angle = ((40*math.pi)/300* math.cos((x+app.scrollCompetitor)/(300/math.pi)))
        elif app.scrollCompetitor <= 9600:
            angle = ((math.pi/5)*math.cos(math.pi*(x+app.scrollCompetitor)/150)-(math.pi/150)*math.sin(math.pi*(x+app.scrollCompetitor)/150))
        elif app.scrollCompetitor <= 15000:
            angle = (0.2*(math.cos(((x+app.scrollCompetitor)+100)/150)**2)-0.2*(math.sin(((x+app.scrollCompetitor)+100)/150)**2))
        else:
            angle = 0
        return angle



    def isFlying(self):
        if self.y1<self.minY:
            self.grounded = False
            return True
        else:
            return False

    def getMaxAngle(self, app, canvas):
        if app.mode == 'trainingMode':
            fixedX = 60
            x = 40 
            angle = -((x+app.scrollX)*math.cos((x+app.scrollX)/100)/1000000) + (math.sin((x+app.scrollX)/100)/10000)
            if angle>= self.maxAngle:
                self.maxAngle = angle
            bottomY = self.minY
            currentScroll = app.scrollX
            return [self.maxAngle, bottomY, currentScroll]
        elif app.mode == 'racingMode':
            fixedX = 60
            x = 40
            if app.scrollX<= 4800:
                angle = (40*math.cos((math.pi*(x+app.scrollX))/300)*(math.pi/300))
                if angle>= self.maxAngle:
                    self.maxAngle = angle
                bottomY = self.minY
                currentScroll = app.scrollX
                return [self.maxAngle, bottomY, currentScroll]
            elif app.scrollX > 4800 and app.scrollX <= 9600:
                angle = ((math.pi/5)*math.cos(math.pi*(x+app.scrollX)/150)-(math.pi/150)*math.sin(math.pi*(x+app.scrollX)/150))
                if angle>= self.maxAngle:
                    self.maxAngle = angle
                bottomY = self.minY
                currentScroll = app.scrollX
                return [self.maxAngle, bottomY, currentScroll]
            elif app.scrollX > 9600 and app.scrollX <= 15000:
                angle = (0.2*(math.cos(((x+app.scrollX)+100)/150)**2)-0.2*(math.sin(((x+app.scrollX)+100)/150)**2))

                if angle>= self.maxAngle:
                    self.maxAngle = angle
                bottomY = self.minY
                currentScroll = app.scrollX
                return [self.maxAngle, bottomY, currentScroll]
            elif app.scrollX > 15000 and app.scrollX <= 17000:
                self.maxAngle = 0
                bottomY = self.minY
                currentScroll = app.scrollX
                return [self.maxAngle, bottomY, currentScroll]
            
    def getMaxAngleCompetitor(self, app):
        x = 20
        if app.scrollCompetitor<= 4800:
            angle = (40*math.cos((math.pi*(x+app.scrollCompetitor))/300)*(math.pi/300))
            if angle>= self.maxAngle:
                self.maxAngle = angle
            bottomY = self.minY
            currentScroll = app.scrollX
            return [self.maxAngle, bottomY, currentScroll]
        elif app.scrollCompetitor > 4800 and app.scrollCompetitor <= 9600:
            angle = ((math.pi/5)*math.cos(math.pi*(x+app.scrollCompetitor)/150)-(math.pi/150)*math.sin(math.pi*(x+app.scrollCompetitor)/150))
            if angle>= self.maxAngle:
                self.maxAngle = angle
            bottomY = self.minY
            currentScroll = app.scrollCompetitor
            return [self.maxAngle, bottomY, currentScroll]
        elif app.scrollCompetitor > 9600 and app.scrollCompetitor <= 15000:
            angle = (0.2*(math.cos(((x+app.scrollCompetitor)+100)/150)**2)-0.2*(math.sin(((x+app.scrollCompetitor)+100)/150)**2))

            if angle>= self.maxAngle:
                self.maxAngle = angle
            bottomY = self.minY
            currentScroll = app.scrollCompetitor
            return [self.maxAngle, bottomY, currentScroll]
        elif app.scrollCompetitor > 15000 and app.scrollCompetitor <= 17000:
            self.maxAngle = 0
            bottomY = self.minY
            currentScroll = app.scrollCompetitor
            return [self.maxAngle, bottomY, currentScroll]

            
         


    def isTopofHill(self, app):
        if app.mode == 'trainingMode':
            x = 40
            y = app.verticalShift + ((x+app.scrollX)/10000)*app.amplitude*math.sin((x+app.scrollX)/100)
            localMax = app.verticalShift - ((x+app.scrollX)/10000)*app.amplitude
            if localMax <= self.globalMax:
                self.globalMax = localMax
            if almostEqual(self.y1, self.globalMax,0.5):
                self.baseSpeed += 1
                return True
            else:
                return False
        elif app.mode == 'racingMode':
            x = 40 
            if app.scrollX <= 4800:
                y = 200 + 40*math.sin((x+app.scrollX)/(300/math.pi))
                maxOfFunction = 200-40
                if almostEqual(self.y1, maxOfFunction,epsilon=1):
                    self.landed = False
                    return True
                else:
                    return False

    def isTopofHillComp(self, app):
        x = 20 
        if app.scrollCompetitor <= 4800:
            y = 200 + 40*math.sin((x+app.scrollCompetitor)/(300/math.pi))
            maxOfFunction = 200-40
            if almostEqual(self.y1, maxOfFunction,epsilon=1):
                self.landed = False
                return True
            else:
                return False
    

    def getXAtTopOfHill(self, app):
        if app.mode == 'trainingMode':
            x = 40
            y = app.verticalShift + ((x+app.scrollX)/10000)*app.amplitude*math.sin((x+app.scrollX)/100)
            maxOfFunction = app.verticalShift-((x+app.scrollX)/10000)*app.amplitude
            if almostEqual(self.y1, maxOfFunction,0.1):
                startX = copy.deepcopy(app.scrollX)
                
                return startX
            

        
    def fly(self, app, canvas, maximumAngle, bottomY):

        self.landed = False
        x = 40 
        if app.mode == 'trainingMode':
            self.minY = app.verticalShift + ((x+app.scrollX)/10000)*app.amplitude*math.sin((x+app.scrollX)/100)
        elif app.mode == 'racingMode':

            if app.scrollX <= 4800:
                self.minY = 200 + 40*math.sin((x+app.scrollX)/(300/math.pi))

                
            elif app.scrollX > 4800 and app.scrollX <= 9600:
                self.minY = 200 + 30*math.sin(math.pi*(x+app.scrollX/150)+ math.cos(math.pi*(x+app.scrollX)/150))
            elif app.scrollX > 9600 and app.scrollX <= 15000: 
                self.minY = 200 + 30*math.sin(((x+app.scrollX)+100)/150)*math.cos(((x+app.scrollX)+100)/60)
        self.grounded = False
    
        fixedX = 60
       
    
        

        if self.y1 == self.minY and app.increment == 1:


            if app.mode == "trainingMode":
                self.y0 = bottomY- (((self.baseSpeed*app.increment) - 0.1*(1/maximumAngle)*(app.increment**2)//1)) - 40
                self.y1 = bottomY - (((self.baseSpeed*app.increment) - 0.1*(1/maximumAngle)*(app.increment**2)//1))
            
            elif app.mode == "racingMode":
                self.y0 = bottomY- (((self.baseSpeed*app.increment) - 0.5*(1/maximumAngle)*(app.increment**2)//1)) - 40
                self.y1 = bottomY - (((self.baseSpeed*app.increment) - 0.5*(1/maximumAngle)*(app.increment**2)//1))
            

         
        
        elif self.y1 < self.minY:
            
            if app.mode == "trainingMode":
                self.y0 = bottomY- (((self.baseSpeed*app.increment) - 0.1*(1/maximumAngle)*(app.increment**2)//1)) - 40
                self.y1 = bottomY - (((self.baseSpeed*app.increment) - 0.1*(1/maximumAngle)*(app.increment**2)//1))
                amountDerivative = self.baseSpeed - (40000*maximumAngle*app.increment//1)

            elif app.mode == "racingMode":
                self.y0 = bottomY- (((self.baseSpeed*app.increment) - 0.5*(1/maximumAngle)*(app.increment**2)//1)) - 40
                self.y1 = bottomY - (((self.baseSpeed*app.increment) - 0.5*(1/maximumAngle)*(app.increment**2)//1))
                amountDerivative = self.baseSpeed - ((1/maximumAngle)*2*app.increment//1)
            #self.y0 = bottomY- ((self.baseSpeed*app.increment) - 0.5*2*(app.increment**2)) - 40
            #self.y1 = bottomY - ((self.baseSpeed*app.increment) - 0.5*2*(app.increment**2)) 
            if amountDerivative > 0:
                beak = [self.x1-10,self.y0+10,self.x1-8,self.y0+26,self.x1+15,self.y0+6]
            elif amountDerivative == 0:
                beak = [self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18]
            else:
                beak = [self.x1-10,self.y0+10,self.x1-12,self.y0+26,self.x1+15,self.y0+30]
            
            
            if self.y1 >= self.minY and app.increment > 1:
                self.landed = True
                self.x0 = fixedX-40
                self.y0 = self.minY-40
                self.x1 = fixedX
                self.y1 = self.minY
                
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill = "yellow", outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
    
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
                self.isGoodLanding(app, canvas)  
                return 
                
            else:
                canvas.create_polygon(beak[0],beak[1],beak[2],beak[3],beak[4],beak[5], fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
            
    def flyCompetitor(self, app, canvas, maximumAngle, bottomY):
        self.landedComp = False
        x = 20 
        if app.scrollCompetitor <= 4800:
            self.minY = 200 + 40*math.sin((x+app.scrollCompetitor)/(300/math.pi))  
        elif app.scrollCompetitor > 4800 and app.scrollCompetitor <= 9600:
            self.minY = 200 + 30*math.sin(math.pi*(x+app.scrollCompetitor/150)+ math.cos(math.pi*(x+app.scrollCompetitor)/150))
        elif app.scrollCompetitor > 9600 and app.scrollCompetitor <= 15000: 
            self.minY = 200 + 30*math.sin(((x+app.scrollCompetitor)+100)/150)*math.cos(((x+app.scrollCompetitor)+100)/60)
        self.groundedComp = False
    
        fixedX = 60
       

        if self.y1 == self.minY and app.incrementComp == 1:
            self.y0 = bottomY- (((self.baseSpeed*app.incrementComp) - (1/maximumAngle)*(app.incrementComp**2)//1)) - 40
            self.y1 = bottomY - (((self.baseSpeed*app.incrementComp) - (1/maximumAngle)*(app.incrementComp**2)//1))
            

         
        
        elif self.y1 < self.minY:
            self.y0 = bottomY- (((self.baseSpeed*app.incrementComp) - (1/maximumAngle)*(app.incrementComp**2)//1)) - 40
            self.y1 = bottomY - (((self.baseSpeed*app.incrementComp) - (1/maximumAngle)*(app.incrementComp**2)//1))
            amountDerivative = self.baseSpeed - ((1/maximumAngle)*2*app.incrementComp//1)
            #self.y0 = bottomY- ((self.baseSpeed*app.increment) - 0.5*2*(app.increment**2)) - 40
            #self.y1 = bottomY - ((self.baseSpeed*app.increment) - 0.5*2*(app.increment**2)) 
            if amountDerivative > 0:
                beak = [self.x1-10,self.y0+10,self.x1-8,self.y0+26,self.x1+15,self.y0+6]
            elif amountDerivative == 0:
                beak = [self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18]
            else:
                beak = [self.x1-10,self.y0+10,self.x1-12,self.y0+26,self.x1+15,self.y0+30]
            
            
            if self.y1 >= self.minY and app.incrementComp > 1:
                self.landedComp = True
                self.x0 = app.scrollCompetitor-app.scrollX
                self.y0 = self.minY-40
                self.x1 = app.scrollCompetitor-app.scrollX + 40
                self.y1 = self.minY
                
                canvas.create_polygon(self.x1-10,self.y0+10,self.x1-10,self.y0+26,self.x1+15,self.y0+18, fill = "yellow", outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
    
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
                self.isGoodLanding(app, canvas)
                return 
                
            else:
                canvas.create_polygon(beak[0],beak[1],beak[2],beak[3],beak[4],beak[5], fill='yellow', outline = "black")
                canvas.create_oval(self.x0,self.y0,self.x1, self.y1, fill =  self.color)
                canvas.create_oval(self.x1-15, self.y0+5, self.x1-5, self.y0+20, fill = "white")
                canvas.create_oval(self.x1-11, self.y0+12, self.x1-8, self.y0+14, fill = "black")
    