from flask import *
import os
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

##
led1 = 4
led2 = 17
##

GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, GPIO.LOW)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, GPIO.LOW)

@app.route('/')
def home():
    templateData={
        'led1' : 0,
        'led2' : 0,
        'off'  : 0,
    }
    return render_template('led.html', **templateData)
@app.route('/<led>/<action>')
def led(led,action):
    if led == "off" and action == "off":
        os.system('sudo shutdown -h now')
        templateData={
        'led1' : 0,
        'led2' : 0,
        'off'  : 1,
    }
    elif led == "on" and action == "on":
        os.system('echo "This should not happen"')
        templateData={
        'led1' : 0,
        'led2' : 0,
        'off'  : 0,
    }
    else:
        GPIO.output(int(led), int(action))
        templateData = {
            'led1' : GPIO.input(led1),
            'led2' : GPIO.input(led2),
            'off'  : 0,
        }
    return render_template('led.html', **templateData)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
