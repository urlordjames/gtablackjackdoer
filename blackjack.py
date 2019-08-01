import readnum
from gtts import gTTS
from mss import mss
import random
import os
from playsound import playsound
import time
from getbestmove import getmove

def process():
    screen = mss()
    screen.shot(output="screenshot.png")

    number = readnum.getnum("screenshot.png", True)
    return number

def say(instruction):
    filename = "audio/" + genname(6) + ".mp3"
    tts = gTTS(instruction)
    tts.save(filename)
    print(instruction)
    playsound(filename)

def dothething():
    number = process()

    instruction = ""

    if number == 0:
        instruction = "failed to recognise card total"
    else:
        say(str(number))
        say("okay, show me the dealer")
        time.sleep(2)
        dealernum = process()
        if not dealernum == 0:
            say(str(dealernum))
            time.sleep(1)
            instruction = getmove(number, dealernum)
        else:
            instruction = getmove(number)

    say(instruction)



def genname(n):
    breh = ""
    for i in range(0, n):
        breh += (random.choice(["a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]))
    return breh

while True:
    dothething()
    time.sleep(3)
