from PyQt5.QtCore import QDir, Qt, QUrl, QTimer
from PyQt5 import QtTest
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)
import sys
import socket, struct, os
import time
#import asyncio
import threading
from random import randint

english = []
roila = []

with open('Roila_Trial3.txt') as currentline:
	trial_lines = currentline.readlines()

for line in trial_lines:
	english.append(line.split(',')[1].strip())
	roila.append(line.split(',')[0].strip())

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the IP address and port.  
localaddr = ("127.0.0.1", 54320)
udp_socket.bind(localaddr)
# Create an increment for while loop
count = 0
# Create a list to restor the data from simulink.
data_collect = []

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

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        global english
        global roila
        self.setWindowTitle("Learning ROILA with a robot tutor")

        self.words = english
        self.index = 0

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
 
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        
        #initial label
        self.label = QLabel("Get ready to listen")
        self.label.setStyleSheet("""
                color: black;
                font: 50px;
        """)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMaximumHeight(100)

        self.openButton = QPushButton("Open Video")   
        self.openButton.clicked.connect(self.openFile)
 
        widget = QWidget(self)
        self.setCentralWidget(widget)
 
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.label)
        #layout.addWidget(self.openButton)
        #layout.addWidget(self.playButton)
 
        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)

        #update timer to loop over videos
        self._update_timer = QTimer()
        E = Engagement()
        self._update_timer.timeout.connect(self.update_video) # triggers update
        self._update_timer.start(12000) # milliseconds (11 sec)

    def update_video(self): #where video gets updated
        try:
            word = self.words[self.index].capitalize() #get word and capitalize
            roila_word = roila[self.index].capitalize()
        except:
            print("End reached at index: ", self.index)
            return "Done"
        
        E = Engagement()
        print(word)
        # no gesture
        fileName = 'C:\\Users\\Jos\\Desktop\\python nao\\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\\bin\\nao_videos\\{}_Plain.mp4'.format(word)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
        self.play() #play video
        subtitles = "{} means {}".format(roila_word,word.lower())
        self.label.setText(subtitles) #where subtitles get updated

        if E < 55:
            print("Adapted")
            QtTest.QTest.qWait(12000)
            fileName = 'C:\\Users\\Jos\\Desktop\\python nao\\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\\bin\\nao_videos\\{}_Gesture.mp4'.format(word)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play() #play video
            subtitles = "{} means {}".format(roila_word,word.lower())
            self.label.setText(subtitles) #where subtitles get updated
            
        self.index += 1 #incrementing to next word


    def openFile(self,word):
        fileName = 'C:\\Users\\Jos\\Desktop\\python nao\\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\\bin\\nao_videos\\{}_Plain.mp4'.format(word)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
 
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
 
app = QApplication(sys.argv)
player = VideoPlayer()
player.resize(640, 480)

player.play()
player.show()
sys.exit(app.exec_())