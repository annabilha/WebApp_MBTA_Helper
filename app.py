
"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, request, render_template
from mbta_helper import find_stop_near
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

# location= input("Insert Your Location")
# print(find_stop_near(location))


@app.route('/website', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        location = request.form['location']
        stop, wheelchair = find_stop_near(location)

        if wheelchair == 1:
            return render_template('mbta_helper_result.html', stop=stop, wheelchair="wheelchair accessible")
        else:
            return render_template('mbta_helper_result.html', stop=stop, wheelchair="not wheelchair accessible")

    return render_template('mbta_helper_form.html')




