from app import app
from flask import request
import os
import subprocess

@app.route("/service",methods=['GET'])
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        #ok = str(subprocess.check_output(['python', '--version']))
        process = subprocess.Popen(['python', './app/gtzankeras/src/app.py', '-t', 'ml', '-m', './app/gtzankeras/models/pipe_svm.joblib', '-s', './app/gtzankeras/data/samples/iza_meu_talisma.mp3'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        returncode = process.wait()
        print('ping returned {0}'.format(returncode))
        ok = str(subprocess.check_output(['pwd']))
        ok1 = str(subprocess.check_output(['ls']))
        print('console {0}'.format(ok))
        print('console1 {0}'.format(ok1))
        print(process.stdout.read())
        return f"Hello from {app_name} running in a Docker container behind Nginx!!!" + request.args['id']
    ok = str(subprocess.check_output(['pwd']))
    #ok = str(subprocess.check_output(['python', './app.py', '-t', 'dl', '-m', '../models/custom_cnn_2d.h5', '-s', '../data/samples/iza_meu_talisma.mp3']))
    process = subprocess.Popen(['python', '/home/ubuntu/projetDocker/app/flask/app/app.py', '-t', 'ml', '-m', '/home/ubuntu/projetDocker/app/flask/app/gtzankeras/models/pipe_svm.joblib', '-s', '/home/ubuntu/projetDocker/app/flask/app/gtzankeras/data/samples/iza_meu_talisma.mp3'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    returncode = process.wait()
    print('ping returned {0}'.format(returncode))
    print(process.stdout.read())

    #return str(process.stdout.read())
    #return "Hello from Flask"
    return str(ok)
