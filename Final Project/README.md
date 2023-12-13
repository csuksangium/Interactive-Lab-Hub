# PolyPi - Learn What You See: An Interactive, Multilingual Journey Through Object Recognition
#### Collaborators: Chanan Suksangium (cs2475), Stanley Walker (sv523), Thomas Wallace (tw526)

<img width="961" alt="Screen Shot 2566-12-10 at 22 40 16" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/8d123267-6548-4e06-b810-6f52884d4317">

## Overview

PolyPi is a language learning interactive device that aims to help users learn foreign language of choice. Users can begin learning by looking at objects through the lens of PolyPi, and PolyPi will handle the rest through object detection and translation. To set the language of PolyPi, users simply say the language out loud. At launch, the supported languages are English, Spanish and French.

## Initial Project Plan

## Setup

To run PolyPi, you will need:

- RaspberryPi 4 x 1
- Raspberry Pi High Quality Camera x 1
- Pimoroni HyperPixel 4.0 Square Hi-Res Display x 1
- C-Mount Lens
- USB Microphone

After cloning the repository

1. Run setup.sh to install requirements & download object detection model
2. Run detect.py

## Design

PolyPi is shaped like a camera to be a tool that is intuitive to all users. The product uses a Raspberry Pi 4 that is fitted with a Raspberry Pi High Quality Camera, Pimoroni HyperPixel 4.0 Square Hi-Res Display, Waveshare Industrial Zoom Lens (C-Mount), and a USB microphone.

write about design software used here & show iterations

## Implementation & Process

After the initial ideation & planning, the process in creating the PolyPi can be divided into 2 parts: the software and the hardware

### Software
The software development of PolyPi was more tedious than we initially anticipated as there were a lot of unseen complications throughout the entire process. The first iteration of the software was done with a webcam & VNC Viewer. We had a working OpenCV + MediaPipe object detection, but adding translation made the product unusable as it took too much computing power. After exploring countless different object detection models & translation methods, we found that loading a English to foreign language dictionary mapping performed the best. 

After obtaining the hardwares for the final product (Pi Camera & Hyperpixel 4), we learned that there was a lot incompatibilities such as:
- The Pi High Quality Camera cannot be used with OpenCV, so we needed to do object detection with PiCamera2
- The Hyperpixel Screen does not work out of the box and we had to disable various things
- The Hyperpixel Screen does not work with the Pi Camera and required settings to be overridden
- The Hyperpixel Screen uses every single GPIO port & requires i2c & SPI disabled, so the shim cannot be added

In the final iteration of the software is composed of 3 components:


Camera:
- PiCam2

  
Object Detection:
- Tensorflow Lite
- efficientdet_lite0.tflite model

  
Voice Recognition:
- Vosk
- KaldiRecognizer

### Hardware

## Demo Video

https://youtube.com/shorts/uEAft7H1vXQ?si=N3X87cuG9Mz5X2Iq

## Contributions
- **Ideation** - Chanan, Stanley, Thomas
- **Product Design** - Stanley, Thomas
- **Software** - Chanan
- **Hardware** - Stanley, Thomas
- **Testing** - Chanan, Stanley, Thomas
- **Video & Demo Production** - Chanan, Stanley, Thomas
