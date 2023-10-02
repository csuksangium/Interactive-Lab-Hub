import spacy
import sys
import json
import time
from vosk import Model, KaldiRecognizer
import os
import subprocess
import sounddevice as sd
import queue
from words2num import w2n
from datetime import datetime, date, timedelta

nlp = spacy.load('en_core_web_sm')


def speak(text):
    command = '''
    say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
    say " placeholdertext"
    '''
    command = command.replace('placeholdertext', text)
    subprocess.call(['bash', '-c', command])


def convert_text_to_datetime(time_text):
    formatted_time = datetime.strptime(time_text, "%I:%M%p")
    today = date.today()
    full_datetime = datetime.combine(today, formatted_time.time())
    return full_datetime


def calc_sleep_time(time_tuple):
    duration = timedelta(hours=time_tuple[0], minutes=time_tuple[1])
    current_time = datetime.now().time()
    current_datetime = datetime.combine(datetime.today(), current_time)
    new_datetime = current_datetime + duration
    return new_datetime


def convert_words_to_time(text):
    doc = nlp(text)
    resu = []
    for token in doc:
        if token.ent_type_ == 'TIME':
            time_components = token.text.split(':')
            print(time_components)
            resu += time_components

    print(resu)
    if ('hour' in resu or 'hours' in resu) and ('minute' in resu or 'minutes' in resu):
        hours = w2n(resu[0])
        mins = w2n(resu[2])
        return (hours, mins)

    elif('hour' in resu or 'hours' in resu) and not ('minute' in resu or 'minutes' in resu):
        hours = w2n(resu[0])
        return (hours, 0)

    elif not ('hour' in resu or 'hours' in resu) and ('minute' in resu or 'minutes' in resu):
        mins = w2n(resu[0])
        return (0, mins)

    else:
        return None


q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def recordAudio():
    model = Model(lang="en-us")
    try:
        file_name = time.strftime("%Y%m%d-%H%M%S") + ".json"
        dump_fn = open(file_name, "wb")

        with sd.RawInputStream(samplerate=16000, blocksize=8000,
                               dtype="int16", channels=1, callback=callback):
            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            rec = KaldiRecognizer(model, 16000)
            result = ""
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    resp = json.loads(rec.Result())['text']
                    print("Result ", resp)
                    result += resp
                else:
                    resp = json.loads(rec.PartialResult())['partial']
                    print("Partial ", resp)
                if len(data) == 0:
                    break

    except KeyboardInterrupt:
        print(result)
        print("\nDone")
        return result
    except Exception as e:
        print("exit")


def alarm(dtt):
    while True:
        set_alarm_for = 'Sure. Setting alarm for ' + str(dtt.hour) + str(dtt.minute)
        speak(set_alarm_for)
        now = datetime.now()
        delta = dtt - now
        if delta > timedelta(0):
            print('will sleep: %s' % delta)
            time.sleep(delta.total_seconds())
            print('just woke up')

        while True:
            speak("It is time to wake up")
            duration = 1  # seconds
            freq = 440  # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
            response = recordAudio()
            if response is None:
                continue
            if response is not None:
                dtt = snooze(response)
                break


def snooze(response):
    res = convert_words_to_time(response)
    print(res)
    new_dt = calc_sleep_time(res)
    return new_dt


while True:
    speak('Hello. How long would you like to sleep for?')
    response = recordAudio()
    print("Response ", response)
    res = convert_words_to_time(response)
    print(res)
    dt = calc_sleep_time(res)
    print(dt)
    alarm(dt)
