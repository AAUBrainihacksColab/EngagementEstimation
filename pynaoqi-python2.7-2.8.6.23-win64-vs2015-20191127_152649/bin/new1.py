from naoqi import ALProxy
gesture = ALProxy("ALAnimatedSpeech", "169.254.86.4", 9559)
tts = ALProxy("ALTextToSpeech", "169.254.86.4", 9559 )



    #If good engage do twice no gesture
    
    
gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) {} means {} ^mode(disabled)\\pau=10000\\".format("left","sujosi","left"))
gesture.post.say(" ^mode(disabled) ^start({}/behavior_1) {} means {} ^mode(disabled)\\pau=10000\\".format("right","sujosi","right"))
