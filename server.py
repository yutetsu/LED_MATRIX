# -*- coding: utf-8 -*-
import os, glob
from flask import Flask, request, send_from_directory
from train_rom import train

## Webserver
app = Flask(__name__)
@app.route('/', methods=['POST'])
def getvar():
    print("[RECIVED] CMD: "+request.form.get('CMD', "NONE")+", TRAIN: "+request.form.get('TRAIN', "NONE")+", SPECIAL: "+request.form.get('SPECIAL', "NONE")+", TYPE: "+request.form.get('TYPE', "NONE")+", DEST: "+request.form.get('DEST', "NONE")+", LINE: "+request.form.get('LINE', "NONE")+", FULL_TYPE: "+request.form.get('FULL_TYPE', "FALSE"))
    for CleanUp in glob.glob('BIN/*.*'):
        if not CleanUp.endswith('grid.png') and not CleanUp.endswith('アドレス1.gif'):    
            os.remove(CleanUp)
    return train(request.form.get('CMD', ""), request.form.get('TRAIN', ""), request.form.get('SPECIAL', ""), request.form.get('TYPE', ""), request.form.get('DEST', ""), request.form.get('LINE', ""), request.form.get('FULL_TYPE', "FALSE"))

@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('BIN', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

