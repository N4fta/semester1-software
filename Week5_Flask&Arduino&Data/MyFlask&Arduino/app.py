from flask import Flask
from flask import render_template
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

from datetime import datetime
import random, time, sys


# -----------
# Setup (runs once)
# -----------
app = Flask(__name__)
table=[]

# -----------
# Constants and global variables
# -----------
DHTPIN = 12  # digital pin
humidity = 0
temperature = 0

LDRPIN = 2  # analog pin A2
lightLevel = 0

BUTTON1 = 8 
BUTTON2 = 9
level1 = 0
prevLevel1 = 0
level2 = 0
prevLevel2 = 0

display_i = 3
display_v = [0,0,0]
hum = ["h","hum","humidity","water","air"]
light = ["l","light","brightness","bright"]


# -----------
# General Functions
# -----------

def utc_signal(utc):
#returns the signal, an integer and returns UTC 0 if utc is invalid
    try:
        for x in utc:
            utc_string=utc[x]
    except:
        return 0
    sign=[]
    result=True
    #check for signals
    if utc_string.find("-"):
        while True:
            try:
                utc_string.remove("-")
                sign.append("negative")
            except:
                break
    if utc_string.find("+"):
        while True:
            try:
                utc_string.remove("+")
                sign.append("positive")
            except:
                break
    #other checks
    if utc_string.find(":"): #removes ":"
        while True:
            try:
                utc_string.remove(":")
            except:
                break
    if utc_string.find("."): #removes "."
        while True:
            try:
                utc_string.remove(".")
            except:
                break
    
    #check if its integer
    if len(sign)>1:
        result=False
    try:
        utc="".join(utc_string)
        int(utc)
    except:
        result=False
    if result==False:
        utc=0

    #add signal
    if len(sign)==1 and sign[0]=="negative":
        utc=-utc
    return utc
    

    return utc

def current_time(utc):
    utc_signal(utc)

    rightNow = datetime.now()

    x = rightNow.strftime("%H:%M:%S, %A %B %Y")

    return x


# -----------
# Arduino Functions
# -----------
def Measure(data):#Callback function that reads DHT
    global humidity, temperature
    # [report_type, error_value, pin, dht_type, humidity, temperature, timestamp]
    if (data[1] == 0):
        humidity = data[4]
        temperature = data[5]

def LDRChanged(data):#Callback function that reads Light Dependent Resistor(LDR)
    global lightLevel
    lightLevel = data[2]
    # print(data)

def ButtonChanged1(data):#Callback function that reads Button Level
    global level1
    level1 = data[2] # get the level
    # Keep the callback function short and fast.
    # Let loop() do the 'expensive' tasks.

def ButtonChanged2(data):#Callback function that reads Button Level
    global level2
    level2 = data[2] # get the level

def setup():
    global board
    board = CustomTelemetrix()
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
    board.set_pin_mode_analog_input(LDRPIN, callback=LDRChanged, differential=10)
    # Note: The differential defines the distance between the previous
    #       and current value. If the difference is greater dan differential
    #       then LDRChange() is called. This solution reduces noise.
    board.set_pin_mode_digital_input_pullup(BUTTON1, callback = ButtonChanged1)
    board.set_pin_mode_digital_input_pullup(BUTTON2, callback = ButtonChanged2)
    # Note: Getting button level via callback ButtonChanged() is more 
    #       accurate for Firmata. When button is pressed or release,
    #       the ButtonChanged() function is called and this sets the 
    #       level variable.
    time.sleep(0.05)

def loop():
    global lightLevel, temperature, display_v, display_i, humidity, level1, prevLevel1, level2, prevLevel2
    # Only print when level changed
    if (prevLevel1 != level1 and prevLevel2 ==level2):
        if prevLevel1 ==1:
            display_i+=1
            display_i%=3
        prevLevel1 = level1
    elif (prevLevel2 != level2 and prevLevel1 ==level1):
        if prevLevel2 ==1:
            display_i-=1
            display_i%=3
        prevLevel2 = level2
    
    #Load new values
    display_v[0]=temperature
    time.sleep(0.01)
    display_v[1]=humidity
    time.sleep(0.01)
    display_v[2]=lightLevel
    time.sleep(0.01)
    
    if display_i<3:
        board.displayShow(display_v[display_i])
    time.sleep(0.01)  # Give Firmata some time to handle protocol.
    return display_v


# -----------
# Main Program
# -----------
setup()

@app.route('/')
@app.route('/<utc>')
def index_page(utc = None):
    temp=[current_time(utc),temperature,humidity,lightLevel]
    table.insert(0,temp)
    while len(table)>10:   # number of checkpoints saved
        table.pop()
    print(table)
    return render_template('data table.html', data=table)

@app.route('/arduino/')
@app.route('/arduino/<sensor>')   # By adding the name  of a sensor you can choose what is displayed
def arduino_display(sen = "temp", utc= None):  # Default is temperature
    display_v = loop()
    return render_template('sensor display.html', sensor=display_v[0], time = current_time(utc))

@app.route('/arduino/h')   # Humidity
def arduino_display2(utc= None):
    display_v = loop()
    return render_template('sensor display.html', sensor=display_v[1], time = current_time(utc))

@app.route('/arduino/l')   # Light
def arduino_display3(utc= None):
    display_v = loop()
    return render_template('sensor display.html', sensor=display_v[2], time = current_time(utc))

app.run()

print('shutdown')
board.displayShow("----")
board.shutdown()

#--------------
# Arduino Program
#--------------
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt: # Shutdown Firmata on Crtl+C.
        board.displayOff()
        print ('shutdown')
        board.shutdown()
        sys.exit(0)