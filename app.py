
"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from mbta_helper import find_stop_near
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

location= input("Insert Your Location")
print(find_stop_near(location))


@app.route('/website')
def website():
    stop, wheelchair = find_stop_near(location)
    if wheelchair == 1:

        return 'Neareast is {}. It is wheelchair accessible.'.format(stop)
    else:
        return 'Neareast is {}. It is NOT wheelchair accessible.'.format(stop)