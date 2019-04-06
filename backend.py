from collections import Counter
from notify_run import Notify
import os
import time
import dropbox
import json
dropboxkey=""
notify = Notify()
notifyendpoint=""
notify.endpoint=notifyendpoint
notify.write_config()

from flask import Flask,request
maindictionary={}
dbx = dropbox.Dropbox(dropboxkey)
dbx.files_download_to_file("bannedpixel.txt","/bannedpixel.txt")
dbx.files_download_to_file("logpixel.txt","/logpixel.txt")
dbx.files_download_to_file("dictionary.txt","/dictionary.txt")

app = Flask(__name__)
@app.route("/pixel")

def home():
    maindictionary=json.load(open("dictionary.txt"))
    if (request.args.get("id")) in open("bannedpixel.txt").read():
        pass
    elif open("logpixel.txt").read().count(request.args.get("id")) == 0:
        with open("logpixel.txt","a+") as f:
                f.writelines(request.args.get("id") +"\n")
        dbx = dropbox.Dropbox("")

        dbx.files_upload(open("logpixel.txt","rb").read(),"/logpixel.txt",mode=dropbox.files.WriteMode.overwrite)


        maindictionary[request.args.get("id")] = time.time()
        with open('dictionary.txt', 'w+') as file:
                file.write(json.dumps(t))
            
        dbx = dropbox.Dropbox(dropboxkey)
        dbx.files_upload(open("dictionary.txt","rb").read(),"/dictionary.txt",mode=dropbox.files.WriteMode.overwrite)
    elif open("logpixel.txt").read().count(request.args.get("id")) == 1:
      
        if time.time() - maindictionary[request.args.get("id")] > 20:
            
            notify.send('Your email too ' + request.args.get("email") + " with subject: " + request.args.get("subject") + " has been opened")
            text=open("logpixel.txt","a+").read()
            text=text.replace((request.args.get("id")),"")
            with open("logpixel.txt","w+") as f:
                f.write(text)
            with open("bannedpixel.txt","a+") as f:
                f.writelines((request.args.get("id")) + "\n")
            
            dbx = dropbox.Dropbox(dropboxkey)

            dbx.files_upload(open("logpixel.txt","rb").read(),"/logpixel.txt",mode=dropbox.files.WriteMode.overwrite)
            dbx.files_upload(open("bannedpixel.txt","rb").read(),"/bannedpixel.txt",mode=dropbox.files.WriteMode.overwrite)
    return " NONE TEST VIEW  "
if __name__ == "__main__":
    app.run(port= int(os.environ.get('PORT', 5000)),host="0.0.0.0")
