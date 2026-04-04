from flask import Flask, render_template, Response
import cv2
import os
from ai_model import process_frame

app = Flask(__name__)

# 🔥 CAMERA STREAM (LIVE AI IN WEBSITE)
def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = process_frame(frame, "squat")

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# 🔥 HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")


# 🔥 LIVE VIDEO ROUTE (BEST FEATURE)
@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# 🔥 OPTIONAL: OLD METHOD (OPENS TERMINAL AI)
@app.route('/start')
def start_ai():
    os.system("python3 ../src/main.py -t squat")
    return "AI Training Started! Check your camera."


# 🔥 RUN APP
if __name__ == "__main__":
    app.run(debug=True)