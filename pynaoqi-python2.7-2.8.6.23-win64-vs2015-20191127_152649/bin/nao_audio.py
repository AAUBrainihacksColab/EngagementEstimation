from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "169.254.82.33", 9559 )
tts.setParameter("pitchShift", 1.1)

roila = []

with open("roila_dict2.txt") as currentline:
        dict_lines = currentline.readlines()
        
for line in dict_lines:
        line.replace("\n", "")
        right_answer = line.split("\t")[0].strip()
        roila.append(right_answer)
        
for word in roila:
    tts.say(word + "\\pau=4000\\")