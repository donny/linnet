import scrollphathd as sphd
import time
import math
import pyowm

OWM_KEY=''

owm = pyowm.OWM(OWM_KEY)
observation = owm.weather_at_place('Melbourne,AU')
weather = observation.get_weather()

status = weather.get_detailed_status()
temp = weather.get_temperature(unit='celsius')
 
message = "{0} {1}".format(
print(status)

#sphd.clear()
#sphd.show()

#for x in range(17):
#    sphd.clear()
#    for y in range(7):
#        sphd.set_pixel(x, y, 0.25)
#    sphd.show()
#    time.sleep(1/17.0)


#sphd.flip(True, True)
#txt = "If it's a good idea, go ahead and do it. It is much easier to apologize than it is to get permission. - Grace Hopper"
#sphd.write_string(txt)
#while True:
#    sphd.show()
#    sphd.scroll(1)
#    time.sleep(0.05)


#while True:
#    t = time.time() * 10
#    for x in range(17):
#        for y in range(7):
#            b = math.sin(x + y + t) + math.cos(x + y + t)
#            b = (b + 2) / 4
#            sphd.set_pixel(x, y, b)
#    sphd.show()
