# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:17:44 2021

@author: Eng Fatima
"""

from gtts import gTTS
import os 


#Readinf files
f = open(r"abobakr.txt",'r',  encoding='utf-8')

text = str(f.read())

#preprocessing

#sh = Shakkala(r"C:\Users\Eng Fatima\spyder proj\gTTS_grad_proj\requirements", version={3})


print(text)

#convert text to mp3
tts = gTTS(text, lang= 'ar' ,lang_check=(True) ,slow=(True) )
tts.save('newhello.mp3')
os.system('newhello.mp3' )