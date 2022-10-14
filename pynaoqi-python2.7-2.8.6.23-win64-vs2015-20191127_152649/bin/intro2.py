from naoqi import ALProxy
gesture = ALProxy("ALAnimatedSpeech", "169.254.123.126", 9559)
tts = ALProxy("ALTextToSpeech", "169.254.123.126", 9559 )

eeg_intro2 = """ 
Now we will continue the calibration task. I will tell you 10 words, and you will need to remember them in order. \\pau=500\\
Then I will ask you which word was in a certain position. \\pau=500\\
For example, I will ask you \\pau=500\\ "What was the 7th word?"  \\pau=500\\ and you will have to think of the answer. \\pau=500\\
Please don't say the answer out loud, the humans told me you need you to sit as still as possible during this part. \\pau=500\\





"""
#Before we start, let's have a short break with some Tai Chi Chuan, I will perform some movements and you can relax with the calming music. \\pau=500\\

a = gesture.post.say(eeg_intro2)
gesture.wait(a, 0)
#b = gesture.post.say(" ^mode(disabled) ^run(tai/behavior_1)   ^stop()")
#gesture.wait(b, 0)
#gesture.post(" ^mode(disabled) ^start(tai/behavior_1) ")

eeg_intro3 = ''' Okay now we are going to do the calibration! Please remember the following words   \\pau=3000\\'''
c =  gesture.post.say(eeg_intro3)
gesture.wait(c, 0)

n_back = ["fish \\pau=1000\\", "toast \\pau=1000\\", "screen \\pau=1000\\", "chair \\pau=1000\\", "sun \\pau=1000\\", "coffee \\pau=1000\\", "phone \\pau=1000\\", "box \\pau=1000\\", "grass \\pau=2000\\"]

for word in n_back:
    gesture.post.say("\\rspd=90\\" + word)

gesture.post.say("What was the last word I said? \\pau=5000\\")
gesture.post.say("What was the word before that? \\pau=5000\\")
gesture.post.say("What was the fifth word? \\pau=5000\\")
gesture.post.say("What was the third word? \\pau=5000\\")