# Chatterboxes

[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

**Please note:** connect the webcam/speaker/microphone while the pi is *off*. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Setup 

*DO NOT* forget to work on your virtual environment! 

Run the setup script
```chmod u+x setup.sh && sudo ./setup.sh  ```

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the directory is a folder called `speech-scripts` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/speech-scripts $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files `.sh` by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/speech-scripts $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech
```
You can test the commands by running
```
echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? 
Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

---
Bonus:
[Piper](https://github.com/rhasspy/piper) is another fast neural based text to speech package for raspberry pi which can be installed easily through python with:
```
pip install piper-tts
```
and used from the command line. Running the command below the first time will download the model, concurrent runs will be faster. 
```
echo 'Welcome to the world of speech synthesis!' | piper \
  --model en_US-lessac-medium \
  --output_file welcome.wav
```
Check the file that was created by running `aplay welcome.wav`. Many more languages are supported and audio can be streamed dirctly to an audio output, rather than into an file by:

```
echo 'This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | \
  piper --model en_US-lessac-medium --output-raw | \
  aplay -r 22050 -f S16_LE -t raw -
```
  
### Speech to Text

Next setup speech to text. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 
```
pip install vosk
pip install sounddevice
```

Test if vosk works by transcribing text:

```
vosk-transcriber -i recorded_mono.wav -o test.txt
```

You can use vosk with the microphone by running 
```
python test_microphone.py -m en
```

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

#### Video of Shell Script

https://youtube.com/shorts/_woj7_FWhx0

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

#### Idea 1: Cook's Assistant

![IMG_0091](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/ea7c9fbc-3c1d-47c3-b3bd-e376dc11b1b1)

#### Idea 2: Study Buddy

![IMG_0092](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/1424ec23-3cfb-4b12-b175-f3046a041c0a)

Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

2 of my ideas came from what I found would improve my quality of life at Cornell Tech

#### 1: Cook's Assistant
As someone living alone, I find that there is a pain point when cooking alone as my hands would be messy and I need to look at the next instructions. By having Cook's Assistant, I can ask for next steps without getting my hands on my phone & I will be able to pay attention to the cooking without running back and forth.

Sample Interaction #1 (Cooking assistant)

<img width="949" alt="Screen Shot 2566-09-24 at 22 25 45" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/a349fd80-e84d-48d2-a5f0-e99beb97b434">

<img width="1086" alt="Screen Shot 2566-09-24 at 22 26 14" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/ac9ec9e1-b68b-4168-bc25-04a17f46ba4f">

<img width="1353" alt="Screen Shot 2566-09-24 at 22 26 44" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/fa5518e2-5537-4971-9ca5-bad310c68d84">

Sample Interaction #2 (Managing Groceries List)

<img width="790" alt="Screen Shot 2566-09-24 at 22 27 10" src="https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/e156a37e-7e61-44a9-b693-df03ee2a32d4">

#### 2: Study Buddy
I find that I tend to lost focus every now and then when studying alone. The purpose of study buddy is for a monitor to help study, stay focused, and remind you in case it hears distracting content during focus time.

Sample Interaction #1 (Study Hall)

User: “What do I have to study today”      Device: “You have Machine Learning and Data science homework”

User: “I would like to begin studying”     Device: “How long would you like to study for?”

User: “I would like to begin studying”     Device: “When would you like to take breaks”

User: “Every 30 minutes”                   Device: “You may begin studying”

Sample Interaction #2 (Focus Monitor)

*Netflix opening theme*                    Device: “I am hearing noises in the background. Are you staying focused?”

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

#### Video of dialogue:

https://youtu.be/e19DjV-7Z9A

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

The dialogue was different than what I imagined because I only thought about the product for my use case, but I did not take into consideration of how others may approach cooking. For example, when I cook, I am quite specific in the way that I would know what pasta I would cook (ie. Carbonara, Pesto, etc.). However, in the dialogue, my partner asked for 'pasta', which was a case I did not think about, so I needed to improvise. 

I think perhaps my prototype use case is too open-ended to scale to other users as the device will be rather hard-coded and not a Machine Learning IoT device quite yet, so in Lab 3 part II I may reconsider working on a concept that has less possibilities of open-ended conversations & something more streamlined.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

  In my previous design (Cook's Assistant), I found the concept to be too open-ended for a hard-coded project (since I am not using ML). Therefore, I am shifting to pursue a new idea (Snooze Buddy) for Lab 3 Part II. Since the Lab is voice focus, I wanted to explore an idea where voice is the best source of input, so I will make an alarm clock that asks for how long I wish to sleep for with snooze features. I find that this is superior to iphone since sleep schedule can vary and you won't have to change alarm time every night, just tell Snooze Buddy 'I want to sleep for 8 hours'. When it comes to snooze, you also can snooze without looking or reaching for the phone, just use your voice without disrupting your sleep. I also need to be careful in anticipating misunderstandings of users
  
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

  As Snooze Buddy intends to help users stay focused on their tasks, I intend to use noise/sound recognition & camera + light (if possible) to wake the user up accordingly, but I will try to solely use voice as interaction input to focus on prototyping project around Lab 3 theme.

3. Make a new storyboard, diagram and/or script based on these reflections.


![IMG_0095](https://github.com/csuksangium/Interactive-Lab-Hub/assets/24725647/85cdf253-4a9a-4aef-9a31-092c5b375bc6)


## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

- The Snooze buddy will ask the user how long they would like to sleep for (this will ensure user gets same amount of hours every day rather than wake up time & it will also work conveniently for naps)
- The Snooze buddy will take in user voice as input, attempt to parse number (in words to integer via NLP library) and calculate the timedelta for the wake up time
- The Snooze buddy will sound the alarm and wake the user up, but the user will have the option to snooze via voice
- The snooze will continue until the user wakes up and turns the alarm off

*Include videos or screencaptures of both the system and the controller.*

(implementation code is in speech-scripts/snooze_buddy.py)

*Video*

https://youtu.be/ToEv3grAvw0

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Participants: Mitch & Neo

Answer the following:

### What worked well about the system and what didn't?
What worked well?
- The time conversion and snooze feature worked well in an unlimited loop without hard coding
- The prototype of the device behaved as expected during trial

What did not work well?
- The test with people was not conducted during actual sleep, so it was difficult to attempt to see the real use case
- The system did not have a built-in functionality to exit the program by voice, only through wizarding the controller at the moment


### What worked well about the controller and what didn't?
What worked well about the controller?
- The controller quite flawlessly parsed both user inputs without any issues
  
What did not work well about the controller?
- The controller needed time after speaking to be able to begin parsing input of the user, which lessened the immersion as I needed to instruct when the users could speak


### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

- The system would be better if I could automate when the voice recording will begin and stop based on the user. For example, the device should be able to detect when user speaks and begins recording & stops recording automatically when users are done giving instructions without the need to wizard the terminal.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

- The system could create a dataset of sleep patterns and determine user sleep pattern & behavior over multiple timeframes, like assessing if voice-based alarm leads to better sleep, affects of snoozing on sleep, best sleeping hours that do not lead to snoozing, etc.
- A camera/light sensing modality may make sense in this case to enhance the dimensionality of data by having information about light & its affect on sleeping and waking up.

