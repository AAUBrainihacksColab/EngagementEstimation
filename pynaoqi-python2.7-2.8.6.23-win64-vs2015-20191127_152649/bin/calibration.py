from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "169.254.76.37", 9559 )


n_back = ["toast \\pau=1000\\", "fish \\pau=1000\\", "trash \\pau=1000\\", "apple pie \\pau=1000\\", "cheese \\pau=1000\\", "robot \\pau=1000\\", "sleep \\pau=1000\\", "coffee \\pau=1000\\", "fall \\pau=1000\\"]

for word in n_back:
    tts.say("\\rspd=90\\" + word)

tts.say("What was the last word I said? \\pau=5000\\")
tts.say("What was the word before that? \\pau=5000\\")
tts.say("What was the fifth word? \\pau=5000\\")
tts.say("What was the third word? \\pau=5000\\")