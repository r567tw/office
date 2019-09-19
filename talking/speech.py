from gtts import gTTS
import os

f = open("content.txt", "r")
content = f.read()

tts = gTTS(content, lang="zh-tw")
tts.save("test.mp3")

