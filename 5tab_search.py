import requests, sys, webbrowser, bs4
import time
import os
from gtts import gTTS



res = requests.get("http://google.com/search?q="+" ".join(sys.argv[1:]))
res.status_code

text = " ".join(sys.argv[1:])

tts = gTTS(text = "Searching "+text+ "." +" Please keep patience.", lang = "en")
tts.save("feeling_lucky.mp3")
os.system("mpg321 feeling_lucky.mp3")

time.sleep(2)

webbrowser.open("http://google.com/search?q="+" ".join(sys.argv[1:]))

soup = bs4.BeautifulSoup(res.text)

ElemLinks = soup.select(".r a")
openTab = min(5,len(ElemLinks))
for i in range(0,openTab):
	webbrowser.open("http://google.com"+ElemLinks[i].get("href"))
