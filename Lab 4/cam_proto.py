# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from __future__ import print_function
import qwiic_proximity
import time
import sys

import cv2
import pyaudio
import wave
import pygame

def test_camera(oProx):
    cap = cv2.VideoCapture(0)  # Change 0 to 1 or 2 if your camera does not show up.
    while True:
        proxValue = oProx.get_proximity()
        print(proxValue)
        ret, frame = cap.read()
        cv2.imshow('Camera Test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if proxValue < 3:
            break
    cap.release()
    cv2.destroyAllWindows()

def test_microphone():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []
    print("Recording...")
    for i in range(0, int(44100 / 1024 * 2)):
        data = stream.read(1024)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open('test.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("Saved as test.wav")

def test_speaker():
    p = pyaudio.PyAudio()

    # List all audio output devices
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
                print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    device_index = int(input("Enter the Output Device id to use: "))  # Enter the id of your USB audio device

    wf = wave.open('test.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    output_device_index=device_index)  # specify your device index here

    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()
    p.terminate()

print("\nSparkFun Proximity Sensor VCN4040 Example 1\n")
oProx = qwiic_proximity.QwiicProximity()

if oProx.connected == False:
    print("The Qwiic Proximity device isn't connected to the system. Please check your connection", file=sys.stderr)

oProx.begin()


while True:
    curr_prox = oProx.get_proximity()
    print(curr_prox)
    if curr_prox >= 3:
        test_camera(oProx)
        # test_microphone()
        # test_speaker()
    time.sleep(0.2)


