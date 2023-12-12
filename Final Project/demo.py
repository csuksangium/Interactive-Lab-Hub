import cv2
import time
from picamera2 import Picamera2
 
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

import spacy
import sys
import json
import time
from vosk import Model, KaldiRecognizer
import os
import subprocess
import sounddevice as sd
import queue
 
model='efficientdet_lite0.tflite'
num_threads=4
 
dispW=1280
dispH=720
 
picam2=Picamera2()
picam2.preview_configuration.main.size=(dispW,dispH)
picam2.preview_configuration.main.format='RGB888'
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
 
webCam='/dev/video2'
cam=cv2.VideoCapture(webCam)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
cam.set(cv2.CAP_PROP_FPS, 30)
 
pos=(20,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(255,0,0)
 
fps=0
 
base_options=core.BaseOptions(file_name=model,use_coral=False, num_threads=num_threads)
detection_options=processor.DetectionOptions(max_results=3, score_threshold=.3)
options=vision.ObjectDetectorOptions(base_options=base_options,detection_options=detection_options)
detector=vision.ObjectDetector.create_from_options(options)
tStart=time.time()

q = queue.Queue()
lang_model = Model(lang="en-us")

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

curr_lang = "english"
lang_choice = ["spanish", "english", "french"]
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):

    rec = KaldiRecognizer(lang_model, 16000)
    result = ""
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            resp = json.loads(rec.Result())['text']
            if resp in lang_choice:
                curr_lang = resp
                print("Language select: ", curr_lang)
        ret, im = cam.read()
        im=picam2.capture_array()
        #im=cv2.flip(im,-1)
        imRGB=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        imTensor=vision.TensorImage.create_from_array(imRGB)
        detections=detector.detect(imTensor)
        image=utils.visualize(im, detections, curr_lang)
        cv2.imshow('Camera',im)
        if cv2.waitKey(1)==ord('q'):
            break
    cv2.destroyAllWindows()
