import RPi.GPIO as gpio
import time
begin = time.time()
curr = 0
period = 1
tick = 0
blockSizeMins = 5
diffSum = 0
avgSum = 0
block = 0
timeStampsMin = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
timeStampsHour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
timeStampsDay = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

hallSensor = 2
led = 3

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup(hallSensor,gpio.IN)
gpio.setup(led, gpio.OUT)

l1Block = 0;
l2Block = 0;
l3Block = 0;

l1start = 0
l2start = 0
l3start = 0

ticksInSecond = 1 / period
ticksInMinute = 60 * ticksInSecond
ticksInHour = 60 * ticksInMinute
ticksInDay = 24 * ticksInHour

secsInMin = 60
secsInHour = 60 * secsInMin
secsInDay = secsInHour * 24

diffDay = 0
diffHour = 0
diffMin = 0

settings = open(".conf")
period = float(settings.readline())

mins = float(settings.readline())
hours = float(settings.readline())
days = float(settings.readline())
debug = int(settings.readline())


ticksInSecond = 1 / period
ticksInMinute = 60 * ticksInMinute
ticksInHour = 60 * ticksInMinute
ticksInDay = 24 * ticksInHour


fileName = "public/data"
csv = open(fileName+".txt","w+")
csv.write("Date,Tick,"+str(mins)+" Min(s),"+str(hours)+" Hour(s),"+st$

i,j,k = 0,0,0

while(True):
    while(gpio.input(hallSensor) == 1):
       t = 0
        time.sleep(0.01)
    
    time.sleep(period / 4)
    gpio.output(led,1)
    time.sleep(0.100)
    gpio.output(led,0)
    tick += 1
    if(debug == 1):
        print("Tick!")
        print("time (System): "+time.ctime(time.time()))
        print("time (Pendulum): "+time.ctime((tick * period) + begin))

    
    
    timeStamp = time.time();
  
    blockTypeTicks = ticksInMinute
    blockTypeSecs = secsInMin
    blockSize = mins
    if(tick % (blockTypeTicks * blockSize) == 0):
        timeStampsMin[i] = timeStamp
        l = len(timeStampsMin)
        if(l > 1):
            diffMin = abs(timeStampsMin[(i) % l] - timeStampsMin[(i -$
            print(str(blockSize)+" Minute Diff: %2.3fs "%(diffMin))
            i += 1
            i %= l
            csv.write(time.ctime(time.time())+",")
            csv.write(str(tick)+",")
            if((diffMin == 0) or (diffMin > 999)):
                 csv.write("-,")
            else:
                 csv.write("%3.3f,"%diffMin)
            if((diffHour == 0) or (diffHour > 999)):
                 csv.write("-,")
            else:
                 csv.write("%3.3f,"%diffHour)
            if((diffDay == 0) or (diffDay > 999)):
                 csv.write("-,")
            else:
                 csv.write("%3.3f,"%diffDay)
            csv.write("\n")

        csv.close()
        csv = open(fileName+".txt","a")

    blockTypeTicks = ticksInHour
    blockTypeSecs = secsInHour
    blockSize = hours
    if(tick % (blockTypeTicks * blockSize) == 0):
    timeStampsHour[j] = timeStamp
        l = len(timeStampsHour)
        if(l > 1):
            diffHour = abs(timeStampsMin[(i) % l] - timeStampsMin[(i $
            print(str(blockSize)+" Hour Diff: %2.3fs "%(diffHour))
            j += 1
            j %= l

    blockTypeTicks = ticksInDay
    blockTypeSecs = secsInDay
    blockSize = days
    if(tick % (blockTypeTicks * blockSize) == 0):
        timeStampsDay[k] = timeStamp
        l = len(timeStampsDay)
        if(l > 1):
            diffDay = abs(timeStampsDay[(i) % l] - timeStampsDay[(i -$
            print(str(blockSize)+" Day Diff: %2.3fs "%(diffDay))
            k += 1
            k %= l










