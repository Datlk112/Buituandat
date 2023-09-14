from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot Get UID By Bùi Tuấn Đạt "

def runn():
  app.run()

def btd():
    t = Thread(target=runn)
    t.start()