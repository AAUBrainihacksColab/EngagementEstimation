from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "169.254.6.181", 9559 )

words = ["\\rspd=90\\fawofo \\pau=2000\\ ", "\\rspd=90\\ nijofa \\pau=2000\\", "\\rspd=90\\ metoto \\pau=2000\\", " \\rspd=90\\junobi \\pau=2000\\", "\\rspd=90\\ fonebe \\pau=2000\\"]

for i in words:
	tts.say(i)
	