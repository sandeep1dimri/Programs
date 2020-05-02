#Program : Text to Speech, and Speech recognition , this is small program to test math skill
#pip install pyttsx3 --> Lib to support text to audio
#pip install SpeechRecognition speech to text
#first do : brew install portaudio and then pip install PyAudio. brew is needed if PyAudio give error in installtion

import pyttsx3 as p_tts
import speech_recognition as sr
import time
import re

import random
#Constants
MATH_OPERATORS=['+','-'] #math operations
Count_Of_Numbers=3 #Count of Numbers on which math operation needed
Number_Range=[1,9] #Numbers Range
TOTAL_QUESTIONS=2 # Number of question or repeatation

Questions_verbose=[]
for ques in range(1 , TOTAL_QUESTIONS+1):
    exp=""
    while(1):
        for each_c in  range(1,Count_Of_Numbers+1):
            exp=exp+str(random.randint(Number_Range[0],Number_Range[1]))
            if each_c < Count_Of_Numbers:
                exp=exp+str(MATH_OPERATORS[random.randint(0,len(MATH_OPERATORS)-1)])
        if eval(exp) > 0: #to take only positive solution
            break
        else:
            #break
            exp=""
    Questions_verbose.append([exp,eval(exp)])    
    print(ques,":",exp,"-->",eval(exp)) 
print(Questions_verbose)


class TeToS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = p_tts.init()


    def start(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        


answers=[]
text_response=[]
for each in Questions_verbose:
    
    print(each[0])
    text_to_speech=(each[0].replace('+','Plus')).replace('-','Minus')

    r = sr.Recognizer()

    text=""
    with sr.Microphone() as source:
        tts = TeToS()
        tts.start(text_to_speech)
        del(tts)
        
        print("Talk Now")
        try:
            audio_text = r.listen(source,timeout=5) #,timeout=5
        except Exception as e:
            print("audio text missing:",str(e))
            print("Could not request results from Google Speech  Recognition service; {0}".format(e)) 
        print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition, so internet is needed on machine 
            # No Internet:will get recognition connection failed: [Errno 8] nodename nor servname provided, or not known
            text=r.recognize_google(audio_text)
            print("Response: "+ text)
            values=[int(each) for each in re.findall(r'-?\d+',text)]
            text_response.append(values[0])
            if int(each[1]) == int(values[0]):
                print("Correct response!")
                answers.append("Correct")
            else:
                answers.append("Incorrect")
                print("Incorrect response!")
        except Exception as e1:
             print("Sorry, missed the response:{0}".format(e1))
             answers.append("Incorrect")

print("Question Set:",Questions_verbose)
print("Response:",text_response)
print("Correct Matrix",answers) 

print("Correct: {:.0%}".format((len(list(filter(lambda x: x=="Correct",answers)))/(len(answers))) ))


