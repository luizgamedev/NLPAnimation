import cv2
import numpy as np
import os
import time
import sys
import nltk
import phonemes
import thread
from  AppKit import NSSpeechSynthesizer

#Defines
timePerPhoneme = 0.2

# called by each thread
def speak_word(word, waittime):
    nssp = NSSpeechSynthesizer
    ve = nssp.alloc().init()
    ve.setVoice_("com.apple.speech.synthesis.voice.Alex")
    ve.startSpeakingString_(word)

    time.sleep(waittime)
    return


file_content = open("sample.txt").read()
tokens = nltk.word_tokenize(file_content)
print tokens

entries = nltk.corpus.cmudict.entries()
print len(entries)


TextToSpeech = []
for token in tokens:
    for entry in entries:
        if token.lower() == entry[0]:
            #print entry
            TextToSpeech.append(entry)
            break
#Debug!
print TextToSpeech
print phonemes.mouths
print phonemes.PhonemeToMouth


## For each mouth you should put a refering mouth to show
## do the double check
for word in TextToSpeech:
    cv2.imshow('window', phonemes.mouths['blair_rest.jpg'])
    cv2.waitKey(1)
    # Get the right list of mouths

    MouthsToShow = []
    for ph in word[1]:
        for key, value in phonemes.PhonemeToMouth.items():
            if key in ph:
                MouthsToShow.append(value)

    #Debug!
    print MouthsToShow

    # Call co-routine to speak
    try:
        thread.start_new_thread(speak_word, (word[0], len(word[1]) * timePerPhoneme ) )
    except:
        print "Error: unable to start thread for audio =/"

    #Show Mouths
    for mouth in MouthsToShow:
        img = phonemes.mouths[mouth]
        cv2.imshow('window', img)
        cv2.waitKey(1)
        time.sleep(timePerPhoneme)