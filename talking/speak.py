from gtts import gTTS


content = input("你想要說什麼：")
tts = gTTS(content, lang="zh-tw")
tts.save("test.mp3")

