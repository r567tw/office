import speech_recognition as sr

recog = sr.Recognizer()
with sr.Microphone() as source:
    audioData = recog.listen(source)
try:
    test = recog.recognize_google(audioData, language="zh-tw")
    print(test)
except:
    print("聽不懂")

