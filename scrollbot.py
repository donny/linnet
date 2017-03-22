import scrollphathd as sphd
import time
import math
import pyowm

OWM_KEY=''
BRIGHTNESS=0.1

owm = pyowm.OWM(OWM_KEY)

def getWeather():
    observation = owm.weather_at_place('Melbourne,AU')
    weather = observation.get_weather()
    status = weather.get_detailed_status().capitalize()
    temp = weather.get_temperature(unit='celsius')
    msg = "{0}. {1}-{2}   ".format(status, temp['temp_min'], temp['temp_max'])
    return msg

def getClock():
    return time.strftime("%H:%M   ")

sphd.flip(True, True)

display_clock = True
sphd.write_string(getClock(), brightness=BRIGHTNESS)

while True:
    if int(time.time()) % 60 == 0:
        display_clock = not display_clock
        sphd.clear()
        sphd.show()
        time.sleep(1)

        if display_clock:
            sphd.write_string(getClock(), brightness=BRIGHTNESS)
        else:
            sphd.write_string(getWeather(), brightness=BRIGHTNESS)

    sphd.scroll(1)
    sphd.show()
    time.sleep(0.1)

