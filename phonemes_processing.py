# Natural Language Library
import nltk

# Speech Library
import pyttsx
from  AppKit import NSSpeechSynthesizer
import time
import sys

# Reading the input File
file_content = open("sample.txt").read()

# Creating Tokens based on the text on the file
tokens = nltk.word_tokenize(file_content)
print tokens

# Getting from the library the phonemes of all English Words
entries = nltk.corpus.cmudict.entries()
# print len(entries)

# Getting the correspondence between the words and the phonemes
# phonemes = {}
# for token in tokens:
#     for entry in entries:
#         if token == entry[0] and not phonemes.has_key(token):
#             phonemes[token] = entry[1]
#
# print phonemes

nssp = NSSpeechSynthesizer
ve = nssp.alloc().init()
# for voice in nssp.availableVoices():

# "com.apple.speech.synthesis.voice.Agnes",
# "com.apple.speech.synthesis.voice.Albert",
# "com.apple.speech.synthesis.voice.Alex",
# "com.apple.speech.synthesis.voice.BadNews",
# "com.apple.speech.synthesis.voice.Bahh",
# "com.apple.speech.synthesis.voice.Bells",
# "com.apple.speech.synthesis.voice.Boing",
# "com.apple.speech.synthesis.voice.Bruce",
# "com.apple.speech.synthesis.voice.Bubbles",
# "com.apple.speech.synthesis.voice.Cellos",
# "com.apple.speech.synthesis.voice.Deranged",
# "com.apple.speech.synthesis.voice.Fred",
# "com.apple.speech.synthesis.voice.GoodNews",
# "com.apple.speech.synthesis.voice.Hysterical",
# "com.apple.speech.synthesis.voice.Junior",
# "com.apple.speech.synthesis.voice.Kathy",
# "com.apple.speech.synthesis.voice.Organ",
# "com.apple.speech.synthesis.voice.Princess",
# "com.apple.speech.synthesis.voice.Ralph",
# "com.apple.speech.synthesis.voice.Trinoids",
# "com.apple.speech.synthesis.voice.Vicki",
# "com.apple.speech.synthesis.voice.Victoria",
# "com.apple.speech.synthesis.voice.Whisper",
# "com.apple.speech.synthesis.voice.Zarvox"

#ve.setVoice_("com.apple.speech.synthesis.voice.Zarvox")
print file_content
#ve.startSpeakingString_(file_content)

time.sleep(1)
while ve.isSpeaking():
    time.sleep(1)

#for token in tokens:
#    ve.startSpeakingString_(token)
#    time.sleep(1)
#    while ve.isSpeaking():
#        time.sleep(1)

