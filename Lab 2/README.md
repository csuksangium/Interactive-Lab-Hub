# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

2. ### Get Kit and Inventory Parts
Prior to the lab session on Thursday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Thursday.




## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment (named venv) by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@raspberrypi:~ $ python -m venv venv
pi@raspberrypi:~ $ source venv/bin/activate
(venv) pi@raspberrypi:~ $ 

```
### Setup Personal Access Tokens on GitHub
Set your git name and email so that commits appear under your name.
```
git config --global user.name "Your Name"
git config --global user.email "yourNetID@cornell.edu"
```

The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock


## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have already done this in the prep)

From your kit take out the display and the [Raspberry Pi 4](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

To show you the IP and Mac address of the Pi to allow connecting remotely we created a service that launches a python script that runs on boot. For the following steps stop the service by typing ``` sudo systemctl stop mini-screen.service```. Othwerise two scripts will try to use the screen at once. 

We can test it by typing 
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```

#### Displaying Info with Texts
You can look in `screen_boot_script.py` and `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?


## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.


<img width="488" alt="Screen Shot 2566-09-11 at 16 56 28" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/74dbc128-b595-49ac-adc9-c87d7b8e87d0">

Video:

https://youtu.be/2Vp6JvBzGiA

## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

**We strongly discourage and will reject the results of literal digital or analog clock display.**


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

![IMG_0073](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/38afcf30-c4fd-4acc-92c9-251d677cb43b)

![IMG_0074](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/9fa5e7c1-9602-4b01-af90-f3492280731e)

## Part F. 
## Make a short video of your modified barebones PiClock

https://youtu.be/2V-lIRRmTBA

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

Add more useful modes to the PiClock that can be cycled through:
As most people today tell time thru a smartphone, we have unironically come full circle, and replaced pocket watches with smartphones.

I wish to explore different ways to tell time that is superior to a locked smartphone.

Given my passion in traditional watch making, & in theme of timekeeping devices of old, I want to explore 'watch complications' in traditional horology, digitally. Programming these features will help me understand complication logic at a higher level. My constraints will be the screen size & 2 buttons

Mode 1: Stop watch - start, stop, reset with buttons

![IMG_0075](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/27e20ae9-bc08-4ea4-aff3-fa6129638496)

Mode 2: Travel Time - Use buttons to advance/previous the hour to display dual timezone when traveling

![IMG_0076](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/173f2b33-e675-4341-87cd-d286b871518c)

Mode 3: Double split - Stop watch but develop a way to split and begin timing on the second clock (need 3 button for this)

![IMG_0077](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/eb70d024-d555-48ab-8731-7438badda475)

Mode 4: set alarm that chimes at desired time

![IMG_0078](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/49169711-b0d3-444d-8b23-689187bb2658)

Mode 5: Minute repeater - this complication was developed a long time ago pre electicity to allow chimes to tell the time in the dark. I plan to develop a similar feature to check time in the dark/at night to avoid dilating pupils with blue light

![IMG_0079](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/49754171-e053-491f-ae46-a42d5f713ae4)


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

   From the feedbacks I received in class for my initial PiClock concept in Part 1, my classmates praised my logic in the stopwatch, but conversely found the display to be too basic, so for part 2 I needed to do something more creative than a basic display while preserving stopwatch/timing mechanic.

   Therefore I decided to pursue a food timer specifically for timing boiling with a focus on using images to familiarize myself with Pi display.

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

Video:

https://www.youtube.com/watch?v=_MNgzBi6DzM

Reflection:

After filming final video, I found that using white background for Pi screen to be quite difficult to film and capture with an iPhone, so in the future labs I will keep that in mind.

