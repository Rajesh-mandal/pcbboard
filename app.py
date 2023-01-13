from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
import cv2
import base64 
import json

app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/detect", methods=['GET','POST'])
def detect():
    file = request.files['file']
    file.save(os.path.join(uploads_dir, secure_filename(file.filename)))
    subprocess.run("dir", shell=True)
    subprocess.run(['python', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(file.filename))], shell=True)


    filename = secure_filename(file.filename)
    # print("filename:",filename)
    # if filename in os.listdir('static'):
    #     get_path = 'static'+'/' +filename
    #     img = cv2.imread(get_path)
    #     cv2.imshow('flask img',img)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    with open('static'+'/' +filename, "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode("utf-8")
    return json.dumps({"success": 1, "filename":my_string})


@app.route("/opencam", methods=['GET'])
def opencam():
    print("here")
    subprocess.run(['python', 'detect.py', '--source', '0'], shell=True)
    return "done"
    

@app.route('/return-files', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    # print("obj-------------------------",obj)
    loc = os.path.join("static", obj)
    # print("loc==============",loc)
    try:
        return send_file(os.path.join("static", obj), attachment_filename=obj)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)