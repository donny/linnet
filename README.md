# linnet

Linnet is a small Python script for [Scroll Bot](https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit) that displays current time and weather observation data using [OpenWeatherMap](http://openweathermap.org).

### Background

This project is part of [52projects](https://donny.github.io/52projects/) and the new stuff that I learn through this project: [Scroll Bot](https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit) and [OpenWeatherMap](http://openweathermap.org).

### Scroll Bot

I read the first [announcement](https://www.raspberrypi.org/blog/raspberry-pi-zero-w-joins-family/) of [Raspberry Pi Zero W](https://www.raspberrypi.org/products/pi-zero-w/) with much excitement. Imagine a Linux capable computer that has wireless built-in in a super tiny package! On the same day, I ordered a Pi Zero W kit from [Pimoroni](https://shop.pimoroni.com/): the [Scroll Bot](https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit). I spent an evening this week assembling the kit ([photo1](https://github.com/donny/linnet/blob/master/photo1.jpg), [photo2](https://github.com/donny/linnet/blob/master/photo2.jpg), [photo3](https://github.com/donny/linnet/blob/master/photo3.jpg)).

I downloaded [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/) and [copied it](https://learn.adafruit.com/introducing-the-raspberry-pi-zero/making-an-sd-card-using-a-mac) to an SD card using [Etcher](https://etcher.io/). I installed the Scroll pHAT HD [SDK](https://github.com/pimoroni/scroll-phat-hd) and tried the example programs.

### Project

After installing the Scroll pHAT HD [SDK](https://github.com/pimoroni/scroll-phat-hd) and [PyOWM](https://github.com/csparpa/pyowm); and getting the API key from [OpenWeatherMap](http://openweathermap.org). We could run Linnet on the Scroll Bot or we could run it on [boot](https://learn.pimoroni.com/tutorial/sandyj/running-scripts-at-boot). A photo of the Scroll Bot running Linnet in action (and a short [movie](https://raw.githubusercontent.com/donny/linnet/master/movie.m4v)):

 ![Photo](https://raw.githubusercontent.com/donny/linnet/master/scrollbot.png)

### Implementation

Linnet is implemented as a Python script. The code is straight forward and the main body can be found below:

```python
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
```

It alternates every minute between displaying time and the current weather observation for Melbourne, Australia. It scrolls the message text as can be seen in the [movie](https://raw.githubusercontent.com/donny/linnet/master/movie.m4v)).

### Conclusion

...
