from json import loads
from time import sleep

import cv2
import imutils
from flask import (Flask, Response, make_response, redirect, render_template,
                   request)
from flask_cors import CORS, cross_origin
from imutils.video import VideoStream

app = Flask(__name__)
cors = CORS(app)

video_processing_trigger = False
video_processing_trigger_dict = {
    'false': False,
    'true': True
}


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/select", methods=['POST'])
@cross_origin()
def video_processing_trigger_select():
    global video_processing_trigger
    video_processing_trigger = video_processing_trigger_dict[
        loads(request.data.decode()).get('key')
    ]
    return make_response("200_OK", 200)


def hello2():
    cap = VideoStream(src=0).start()
    sleep(2)
    while True:
        frame = cap.read()
        frame = imutils.resize(frame, width=800)
        if video_processing_trigger:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        if not flag:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route("/video")
def video():
    return Response(hello2(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


app.run(debug=True, host="0.0.0.0", port=5001)
