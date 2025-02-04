# Ph-UI!!!


For lab this week, we focus both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 


### Start brainstorming ideas by reading: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

* New hardware for your kit will be handed out. Update your parts list. 


(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Camera Test](#part-f)

G) [Record the interaction](#part-g)


## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
 
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). Install the latest requirements from your working virtual environment:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip install -r requirements.txt

```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 
 
<img src="https://cdn-shop.adafruit.com/970x728/3595-06.jpg" width=200>
 

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder (optional)

> **_NOTE:_**  Not in the kit yet - skip this.

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separate breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">

   
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick (optional)


A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor


Earlier we have asked you to play with the proximity sensor, which is able to sense objects within a short distance. Here, we offer [Sparkfun Proximity Sensor Breakout](https://www.sparkfun.com/products/15177), With the ability to detect objects up to 20cm away.

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/9/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-01.jpg" height="200" />

</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python qwiic_distance.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Proximity_Py) to learn more about the sensor and see other examples

### Part C
### Physical considerations for sensing


Usually, sensors need to be positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.


**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

For Lab 3, the initial idea I intend to explore a prototype of camera that is activated by proximity sensor, which will stream the footage wirelessly to a laptop. Below are 5 sketches of different iterations of the prototype I intend to create.

#### Sketch 1

Sketch 1 is the first iteration that came into my mind, which is inspired by smart home camera as an IoT device. For versatility, I opted to have an OLED screen in case information should be displayed such as 'Recording'. However, if this product is mounted to the door, then there is no need for the Pi to be mounted directly on the cardboard, so this design did not include Pi, which will be connected via wires.

![IMG_0096](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/c50dbe5a-ca9d-4a35-bc8a-691694df983b)

#### Sketch 2

Sketch 2 is similar to sketch 1 as the prototype will contain a camera, screen, and proximity sensor. However, the Pi will be mounted on the back. The idea behind this concept is a home-use camera, which is why I designed for the legs/stands & the camera is mounted vertically to increase view angle. A use case I had in mind when sketching this idea is a camera by the pet feeder that activates to show that your pet is feeding.

![IMG_0097](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/5c5dc2a5-fa8f-4704-9e23-0126d822dc9a)

#### Sketch 3

Sketch 3 is a compact version of sketch 1 where the cardboard enclosing the camera and proximity will be as small as possible. This will also mean that the Pi will not be mounted nor contained in the cardboard prototype, instead connected by wires to ensure a small footprint. The idea behind this prototype is a discreet camera (ie security camera) within home use hence the emphasis on size. The screen is also not used here.

![IMG_0098](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/90eae052-baf0-4725-9bb6-12144d4d303a)

#### Sketch 4

Sketch 4 is a direct iteration from sketch 1, but the Pi will be mounted on the product. I opted for a ledge to hold the Pi in place, but also to make it easily removable for repairability & update. This allows the Pi to slide in and out without having to detach the securely mounted camera & sensor. The rear screen can also be used to display any information.

![IMG_0099](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/3071d4fe-46c3-447a-8a43-3b503bac79cf)

#### Sketch 5

Sketch 5 takes on the design where the Pi will be enclosed in the same cardboard body as the camera and the proximity sensor. The body will be securely sealed and it will have a latch/lever. The inspiration behind this sketch is an outdoor version of camera, so the Pi will have to be enclosed to withstand environmental factors such as rain, wind & dust. 

![IMG_0100](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/05366474-5cc7-4541-9b37-9c34b701a37c)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Some of the questions raised by the sketches is how small can I make my prototype for its use cases to be viable & if it is ok for the Pi to be attached or can be Pi exist outside. 

I need to physically prototype to see the footprint in real life as I suspect the constraint (size of camera) will disallow it to be a discrete camera. I also need to physically test to see if the Pi will be difficult to operate if contained in the prototype? If it is ok to be outside entirely to keep it small?

**\*\*\*Pick one of these designs to prototype.\*\*\***

I will attempt to prototype sketch 3.

### Part D
### Physical considerations for displaying information and housing parts



Here is a Pi with a paper faceplate on it to turn it into a display interface:


<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>


Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibly mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />

</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

#### Sketch 1:

![IMG_03FD1C4C5948-1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/054137a1-9d81-47e2-88cd-e1dd3a29051d)

#### Sketch 2:

![IMG_18801809E645-1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/4c252e99-fd60-41dd-af8b-2936d4ebdd6c)

#### Sketch 3:

![IMG_DA0B4530CA0D-1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/3b6c442c-c270-40e1-bece-cacbd2de7692)

#### Sketch 4:

![IMG_35C92E9BBB0D-1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fc94a91e-b4af-474e-a016-96713d10f5e3)

#### Sketch 5:

![IMG_660475F61827-1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fcfd1e90-b992-459a-a535-0ac0556193ab)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Some of the things that these sketches raise as questions would be if the mounting of the camera position, sensors, and Pi/screen would be feasible in a prototype of such dimension because securing the sensors next to the camera since it will require space to hold the sensor and camera in place.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I will initially prototype with sketch #1 to get the basic functionality working and continue to add screen if it improves the product.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The design is aimed to be as compact as possible as the footprint will only need to contain the camera & sensor. I intend to initially control the device from the outside as the cable with the camera is quite bulky and would take up a lot of space. I also aim to put the sensor in front with the camera so it will be activated when subject stands in front. Other sides of the product is unused.

Build a cardboard prototype of your design.


**\*\*\*Document your rough prototype.\*\*\***

<img width="579" alt="Screen Shot 2566-10-10 at 23 43 08" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/7c62615f-4c29-4435-91a9-5ec034b1c345">

<img width="585" alt="Screen Shot 2566-10-10 at 23 43 18" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/91bfbb6e-f03d-4354-a911-14bca4b3f0a8">

<img width="577" alt="Screen Shot 2566-10-10 at 23 43 28" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/631b5631-b8be-4dac-86fd-200f035cd6e8">

<img width="587" alt="Screen Shot 2566-10-10 at 23 43 35" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/3e75162f-8631-4b3e-b7bd-082de974ce23">


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

> **_NOTE:_**  Not in the kit yet.

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which is included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.


<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.


Now that you have a basic idea of what a servo motor is, look into the script `servo_test.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degrees. Try running the servo example code now and see what happens:


```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!


### Part F (Optional)
### Camera
You can use the inputs and outputs from the video camera in the kit. 
We provide another script called camera_test.py to test the USB camera on raspberry pi. 
It uses qt to render a video to the screen, so it is necessary to connect a screen or to connect via VNC to run this script. 

First install some more dependencies into your virtual environment. OpenCV should already be installed on the Pi for the super user. 

```
sudo apt-get install portaudio19-dev python-all-dev
pip install opencv-python pyaudio pygame
```

Once executed the script will render the camera output, press 'q' to stop video and record a sound through the microphone which will be played back by specificing the audio output. 

---
The video is rendered locally on the pi. For wizarding interactions and prototyping it can be necessary to stream the video to another device such as your laptop. A wizard, observing the user and acting as a computer vision algorithm, can then trigger interactions remotley, such as we did in the tinkerbelle lab.

The following resources are good starts on how to stream video: 
* [OpenCV – Stream video to web browser/HTML page](https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
* [Live video streaming over network with OpenCV and ImageZMQ](https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
### Part G

### Record

#### "Looks Like": shows how the device should look, feel, sit, weigh, etc.

The prototype from front view shows a cut out for the proximity sensor to operate and a cut out for the camera. I opted for a flap to protect the camera lens when not in use. The prototype sits flat on the base.

<img width="590" alt="Screen Shot 2566-10-23 at 22 57 13" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/f5b20a67-c446-4a10-ad65-76295a2bfff5">

The prototype from top view with the removable top to allow the camera and proximity sensor to be removed. The footprint is very small and no room for the wire nor to Pi to fit inside therefore it weighs around the same as the camera.

<img width="585" alt="Screen Shot 2566-10-23 at 22 57 34" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/58424ebd-8a99-4ab5-b9d2-3eaa17334320">

The cutout to allow the wires connecting the camera to the Pi and the proximity sensor externally

<img width="591" alt="Screen Shot 2566-10-23 at 22 57 22" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/1626e4b6-de7a-4db6-a963-9a2b3e6bc3e7">

Top view of the camera with a Pi for scale to understand the size

<img width="586" alt="Screen Shot 2566-10-23 at 22 57 04" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/793ffd27-b281-4595-8a5f-da7c85a05669">

#### "Works Like": shows what the device can do.

The diagram below demonstrates how the device can be activated and interacted with. After the chain of events leading to the screen step, the potential is limitless as you can persist & log the footage, apply computer vision, etc.

![IMG_0112](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/64fa7b50-115c-4fc2-aa58-4882d856f335)

#### "Acts Like": shows how a person would interact with the device.

https://youtu.be/yeyS0QwVukE

