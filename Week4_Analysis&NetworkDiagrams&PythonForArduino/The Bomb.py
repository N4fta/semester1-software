import time, sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

#-----------
# Constants
#-----------
BUTTON_PINS = [8,9]
LED_PINS = [4, 5, 6, 7]
BUZZER = 3
POTPIN = 0 # analog pin A0

#------------------------------
# Initialized global variables
#------------------------------
i=60.0      #initial counter value
speed=0.1     #how fast the counter goes down
cycle=0       #cycle counter, used to keep count of cycles and perform certain actions only every X cycles instead of every 0.1seconds
LED_state=False  #Red LED state used for the "warning LED"
prevPin=4    #previous pin (used in case of failure)
dCycles=0   #cycles for the success sequence
value=0    #value of the potentiometer
level=0     #level of the success sequence
mistake=[]   #list of buttons counted as input


#-----------
# functions
#-----------
def setup():
    global board
    board = CustomTelemetrix()
    # Put your code here.
    for pin in BUTTON_PINS:
        board.set_pin_mode_digital_input_pullup(pin)
    for pin in LED_PINS:
        board.set_pin_mode_digital_output(pin)
    board.set_pin_mode_digital_output(BUZZER)
    board.set_pin_mode_analog_input(POTPIN, callback=PotChanged, differential=10)
    # Note: The differential defines the distance between the previous 
    #       and current value. If the difference is greater dan differential 
    #       then PotChange() is called. This solution reduces noise.
    time.sleep(0.3)

def PotChanged(data):
    global value
    value = data[2]

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
#copied from the arduino map function definiton 

def deactivation_sequence():
    global dCycles, level,mistake
    dCycles+=1
    if dCycles<level*15:            #time allocated per level (eg. level*15 is equal to 1.5seconds per level)  
        return dCycles,level
    elif dCycles==level*15:          #time allocated per level
        dCycles,level=0,0
        mistake=[]
        for pin in LED_PINS:
            board.digital_write(pin, 0)
    
def success(cycle):
    global speed
    speed=0
    while True:
        #LEDs
        if cycle==5:
            for pin in LED_PINS:
                board.digital_write(pin, 1)
        elif cycle>=10:
            for pin in LED_PINS:
                board.digital_write(pin, 0)
        
        #display
        if cycle>=10:
            board.displayShow("----")
            cycle=0                    
        elif cycle==5:
            board.displayShow(i)
            cycle+=1
        else:
            cycle+=1
        time.sleep(0.1)



def loop():
    global i, cycle,LED_state,prevPin,dCycles,speed,level,mistake

    #buttons read
    button1 = board.digital_read(8)[0]
    button2 = board.digital_read(9)[0]

    #mistake checker
    # if len(mistake)!=0:
    #     for x in mistake:
    #         print(x)
    #         if x==0:
    #             speed+=0.1
    #     print(speed)

    #deactivation sequence
    if button1==0 or level>=1:
        board.digital_write(LED_PINS[1], 1)
        if button2==0 or level>=2:
            board.digital_write(LED_PINS[2], 1)
            if button1==0 or level>=3:
                board.digital_write(LED_PINS[3], 1)
                if value>=1000:
                    success(cycle)
                else:
                    level=3
                    mistake=[button1,button2]
                    deactivation_sequence()
            else:
                level=2
                mistake=[button2]
                deactivation_sequence()
        else:
            level=1
            mistake=[button1]
            deactivation_sequence()
        


    #warning light
    if cycle>=3 and i<10 or cycle>=5 and i<30 or cycle>10 and i<60:
        cycle=0
        if LED_state==False:
            board.digital_write(LED_PINS[0], 1)
            board.digital_write(BUZZER, 1)#buzzer
            LED_state=True
        elif LED_state==True:
            board.digital_write(LED_PINS[0], 0)
            board.digital_write(BUZZER, 0)#buzzer
            LED_state=False
    cycle+=1

    #level
    if i>0:
        board.displayShow(i)
        i-=speed
    else:
        while True:
            for pin in LED_PINS:
                #display
                if cycle>=10:
                    board.displayShow("----")
                    cycle=0                    
                elif cycle==5:
                    board.displayShow("0.000")
                    cycle+=1
                else:
                    cycle+=1
                #buzzer
                board.digital_write(BUZZER, 1)#map_range(cycle,0,10,0,255))

                #variables
                board.digital_write(prevPin, 0)
                board.digital_write(pin, 1)
                time.sleep(0.1)
                prevPin = pin

    
    time.sleep(0.1) # Give Firmata some time to handle the protocol.

# Put your functions here.

#--------------
# main program
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
