import cv2
import numpy as np
import os
import time
import sys
import nltk
import phonemes
import thread
import time
from  AppKit import NSSpeechSynthesizer

#Defines
timePerPhoneme = 0.15
longPhonemeBonus = 0.05
smallPhonemeBonus = -0.05

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

start_time = time.time()
TextToSpeech = []
for token in tokens:
    for entry in entries:
        if token.lower() == entry[0]:
            #print entry
            TextToSpeech.append(entry)
            break
end_time = time.time()
#Debug!
print "Pre-processing Done! Time: %s Seconds"%(end_time - start_time)
#print TextToSpeech
#print phonemes.mouths
#print phonemes.PhonemeToMouth


## For each mouth you should put a refering mouth to show
## do the double check
for word in TextToSpeech:
    # cv2.imshow('window', phonemes.mouths['blair_rest.jpg'])
    # cv2.waitKey(1)
    # Get the right list of mouths

    timeForAWord = 0.0
    timeOfThisPhoneme = 0.0
    MouthsToShow = []
    for ph in word[1]:
        for key, value in phonemes.PhonemeToMouth.items():
            if '1' in ph:
                timeForAWord += timePerPhoneme + longPhonemeBonus
                timeOfThisPhoneme = timePerPhoneme + longPhonemeBonus
            elif '0' in ph:
                timeForAWord += timePerPhoneme + smallPhonemeBonus
                timeOfThisPhoneme = timePerPhoneme + smallPhonemeBonus
            else:
                timeForAWord += timePerPhoneme
                timeOfThisPhoneme = timePerPhoneme
            if key in ph:
                MouthsToShow.append((value, timeOfThisPhoneme))


    #Debug!
    #print MouthsToShow

    # Call co-routine to speak
    try:
        t = thread.start_new_thread(speak_word, (word[0], timeForAWord ) )
    except:
        print "Error: unable to start thread for audio =/"

    #Show Mouths
    for mouth in MouthsToShow:
        img = phonemes.mouths[mouth[0]]
        cv2.imshow('window', img)
        cv2.waitKey(1)
        time.sleep(mouth[1])
