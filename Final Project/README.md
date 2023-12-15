# PolyPi - Learn What You See: An Interactive, Multilingual Journey Through Object Recognition
#### Collaborators: Chanan Suksangium (cs2475), Stanley Walker (sv523), Thomas Wallace (tw526)

<img width="961" alt="Screen Shot 2566-12-10 at 22 40 16" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/8d123267-6548-4e06-b810-6f52884d4317">

## Overview

PolyPi is a language learning interactive device that aims to help users learn foreign language of choice. Users can begin learning by looking at objects through the lens of PolyPi, and PolyPi will handle the rest through object detection and translation. To set the language of PolyPi, users simply say the language out loud. At launch, the supported languages are English, Spanish and French.

## Initial Project Plan

<img width="929" alt="Screen Shot 2566-12-13 at 14 38 38" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/30ce7aac-e852-4387-9547-cea7ca9cdb41">

## Setup

To run PolyPi, you will need:

- [RaspberryPi 4 x 1](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
- [Raspberry Pi High Quality Camera x 1](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/)
- [Pimoroni HyperPixel 4.0 Square Hi-Res Display x 1](https://www.pishop.us/product/hyperpixel-4-0-square-hi-res-display-for-raspberry-pi-non-touch/)
- [Waveshare Industrial Zoom Lens (C-Mount)](https://www.waveshare.com/8-50mm-zoom-lens-for-pi.htm)
- [SunFounder USB Microphone](https://www.sunfounder.com/products/mini-usb-microphone)

After cloning the repository

1. Run setup.sh to install requirements & download object detection model
2. Run detect.py to begin running PolyPi

## Design

PolyPi is shaped like a camera to be a tool that is intuitive to all users. The product uses a Raspberry Pi 4 that is fitted with a Raspberry Pi High-Quality Camera, Pimoroni HyperPixel 4.0 Square Hi-Res Display, Waveshare Industrial Zoom Lens (C-Mount), and a SoundFounder USB microphone.

### Sketch:

<img width="500" height="400" alt="Ideation 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/062de37a-858a-4bef-aed3-3654879c98f7">
<img width="500" height="400" alt="Ideation 2" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/5e25a618-a7e6-4e36-9484-2c98f36d1228">

Taking inspiration from Polaroid 300 & the side grips on DSLR's:

<img width="500" height="500" alt="Ideation 2" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/c3b17269-c0cc-4bea-8e4c-8ffbafd3631d">
<img width="500" height="250" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/397a1246-4cd3-4dce-9d8d-f6c3a91f57a9">

### Render (using Fusion360):

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fa131970-cc51-48db-b01a-ea9979f56265

[link to render](https://a360.co/41nqTCc)
## Implementation & Process

After the initial ideation & planning, the process of creating the PolyPi can be divided into 2 parts: the software and the hardware

### Software
The software development of PolyPi was more tedious than we initially anticipated as there were a lot of unseen complications throughout the entire process. The first iteration of the software was done with a webcam & VNC Viewer. We had a working OpenCV + MediaPipe object detection, but adding translation made the product unusable as it took too much computing power. After exploring countless different object detection models & translation methods, we found that loading an English-to-foreign language dictionary mapping performed the best. 

This was the first time we got it working

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/d4481fbb-4f5b-4ab9-a42a-8db2589202ce

This was our last version

https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/a09c330a-e762-46b7-96fe-407b64c2d0cb




After obtaining the hardware for the final product (Pi Camera & Hyperpixel 4), we learned that there were a lot incompatibilities such as:
- The Pi High-Quality Camera cannot be used with OpenCV, so we needed to do object detection with PiCamera2
- The Hyperpixel Screen does not work out of the box and we had to disable various things
- The Hyperpixel Screen does not work with the Pi Camera and requires settings to be overridden (such as the screen orientation)
- The Hyperpixel Screen uses every single GPIO port & requires i2c & SPI disabled, so the shim cannot be added

In the final iteration of the software is composed of 3 components:


Camera:
- [PiCam2](https://github.com/raspberrypi/picamera2)

  
Object Detection:
- [Tensorflow Lite](https://toptechboy.com/raspberry-pi-lesson-63-object-detection-on-raspberry-pi-using-tensorflow-lite/)
- efficientdet_lite0.tflite model

  
Voice Recognition:
- [Vosk](https://github.com/alphacep/vosk-api)
- KaldiRecognizer

### Hardware & Product Design

For product design, rendering, and 3D printing we used Fusion360

#### Iteration 1:

In the product's first iteration, we brainstormed that the interactability of PolyPi should be universally operable, so we designed & 3D printed a compact camera housing for the Raspberry Pi, camera, and the screen as most users are familiar with traditional cameras. The mount fits the components well, but as a product design overall the ergonomics could be improved given the size and weight.

<img width="330" height="440" alt="Description of image 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/599eb0c3-005e-47e6-bc8d-4474a37cbf16">
<img width="330" height="440" alt="Description of image 2" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/7bb64ff9-6390-433c-b793-5a3e602e3fa0">
<img width="330" height="440" alt="Description of image 3" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/ce72d95a-9d12-4acd-ab8d-dd4e036176d1">
<img width="330" height="440" alt="Description of image 4" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/efdeb54d-2b60-4aca-8f25-30e27e5073e6">
<img width="330" height="440" alt="Description of image 5" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/9550fa78-ea3a-4015-a4c9-ada6c320012d">

#### Iteration 2:

In the second iteration, we focused on improving the body of the camera & designed a new body that encased the compact 1st iteration of PolyPi and did an initial product test by assembling and interacting with the product, taking notes of the measurements and styling that needed changing.



<img width="330" height="440" alt="Description of image 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/11597920/3ca0fd88-9e4a-41e5-b373-4ed73b01182f">
<img width="330" height="440" alt="Description of image 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/85c14452-e20a-45f1-95d9-e1823b02842c">
<img width="330" height="440" alt="Description of image 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/927ed2e2-210b-47dd-9df2-911cfc972d6c">


#### Iteration 3 (Final):

In the third (final) iteration of the hardware & product design, we kept the previous designs and did incremental refinements for the demo, which included:

- Reprinting the case black for aesthetic purposes
- Adding grooves and curves to improve the ergonomics
- Adding rounded edges for the screen to better integrate the screen into the camera body
- Modifying and cutting open the case for ports & cables accessibility

[link to render](https://a360.co/41nqTCc)

<img alt="Description of image 1" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/1bf91102-9e26-4d7e-a66d-9d02f5a16544">
<img width="330" height="440" alt="Description of image 2" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/f04f1c2b-037d-4a68-80ea-8fd1caa11c7e">
<img width="330" height="440" alt="Description of image 3" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/06cc4847-e008-4da7-adf3-472f5a6bd311">
<img width="330" height="440" alt="Description of image 4" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/f3471ebf-f8bc-4e44-ba78-ec53eef63239">
<img width="330" height="440" alt="Description of image 5" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/8dd1a7c6-897a-4e50-b1d9-de4865e30fd3">
<img width="330" height="440" alt="Description of image 6" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fe0d29dc-d96f-4aec-84aa-80785447b99b">



## Demo Video

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/da9cb036-f6ce-4999-9074-d6f085b77f3b

## Future Iterations

If we were to take this project forward we would love to do a few things more:

1. Make it fully portable: For this, we would need to integrate with an easy-to-charge battery, that way you could take Polypi for a trip overseas!
2. Make it orientation aware: One of the issues we had was the fact that the screen and camera weren't the same side up. We could integrate a gyroscope, that could talk to the screen and automatically rotate it, just like your phone works when you rotate it to landscape mode.
3. Make it more compact. We would like to play around with more camera lenses, the one we used was on the heavy side, and a smaller lens might do the trick.
4. Make it a global communication device. Right now we support English, Spanish and French, but there are more languages and it would be amazing to support more of them!
5. Make it understand more items. Because of the memory and offline nature of Polypi, we had to scale down on how many items we could translate, a newer Raspberry Pi with more power (Raspberry Pi 5) and also an SD card with more memory could help us reach this goal.

## Contributions
- **Ideation** - Chanan, Stanley, Thomas
- **Product Design** - Stanley, Thomas
- **Software** - Chanan
- **Hardware** - Stanley, Thomas
- **Testing** - Chanan, Stanley, Thomas
- **Video & Demo Production** - Chanan, Stanley, Thomas


<img width="1035" alt="Screen Shot 2566-12-13 at 15 17 31" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/5ddfe18f-be10-423b-8fdb-3a59f13585ff">

