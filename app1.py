from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

if __name__ == "__main__":
    app.run(debug=True, threaded=True)