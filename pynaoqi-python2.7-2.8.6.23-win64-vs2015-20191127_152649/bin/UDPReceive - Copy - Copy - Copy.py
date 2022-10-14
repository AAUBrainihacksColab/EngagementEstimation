#!/usr/bin/env python    
# -*- coding: utf-8 -*

import socket, struct, os
import time
#import asyncio
import threading
from naoqi import ALProxy
from random import randint

import Tkinter as tk #Tkinter for 2.
from Tkinter import *



gesture = ALProxy("ALAnimatedSpeech", "169.254.123.126", 9559)
tts = ALProxy("ALTextToSpeech", "169.254.123.126", 9559 )


#beginning of condition 1
introduction_1 = """ \\rspd=90\\ It's time to start the first condition! \\pau=500\\ 
I'm going to teach you 15 words now. Try to sit as still as possible. \\pau=1500\\

"""
#end of condition 1
finished_1 = """That's it for now! \\pau=500\\ You've learned 15 new words in Roila. Good job! \\pau=500\\ The humans will
give you a little quiz now. \\pau=500\\ Just pick the meaning of each word in English from 4 options. \\pau=500\\ If you
want to hear me say the word again, click the pronounce button. Good luck! \\pau=1500\\"""

#beginning of condition 2
introduction_2 = """It's time for another set of words! \\pau=500\\ I will teach you 15 more words, \\pau=500\\ just like before, 
\\pau=500\\ and then you will take the test again. \\pau=500\\  Only this time, the words will be different.  \\pau=500\\ Get ready to learn some Roila!"""

#end of condition 2
finished_2 = """Well done! You learned another 15 new words. It's time to take the quiz now. Just do your best
and after that, the humans will give you some questionnaires to see what you thought of me and your experience.
Thank you for being such a good student!"""

#list of intervention prompts
interventions = ["Maybe I should say that again", "Oh, I think you might have missed something", "Let's try that again!",
"Let me say that again", "Maybe we need another repetition, here it comes", "Let's do the last word again", "Oops, maybe that wasn't clear. Once more"
, "The last word was", "Did you miss something? Don't worry, we can do it again", "And once more for good measure", "I think this will help you remember"]

gesture.post.say(introduction_1)
gesture.post.say("Are you ready to start the experiment? \\pau=2000\\")
gesture.post.say("Get \\emph=1\\ ready to listen! \\pau=2000\\")

tts.setParameter("pitchShift", 1)
#tts.say("Are you ready to start the experiment? \\pau=2000\\")
#tts.say("Get \\emph=1\\ ready to listen! \\pau=2000\\")
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the IP address and port.  
localaddr = ("127.0.0.1", 54320)
udp_socket.bind(localaddr)
# Create an increment for while loop
count = 0
# Create a list to restor the data from simulink.
data_collect = []

gui = Tk()

def sample():
    i = 0
    while (True):
        recv_data = udp_socket.recvfrom(1024)
        #print(recv_data)
        
        out, info = recv_data
        testResult = struct.unpack('>B', out)
        #RealNumber = ord(out)
        for a in testResult:
            RealNumber = a
            
        #input_bytes = b"\x00\x01" #note that this might need to change in python 2.7
        #output_numbers = list(input_bytes)
        Engagement = open('engagement.txt', 'a')
        Engagement.write(str(a))
        Engagement.write(",")
        Engagement.close()
                    

def Engagement():
    
    Engagementnum = ""
    englili = []
    with open("engagement.txt", 'r+') as f:
        lines = f.readlines()
        print("lines: ", lines)
        for a in lines:
            for b in a:
                if (b != ","):
                    #print("the number a is: ", b)
                    Engagementnum += str(b)
                else:
                    englili.append(int(Engagementnum))
                    Engagementnum = ""
                
            print(englili)
            f.truncate(0)
    average = sum(englili)/len(englili)
    print("The average Engagement is: ", average)
            #tts.say("your average engagement is: " )
            #tts.say(str(average))
    
    print("Resetting the list now, hold on")
    return average

t1 = threading.Thread(target = sample) 
t1.start() 

roila = []
english = []

 
# set the size of the GUI Window
gui.geometry("1680x1050")
#gui.attributes("-fullscreen", True)
# set the title of the Window
gui.title("Learning ROILA")
word = ""        
# The title to be shown
title = Label(gui, text="Words in ROILA with their meanings",
width=108, height=2, bg="#81C784",fg="#212121", font=("calibri", 17, "bold"))
# place of the title
title.place(x=0, y=2)


def change_word(roila,english):
    #placeholder = StringVar()
    gui.label = tk.Label(gui, text="{} means {}.".format(roila.capitalize(),english), width=100,font=( 'calibri' ,60, 'bold' ), anchor= 'w', fg="#212121")
    #placeholder.set(word)
    #placing the option on the screen
    gui.label.place(x=250, y=300)
  
        
t1 = threading.Thread(target = sample) 
t1.start() 

roila = []
english = []


with open('Roila_Trial1.txt') as currentline:
        dict_lines = currentline.readlines()

#Make dict
for line in dict_lines:
    line.replace('\n','')
    roila.append(line.split(',')[0])
    english.append(line.split(',')[1].strip())
#Zip dict
roila_english = dict(zip(roila,english))
count = 0
#Loop dict
for roila,english in roila_english.items(): #change to .iteritems() for python 2.x
    #time.sleep(5)
    #If good engage do twice no gesture
    change_word(roila,english)
    gui.update_idletasks()
    gui.update()
    count += 1
    print(count)
    print(english)
    for i in range(2):
        a = gesture.post.say(" ^mode(disabled)  \\rspd=50\\ \\emph=1\\ {} \\pau=500\\ \\rspd=80\\ means \\emph=1\\ {} ^mode(disabled)\\pau=2000\\".format(roila,english))
        gesture.wait(a, 0)
    #If bag engage do again with gesture
    E = Engagement()
    #E = randint(1,160)
    print(E)
    if E < 55:    
        print("Adapted")
        index = randint(0,len(interventions)-1)
        gesture.post.say(interventions[index])
        b= gesture.post.say(" ^mode(disabled) ^start({}/behavior_1)  \\rspd=50\\ \\emph=1\\ {} \\pau=500\\ \\rspd=80\\ means \\emph=1\\ {} ^mode(disabled)\\pau=4000\\ ^stop()".format(english,roila,english))
        gesture.wait(b, 0)
        E = Engagement()
    else:
        continue

gesture.post.say(finished_1)
gui.destroy()


#execfile("non-adaptive.py")
#t1.join()
#udp_socket.close()



