# PolyPi - Learn What You See: An Interactive, Multilingual Journey Through Object Recognition
#### Collaborators: Chanan Suksangium (cs2475), Stanley Walker (sv523), Thomas Wallace (tw526)

<img width="961" alt="Screen Shot 2566-12-10 at 22 40 16" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/8d123267-6548-4e06-b810-6f52884d4317">

## Overview

PolyPi is a language learning interactive device that aims to help users learn foreign language of choice. Users can begin learning by looking at objects through the lens of PolyPi, and PolyPi will handle the rest through object detection and translation. To set the language of PolyPi, users simply say the language out loud. At launch, the supported languages are English, Spanish and French.

## Initial Project Plan

<img width="929" alt="Screen Shot 2566-12-13 at 14 38 38" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/30ce7aac-e852-4387-9547-cea7ca9cdb41">

## Setup

To run PolyPi, you will need:

- RaspberryPi 4 x 1
- Raspberry Pi High Quality Camera x 1
- Pimoroni HyperPixel 4.0 Square Hi-Res Display x 1
- C-Mount Lens
- USB Microphone

After cloning the repository

1. Run setup.sh to install requirements & download object detection model
2. Run detect.py to begin running PolyPi

## Design

PolyPi is shaped like a camera to be a tool that is intuitive to all users. The product uses a Raspberry Pi 4 that is fitted with a Raspberry Pi High Quality Camera, Pimoroni HyperPixel 4.0 Square Hi-Res Display, Waveshare Industrial Zoom Lens (C-Mount), and a USB microphone.

### Sketch:

![ed03786d-7f4c-40c5-a407-d5d26c07f0df](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/46ea23ac-47fc-4eec-8605-bbc0fc8ca082)

![edc312aa-58ce-477e-b79b-d3edb6604776](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/feafd43e-7a8d-4f9f-981a-aa0c1bfe9860)

### Render (using Fusion360):

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fa131970-cc51-48db-b01a-ea9979f56265

## Implementation & Process

After the initial ideation & planning, the process in creating the PolyPi can be divided into 2 parts: the software and the hardware

### Software
The software development of PolyPi was more tedious than we initially anticipated as there were a lot of unseen complications throughout the entire process. The first iteration of the software was done with a webcam & VNC Viewer. We had a working OpenCV + MediaPipe object detection, but adding translation made the product unusable as it took too much computing power. After exploring countless different object detection models & translation methods, we found that loading a English to foreign language dictionary mapping performed the best. 

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/d4481fbb-4f5b-4ab9-a42a-8db2589202ce

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

#### Iteration 1:

![861f4ced-0950-4b87-a73a-1a03955acd6c](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/599eb0c3-005e-47e6-bc8d-4474a37cbf16)

![16e2d2bf-f9cd-400c-b8b2-26419849f24d](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/7bb64ff9-6390-433c-b793-5a3e602e3fa0)

![9d295b39-0059-4902-84c0-829a86f75050](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/ce72d95a-9d12-4acd-ab8d-dd4e036176d1)

![5f820eda-c921-4461-8e79-668195f03486](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/efdeb54d-2b60-4aca-8f25-30e27e5073e6)

![a79c9cf2-11cc-4168-bcfe-e13ad38aafd1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/9550fa78-ea3a-4015-a4c9-ada6c320012d)

#### Iteration 2:

![7b73c3e7-7ceb-403f-947a-4c3b6b8d5308](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/85c14452-e20a-45f1-95d9-e1823b02842c)

![2730edd1-90e2-4568-a3cc-0635391713ab](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/927ed2e2-210b-47dd-9df2-911cfc972d6c)

#### Iteration 3 (Final):

![178a4177-0bb6-44be-b2a7-cd71bd2494e2](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/1bf91102-9e26-4d7e-a66d-9d02f5a16544)

![72623308-0f17-4aff-bacb-e3dc6a25c9f1](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/f04f1c2b-037d-4a68-80ea-8fd1caa11c7e)

![2075c93f-ef86-4b06-b3b1-8fea667a0718](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/06cc4847-e008-4da7-adf3-472f5a6bd311)

![a52faec6-963e-4613-bdd4-74b84ad907ed](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/f3471ebf-f8bc-4e44-ba78-ec53eef63239)

![07d2b5ce-3ef2-455b-9451-bf42a06dd5da](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/8dd1a7c6-897a-4e50-b1d9-de4865e30fd3)

![7fd47dc5-0fbe-40b2-9f8f-3c48acb955a9](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fe0d29dc-d96f-4aec-84aa-80785447b99b)


## Demo Video

https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/da9cb036-f6ce-4999-9074-d6f085b77f3b

## Contributions
- **Ideation** - Chanan, Stanley, Thomas
- **Product Design** - Stanley, Thomas
- **Software** - Chanan
- **Hardware** - Stanley, Thomas
- **Testing** - Chanan, Stanley, Thomas
- **Video & Demo Production** - Chanan, Stanley, Thomas


<img width="1035" alt="Screen Shot 2566-12-13 at 15 17 31" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/5ddfe18f-be10-423b-8fdb-3a59f13585ff">

