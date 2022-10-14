from naoqi import ALProxy
gesture = ALProxy("ALAnimatedSpeech", "169.254.185.62", 9559)


eeg_intro = """
\\rspd=90\\ Hello! My name is Nao. I'm a social robot and today, I will be your language tutor. \\pau=500\\ But first,
the humans need to put an E E G cap on your head, so I can monitor your brainwaves! \\pau=500\\
That sounds pretty wild, right? \\pau=500\\

But don't worry, it won't hurt and it's perfectly safe! \\pau=500\\
You will just have a fabric cap with some plastic parts the contain
electrodes on your head. \\pau=500\\ To make your brainwaves more easy to read, the humans will add some 
conductive gel to three frontal electrodes closest to your forehead, once the cap is on. \\pau=500\\
This reduces impedence. The gel is designed to be safe for human skin, but it might feel a little cold when it is applied. \\pau=500\\ The humans also tell me the gel tastes salty.\\pau=500\\ I am not sure what that means. \\pau=500\\ As a robot, I am not 
capable of experiencing the sensation of salty. \\pau=500\\ On another note, I am also not sure why the humans have consumed the gel. \\pau=500\\
I definitely do not recommend that you do the same. \\pau=500\\It is not in my database of acceptable human foods. \\pau=500\\

Once the cap is on, feel free to adjust the cap or your hair to get more comfortable! \\pau=500\\ In case you came here with glasses,
remember to put them back on, so you can see everything clearly during the experiment. \\pau=500\\

Before we start, I also want to tell you more about what we'll be doing today. \\pau=500\\ I will be teaching
you a language called Roila.\\pau=500\\  Roila means robot interaction language! \\pau=500\\
It is an artificial language made for robots - it is easier for us to understand
than other languages. \\pau=500\\ Roila doesn't resemble any human lanuages you might be used to,
so you probably won't recognize any of the words. \\pau=500\\ But don't worry, I'll tell you everything
you need to know! \\pau=500\\ All you need to do is sit still and listen to me. \\pau=500\\You will also see the words
spelled out on a screen in front of you when I say them, 
so you can learn both the spelling and pronounciation at the same time. \\pau=500\\

I will teach you a total of 45 words today and we'll do this in three parts. \\pau=500\\
These three parts are what the humans call conditions. \\pau=500\\In one of the conditions, I will
adapt to your brainwaves to try to help you remember more words. \\pau=500\\ I do this by trying to figure
out how engaged you are and if you might have missed a word. \\pau=500\\ In the other condition, I won't have
access to your brain waves and will just have to guess when you're distracted randomly. \\pau=500\\ For the sake
of science, I can't tell you which condition is which - they will happen in random order
and they will both look the same to you. \\pau=500\\ There is another condition where I will leave the room and talk to you virtually on the screen.

In each condition, I will teach you 15 words by repeating them twice along with their meanings. \\pau=500\\
If I think it is needed, I will repeat it a third time and do a little gesture for you to help you remember. \\pau=500\\  
After we're done with the words, I'll give you a short multiple choice quiz to see what you remembered. \\pau=500\\ This is to see if I've done a good job teaching you! \\pau=500\\

When you do the quiz, you will be asked to choose the meanings of words in Roila from 4 options. \\pau=500\\
After the quiz, the humans will also give you a questionnaire to see how you felt about me and
your learning experience. \\pau=500\\Then you can have a break and relax for a bit before we start the next part,
which will look very similar - only the words will be different! \\pau=500\\

When the experiment starts, there will be some times where I'll need you to sit as still as possible.\\pau=500\\
When you move even a little bit, the data from your brain waves gets noisy and it's harder for me to tell what to do.\\pau=500\\
So it really helps if you can do your best statue impression for these bits. \\pau=500\\

I will let you know when it's time to sit still, the rest of the time you can just make yourself comfortable. \\pau=500\\
"""

english = "test"
roila = "fafaku"
gesture.post.say("hi")


#gesture.post.say(" ^mode(disabled) ^start({}/behavior_1)  \\rspd=50\\ \\emph=1\\ {} \\pau=500\\ \\rspd=80\\ means \\emph=1\\ {} ^mode(disabled)\\pau=4000\\ ^stop()".format(english,roila,english))