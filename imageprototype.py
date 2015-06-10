import cv2
import numpy as np
import os
import time
import sys
import nltk
import phonemes

# called by each thread
def speak_word(word, waittime):
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

    # Get the right list of mouths

    MouthsToShow = []
    for ph in word[1]:
        for key, value in phonemes.PhonemeToMouth.items():
            if key in ph:
                MouthsToShow.append(value)

    #Debug!
    print 'Mouths to Show: ' + MouthsToShow

    # Call co-routine to speak

    #Show Mouths
    for mouth in MouthsToShow:
        img = phonemes.mouths[mouth]
        cv2.imshow('window', img)
        cv2.waitKey(1)
        time.sleep(0.2)