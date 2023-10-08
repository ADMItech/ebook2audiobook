###################################
# !/usr/bin/python
# Python 3.10
# (C) 2023 admi.tech
###################################

# Import main packages
from gtts import gTTS
import mobi
import html2text

# TODO 1: Read .mobi and turn it to text
tempdir, filepath = mobi.extract("rawdata/postsedliaci_ukazka.mobi")
file = open(filepath, "r")
content = file.read()

# TODO 2: Turn text to audio file
# Create text
mytext: str = html2text.html2text(content)
# Pick language / 'sk': 'Slovak' , 'en': 'English'
language = 'sk'
# Create audio object
myobj = gTTS(text=mytext, lang=language, slow=False)
# save to local folder:
myobj.save("output/audiobook.mp3")